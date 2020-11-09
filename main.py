import struct
import re
from bit_utils import find_next_null, write_bits
from item_data import ItemGroup, Rarity
from item import Item
from page import Page
import tkinter as tk
from tkinter import filedialog
from shutil import copy
import configparser

root = tk.Tk()
root.withdraw()


def read_stash_file(file_path):
    # Read stash file and return header, stash version, shared gold (if applicable), number of pages and the rest of
    # the stash data
    with open(file_path, "rb") as f:
        header = f.read(4)
        ver = f.read(2)
        gold = None

        # There is some difference between versions and shared/personal stash files here. If the stash is a shared stash
        # ("SSS\0") and the version is 02, we need to read 4 bytes into shared gold. If the stash is a personal stash
        # ("CSTM") then we need to read 4 unused junk bytes. Otherwise, skip.
        if header == b'SSS\x00' and ver == b'02':
            gold = f.read(4)
        if header == b'CSTM':
            f.read(4)

        num_pages = struct.unpack('I', f.read(4))[0]
        stash_data = f.read(-1)
    return header, ver, gold, num_pages, stash_data


def get_flags(stash_data, ptr):
    # Check if flags exist by counting past the next null and checking for JM
    next_null = find_next_null(stash_data, ptr)
    if stash_data[next_null + 1: next_null + 3] != b'JM':
        return stash_data[ptr: ptr + 4], ptr + 4  # If flags exist then return them and advance pointer
    return None, ptr


def get_page_name(stash_data, ptr):
    # Return page name
    next_null = find_next_null(stash_data, ptr)
    return stash_data[ptr: next_null], next_null + 1


def get_data_chunks(data, header):
    # Get data and split into "chunks", each chunk being all the data from one appearance of the header until
    # either the next appearance or EOD
    chunks = []
    chunk_locs = [m.start() for m in re.finditer(header, data)] + [len(data)]
    for idx, loc in enumerate(chunk_locs):
        if idx == len(chunk_locs) - 1:
            continue
        next_loc = chunk_locs[idx + 1]
        chunks.append(data[loc: next_loc])
    return chunks


def chunks_unify_sockets(chunks):
    # For each chunk of data (separated by JM), check the bits to see how many socketed items the item contains
    # If an item contains X filled sockets, then append the next X chunks to it and skip forward
    new_chunks = []
    while chunks:
        item_candidate = chunks.pop(0)
        socketed_items = Item.num_filled_sockets(item_candidate)
        for i in range(socketed_items):
            item_candidate += chunks.pop(0)
        new_chunks.append(item_candidate)
    return new_chunks


def get_items(page_data, ptr):
    # Get list of items, paying attention to socketed items
    item_data = page_data[ptr:]
    # Get all "chunks" separated by "JM", then unify chunks by considering whether an item is actually a part of
    # (socketed in) the previous item
    chunks = get_data_chunks(item_data, b'JM')[1:]
    items = chunks_unify_sockets(chunks)
    return items


def get_pages(stash_data):
    # Return stash page data
    return get_data_chunks(stash_data, b'ST')


def parse_stash_data(stash_data, config):
    # Retrieve the pages we do not wish to sort, and parse the list of items in the remaining pages
    stash_pages = get_pages(stash_data)
    num_pages_to_ignore = int(config["SETTINGS"]["IgnoreFirstXPages"])

    # If there are fewer pages total than those we wish to ignore, do nothing except return all pages.
    # Otherwise divide into pages to ignore and pages to parse
    if num_pages_to_ignore >= len(stash_pages):
        return stash_pages, []
    pages_to_ignore = stash_pages[0:num_pages_to_ignore]
    pages_to_parse = stash_pages[num_pages_to_ignore:]

    # Parse items in remaining pages
    items = []
    for page in pages_to_parse:
        ptr = 2  # Start 2 bytes in
        flags, ptr = get_flags(page, ptr)  # Get page flags and advance pointer
        stash_page_name, ptr = get_page_name(page, ptr)  # Get page name and advance pointer
        page_items = get_items(page, ptr)  # Get items in page
        for item in page_items:
            items.append(Item(data=item))  # Initialize an Item instance for each item

    return pages_to_ignore, items


