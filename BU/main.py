import struct
import re
from enum import IntEnum
from item_data import get_item_size, get_true_set_id, get_item_group, ItemGroup


class Rarity(IntEnum):
    LOW_QUALITY = 1
    NORMAL = 2
    HIGH_QUALITY = 3
    MAGIC = 4
    SET = 5
    RARE = 6
    UNIQ = 7
    CRAFT = 8


def byte_to_bits(byte_value):
    return format(byte_value, '08b')


def bits_to_byte(bits):
    return int(bits, 2).to_bytes(len(bits) // 8, byteorder='big')


def reverse_bits(bits):
    return bits[::-1]


def bit_string_to_int(bit_string):
    out = 0
    for bit in bit_string:
        out = (out << 1) | int(bit)
    return out


def int_to_bit_list(n, min_size):
    bin = [1 if digit == '1' else 0 for digit in bin(n)[2:]]
    if len(bin) < min_size:
        bin = [0]  * (min_size - len(bin)) + bin
    return bin


def int_to_bit_string(n, min_size):
    b = int_to_bit_list(n, min_size)
    return ''.join((str(w) for w in b))


def read_bits(data, offset, size):
    byte_start = int(offset / 8)
    byte_end = int((offset + size)/8)
    bytes_to_read = byte_end - byte_start + 1
    res = []
    for byte_idx in range(bytes_to_read):
        byte = byte_start + byte_idx
        bits_raw = reverse_bits(byte_to_bits(data[byte]))
        bits_to_read = [1 if offset <= byte * 8 + bit_idx < offset + size
                        else 0
                        for bit_idx in range(8)]
        bits = [i for (i, v) in zip(bits_raw, bits_to_read) if v]
        res = res + bits
    return bit_string_to_int(reverse_bits(res))


def write_bits(data, offset, size, value_to_write):
    value_reversed = reverse_bits(int_to_bit_list(value_to_write, size))
    byte_start = int(offset / 8)
    byte_end = int((offset + size - 1)/8)
    bytes_to_read = byte_end - byte_start + 1
    data_new = data[:byte_start]
    for byte_idx in range(bytes_to_read):
        byte = byte_start + byte_idx
        bits_raw = reverse_bits(byte_to_bits(data[byte]))
        bits_new = ''
        for bit_idx, bit in enumerate(bits_raw):
            if offset <= byte * 8 + bit_idx < offset + size:
                bits_new += str(value_reversed.pop(0))
            else:
                bits_new += bits_raw[bit_idx]
        data_new += bits_to_byte(reverse_bits(bits_new))
    data_new += data[byte_end + 1:]
    return data_new


def find_next_null(data, start):
    cur = start
    while cur < len(data) and data[cur] != 0:
        cur += 1
    return cur


def read_file():
    with open("_LOD_SharedStashSave.sss", "rb") as f:
        header = f.read(4)
        ver = f.read(2)
        gold = None
        if ver == b'02':
            gold = f.read(4)
            # gold = struct.unpack('I', f.read(4))[0]
        num_pages = struct.unpack('I', f.read(4))[0]
        stash_data = f.read(-1)
    return header, ver, gold, num_pages, stash_data


def get_flags(stash_data, ptr):
    next_null = find_next_null(stash_data, ptr)
    if stash_data[next_null + 1: next_null + 3] != b'JM':
        return stash_data[ptr: ptr + 4], ptr + 4
    return None, ptr


def get_page_name(stash_data, ptr):
    next_null = find_next_null(stash_data, ptr)
    return stash_data[ptr: next_null], next_null + 1


def get_data_chunks(data, header):
    chunks = []
    chunk_locs = [m.start() for m in re.finditer(header, data)] + [len(data)]
    for idx, loc in enumerate(chunk_locs):
        if idx == len(chunk_locs) - 1:
            continue
        next_loc = chunk_locs[idx + 1]
        chunks.append(data[loc: next_loc])
    return chunks


def chunks_unify_sockets(chunks):
    new_chunks = []
    print(len(chunks))
    while chunks:
        item_candidate = chunks.pop(0)
        if not is_ear(item_candidate):
            socketed_items = read_bits(item_candidate, 108, 3)
            for i in range(socketed_items):
                item_candidate += chunks.pop(0)
        new_chunks.append(item_candidate)
    return new_chunks


def get_items(page_data, ptr):
    item_data = page_data[ptr:]

    chunks = get_data_chunks(item_data, b'JM')[1:]
    items = chunks_unify_sockets(chunks)
    return items


def get_pages(stash_data):
    return get_data_chunks(stash_data, b'ST')


def get_position(item):
    x_pos = read_bits(item, 65, 4)
    y_pos = read_bits(item, 69, 4)
    return x_pos, y_pos


def get_item_code(item):
    if is_ear(item):
        return 'ear'
    item_code = ''
    for i in range(4):
        char = chr(read_bits(item, 76 + i * 8, 8))
        if char != ' ':
            item_code += char
    return item_code


def is_ear(item):
    return read_bits(item, 32, 1)


def is_runeword(item):
    return read_bits(item, 42, 1)


def is_simple(item):
    return read_bits(item, 37, 1)


def get_rarity(item):
    return Rarity(read_bits(item, 150, 4))


def has_multiple_pictures(item):
    return read_bits(item, 154, 1)


def is_class_specific(item):
    if has_multiple_pictures(item):
        return read_bits(item, 158, 1)
    return read_bits(item, 155, 1)


def get_set_id(item):
    offset = 156
    if has_multiple_pictures(item):
        offset += 3
    if is_class_specific(item):
        offset += 11
    return read_bits(item, offset, 12)


class Item:
    def __init__(self, item_data, item_code, is_rw, x_size, y_size, item_type, item_rarity=None, item_set_id=None):
        self.data = item_data
        self.code = item_code
        self.type = item_type
        self.is_rw = is_rw
        self.is_simple = is_simple(self.data)
        self.rarity = item_rarity
        self.set_id = item_set_id
        self.x_size = x_size
        self.y_size = y_size

    def set_position(self, x, y):
        self.data = write_bits(self.data, 65, 4, x)
        self.data = write_bits(self.data, 69, 4, y)


def parse_stash_data(stash_data):
    stash_pages = get_pages(stash_data)
    items = []
    idx = 0
    for page in stash_pages:
        # stash_header = page[0:2]
        ptr = 2
        flags, ptr = get_flags(page, ptr)
        stash_page_name, ptr = get_page_name(page, ptr)
        idx += 1
        print("PAGE NO." + str(idx))
        page_items = get_items(page, ptr)
        for item in page_items:
            item_code = get_item_code(item)
            item_is_rw = is_runeword(item)
            item_type = get_item_group(item_code)
            x_size, y_size = get_item_size(item_code)
            rarity = None
            true_set_id = None
            if not is_simple(item):
                rarity = get_rarity(item)
                if rarity == Rarity.SET:
                    true_set_id = get_true_set_id(get_set_id(item))

            items.append(Item(item_data=item,
                              is_rw=item_is_rw,
                              item_code=item_code,
                              x_size=x_size,
                              y_size=y_size,
                              item_type=item_type,
                              item_rarity=rarity,
                              item_set_id=true_set_id))
    return items


def to_groups(item_list):
    uniques = []
    sets = {}
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

    for item in item_list:
        if item.is_rw:
            runewords.append(item)
        elif item.type == ItemGroup.JEWEL:
            jewels.append(item)
        elif item.type == ItemGroup.RUNE:
            runes.append(item)
        elif item.type in [ItemGroup.UBERKEY, ItemGroup.UBERPART]:
            ubers.append(item)
        elif item.rarity == Rarity.SET:
            if item.set_id in sets:
                sets[item.set_id].append(item)
            else:
                sets[item.set_id] = [item]
        elif item.type in [ItemGroup.AMULET, ItemGroup.RING]:
            rings_ammies.append(item)
        elif item.type == ItemGroup.ESSENCE:
            essences.append(item)
        elif item.rarity in (Rarity.LOW_QUALITY, Rarity.NORMAL, Rarity.HIGH_QUALITY) and not item.is_simple:
            bases.append(item)
        elif item.type == ItemGroup.CHARM:
            charms.append(item)
        elif item.type in [ItemGroup.GEM_CHIP, ItemGroup.GEM_FLAWED, ItemGroup.GEM_NORM,
                           ItemGroup.GEM_FLAWLESS, ItemGroup.GEM_PERFECT]:
            gems.append(item)
        elif item.rarity == Rarity.UNIQ:
            uniques.append(item)
        else:
            misc.append(item)

    uniques.sort(key=lambda x: (x.type, x.code))
    ubers.sort(key=lambda x: x.code)
    runewords.sort(key=lambda x: (x.type, x.code))
    bases.sort(key=lambda x: (x.type, x.code))
    jewels.sort(key=lambda x: x.rarity)
    rings_ammies.sort(key=lambda x: (x.type, x.rarity))
    runes.sort(key=lambda x: x.code)
    misc.sort(key=lambda x: x.code)
    charms.sort(key=lambda x: (x.code, x.rarity))
    gems.sort(key=lambda x: (x.type, x.code))
    essences.sort(key=lambda x: x.code)
    for item_set in sets:
        sets[item_set].sort(key=lambda x: x.type)

    groups = []

    groups.append(gems)
    groups.append(runes)
    groups.append(charms)
    groups.append(jewels)
    groups.append(essences)
    groups.append(bases)
    groups.append(runewords)
    groups.append(rings_ammies)
    for item_set in sets:
        groups.append(sets[item_set])
    groups.append(uniques)
    groups.append(misc)

    return groups


class Page:
    def __init__(self):
        self.spaces = [[0] * 10 for _ in range(10)]
        self.items = []

    def is_collision(self, x_position, x_size, y_position, y_size):
        for x in range(x_size):
            for y in range(y_size):
                if x_position + x > 9 or y_position + y > 9 or\
                        self.spaces[x_position + x][y_position + y] > 0:
                    return True
        return False

    def allocate(self, x_position, x_size, y_position, y_size):
        for x in range(x_size):
            for y in range(y_size):
                self.spaces[x_position + x][y_position + y] += 1

    def insert_item(self, item):
        allocated = False
        for x in range(10):
            for y in range(10):
                if not allocated and not self.is_collision(x, item.x_size, y, item.y_size):
                    item.set_position(x, y)
                    self.items.append(item)
                    self.allocate(x, item.x_size, y, item.y_size)
                    allocated = True
        return allocated

    def num_items(self):
        return len(self.items)


def to_pages(groups):
    pages = []
    for group in groups:
        current_page = Page()
        for item in group:
            if not current_page.insert_item(item):
                pages.append(current_page)
                current_page = Page()
                current_page.insert_item(item)
        pages.append(current_page)
    return pages


def make_stash(header, ver, gold, new_pages):
    with open("_LOD_SharedStashSave_NEW.sss", "wb+") as f:
        f.write(header)
        f.write(ver)
        if ver == b'02':
            f.write(gold)
        f.write(write_bits(b'\x00\x00\x00\x00', 0, 32, len(new_pages)))
        for page in new_pages:
            f.write(b'ST\x01\x00\x00\x00\x00JM')
            f.write(write_bits(b'\x00\x00', 0, 16, page.num_items()))
            for item in page.items:
                f.write(item.data)


def main():
    # TO ADD
    # option to keep sets on different pages
    # different orderings
    # "ignore pages"
    # refactor code
    # move all item methods to item class
    # page methods to page class?
    header, ver, gold, num_pages, stash_data = read_file()
    print(header)
    print(ver)
    item_list = parse_stash_data(stash_data)
    print(len(item_list))
    for item in item_list:
        print(item.code)
        print(item.rarity)
        print(get_position(item.data))
        print(item.x_size)
        print(item.y_size)
    groups = to_groups(item_list)

    num_items_total = 0
    for group in groups:
        num_items_total += len(group)
    print(num_items_total)

    pages = to_pages(groups)

    make_stash(header, ver, gold, pages)


if __name__ == "__main__":
    main()