def to_groups(item_list, config):
    # Sort the items into groups. Each group is sorted internally with some criteria, and different groups will never
    # be on the same stash page.

    # The groups:
    sets = {}  # Note that sets are the exception here as they contain subgroups (the sets) while the other groups don't
    uniques = []
    runewords = []
    runes = []
    jewels = []
    rings_ammies = []
    bases = []
    misc = []
    gems = []
    charms = []
    ubers = []
    essences = []

    # These rules decide which item goes into which group. Note that the ordering here is important. For example, if you
    # want anni/torches to be sorted with the charms, the charm group condition must come before the "unique" condition
    for item in item_list:
        if item.rw:
            runewords.append(item)
        elif item.group == ItemGroup.JEWEL:
            jewels.append(item)
        elif item.group == ItemGroup.RUNE:
            runes.append(item)
        elif item.group in [ItemGroup.UBERKEY, ItemGroup.UBERPART]:
            ubers.append(item)
        elif item.group == ItemGroup.MISC:
            misc.append(item)
        elif item.rarity == Rarity.SET:
            if item.set_id in sets:
                sets[item.set_id].append(item)
            else:
                sets[item.set_id] = [item]
        elif item.group in [ItemGroup.AMULET, ItemGroup.RING]:
            rings_ammies.append(item)
        elif item.group == ItemGroup.ESSENCE:
            essences.append(item)
        elif item.rarity in [Rarity.LOW_QUALITY, Rarity.NORMAL, Rarity.HIGH_QUALITY] and not item.simple:
            bases.append(item)
        elif item.group == ItemGroup.CHARM:
            charms.append(item)
        elif item.group in [ItemGroup.GEM_CHIP, ItemGroup.GEM_FLAWED, ItemGroup.GEM_NORM,
                            ItemGroup.GEM_FLAWLESS, ItemGroup.GEM_PERFECT]:
            gems.append(item)
        elif item.rarity == Rarity.UNIQ:
            uniques.append(item)
        else:  # Catch-all for items which don't fall into one of the other categories and aren't explicitly misc
            misc.append(item)

    # Sort each group internally, according to its own criteria. Uniques are sorted by type (helms, gloves, etc) and
    # then by item code (grim helm, winged helm, etc). Jewels are sorted by rarity. Modify this as you see fit.
    uniques.sort(key=lambda x: (x.group, x.code))
    ubers.sort(key=lambda x: x.code)
    runewords.sort(key=lambda x: (x.group, x.code))
    bases.sort(key=lambda x: (x.group, x.code))
    jewels.sort(key=lambda x: x.rarity)
    rings_ammies.sort(key=lambda x: (x.group, x.rarity))
    runes.sort(key=lambda x: x.code)
    misc.sort(key=lambda x: x.code)
    charms.sort(key=lambda x: (x.code, x.rarity))
    gems.sort(key=lambda x: (x.group, x.code))
    essences.sort(key=lambda x: x.code)
    for item_set in sets:
        sets[item_set].sort(key=lambda x: x.group)

    # Finally, add all sorted groups to the groups list. The ordering here is what will determine the actual order in
    # the stash, so modify to your taste.
    groups = []
    groups.append(gems)
    groups.append(runes)
    groups.append(charms)
    groups.append(jewels)
    groups.append(ubers)
    groups.append(essences)
    groups.append(bases)
    groups.append(runewords)
    groups.append(rings_ammies)
    if config["SETTINGS"]["UnifySets"] == '1':  # For set items, check config. If UnifySets is active then all set items
        # are unified into one supergroup, meaning different sets can appear on the same stash page. Otherwise, treat
        # each set as a different group with its own page.
        sets_supergroup = []
        for item_set in sets:
            sets_supergroup.extend(sets[item_set])
        groups.append(sets_supergroup)
    else:
        for item_set in sets:
            groups.append(sets[item_set])
    groups.append(uniques)
    groups.append(misc)

    # Finally, remove any empty groups to avoid having empty stash pages
    groups = [group for group in groups if group]

    return groups


def to_pages(groups):
    # Take the ordered item groups and put them into virtual stash pages
    pages = []  # List of stash pages
    for group in groups:
        current_page = Page()  # For each group, create a new stash page
        for item in group:  # Then for each item, attempt to insert it somewhere in the page
            if not current_page.insert_item(item):  # If insertion fails, add current page to list of "ready" stash
                # pages, create a new page, and insert item into the new page
                pages.append(current_page)
                current_page = Page()
                current_page.insert_item(item)
        pages.append(current_page)  # When done, add current page to list of "ready" stash
    return pages


def make_stash(path, header, ver, gold, new_pages, ignored_pages):
    # Rewrite the stash file using the new (and ignored) stash pages
    with open(path, "wb") as f:
        # First write header and version
        f.write(header)
        f.write(ver)
        # If the stash is shared ("SSS\0") and ver 2, write the shared gold
        if header == b'SSS\x00' and ver == b'02':
            f.write(gold)
        # If the stash is personal, write 4 junk bytes.
        if header == b'CSTM':
            f.write(b'\x00\x00\x00\x00')

        # Write number of pages. It is possible to write these directly but easier to utilize the existing write_bits
        # method by feeding it some 4-byte string and having it rewrite it, since it already handles the endian issues
        f.write(write_bits(b'\x00\x00\x00\x00', 0, 32, len(ignored_pages) + len(new_pages)))

        # Write each ignored page back into the stash, unmodified from its original form
        for page in ignored_pages:
            f.write(page)

        # For the new pages, first write the header and flags, then the number of items,
        # and then each individual item.
        for page in new_pages:
            if header == b'SSS\x00':  # For shared stashes, turn on the shared stash page flag
                f.write(b'ST\x01\x00\x00\x00\x00JM')
            if header == b'CSTM':  # For personal stashes, keep all flags turned off
                f.write(b'ST\x00\x00\x00\x00\x00JM')
            # IF USING OLDER VERSIONS OF PLUGY, COMMENT OR DELETE THE 4 LINES ABOVE AND UNCOMMENT THE LINE BELOW
            # f.write(b'ST\x00JM')
            f.write(write_bits(b'\x00\x00', 0, 16, page.num_items()))
            for item in page.items:
                f.write(item.data)


def backup_stash(stash_file_path, config):
    # Backup old stash file if indicated in settings
    if config["SETTINGS"]["BackupStashFile"] == '1':
        new_path = stash_file_path.rsplit(".", 1)[0] + "_OLD." + stash_file_path.rsplit(".", 1)[1]
        copy(stash_file_path, new_path)


def main():
    # Read config
    config = configparser.ConfigParser()
    config.read("settings.ini")

    # Get stash file from user
    stash_file_path = filedialog.askopenfilename(title="Select shared stash file",
                                                 filetypes=[("PlugY shared stash file", "*.sss"),
                                                            ("PlugY personal stash file", "*.d2x")])

    # Backup old file
    backup_stash(stash_file_path, config)

    # Read stash file and parse items
    header, ver, gold, num_pages, stash_data = read_stash_file(stash_file_path)
    pages_to_ignore, item_list = parse_stash_data(stash_data, config)

    # Sort items into different groups, and sort each group
    groups = to_groups(item_list, config)

    # Create new stash pages and fill them with the sorted items from the groups
    pages = to_pages(groups)

    # Finally, write all data to a new stash file
    make_stash(stash_file_path, header, ver, gold, pages, pages_to_ignore)


if __name__ == "__main__":
    main()
