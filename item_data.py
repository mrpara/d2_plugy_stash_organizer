# ITEM DATA FILE
from typing import Dict
from enum import IntEnum


# ITEM RARITIES
class Rarity(IntEnum):
    LOW_QUALITY = 1
    NORMAL = 2
    HIGH_QUALITY = 3
    MAGIC = 4
    SET = 5
    RARE = 6
    UNIQ = 7
    CRAFT = 8


# ITEM GROUPS (ARCHETYPES)
class ItemGroup(IntEnum):
    HELM = 1
    BODY = 2
    SHIELD = 3
    GLOVES = 4
    BOOTS = 5
    BELT = 6
    PELT = 7
    BARB = 8
    PAL = 9
    NEC = 10
    AXE = 11
    MACE = 12
    SWORD = 13
    DAGGER = 14
    THROW = 15
    JAV = 16
    SPEAR = 17
    POLEARM = 18
    BOW = 19
    XBOW = 20
    STAFF = 21
    WAND = 22
    SCEPTER = 23
    ASN = 24
    SORC = 25
    AMA = 26
    CIRCLET = 27
    THROWPOT = 28
    QUEST = 29
    RUNE = 31
    POTION = 32
    CHARM = 33
    SCROLL = 34
    MISC = 35
    JEWEL = 36
    AMULET = 37
    RING = 38
    UBERKEY = 39
    UBERPART = 40
    ESSENCE = 41
    GEM_AMETHYST = 42
    GEM_DIAMOND = 43
    GEM_EMERALD = 44
    GEM_RUBY = 45
    GEM_SAPPHIRE = 46
    GEM_TOPAZ = 47
    GEM_SKULL = 48


class ItemTypeData:
    # Class for storing size and type of items
    def __init__(self, x_size, y_size, item_group):
        self.x_size = x_size
        self.y_size = y_size
        self.item_group = item_group


def get_item_size_x(item_code):
    return item_data[item_code].x_size


def get_item_size_y(item_code):
    return item_data[item_code].y_size


def get_item_size(item_code):
    return get_item_size_x(item_code), get_item_size_y(item_code)


def get_item_group(item_code):
    return item_data[item_code].item_group


# ITEM SIZE DATA
item_data: Dict[str, ItemTypeData] = {}
# HELM
item_data['cap'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Cap
item_data['skp'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Skull Cap
item_data['hlm'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Helm
item_data['fhl'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Full Helm
item_data['ghm'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Great Helm
item_data['crn'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Crown
item_data['msk'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Mask
item_data['bhm'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Bone Helm
item_data['xap'] = ItemTypeData(2, 2, ItemGroup.HELM)   # War Hat
item_data['xkp'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Sallet
item_data['xlm'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Casque
item_data['xhl'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Basinet
item_data['xhm'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Winged Helm
item_data['xrn'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Grand Crown
item_data['xsk'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Death Mask
item_data['xh9'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Grim Helm
item_data['uap'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Shako
item_data['ukp'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Hydraskull
item_data['ulm'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Armet
item_data['uhl'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Giant Conch
item_data['uhm'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Spired Helm
item_data['urn'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Corona
item_data['usk'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Demonhead
item_data['uh9'] = ItemTypeData(2, 2, ItemGroup.HELM)   # Bone Visage
# BODY
item_data['qui'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Quilted Armor
item_data['lea'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Leather Armor
item_data['hla'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Hard Leather
item_data['stu'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Studded Leather
item_data['rng'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Ring Mail
item_data['scl'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Scale Mail
item_data['chn'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Chain Mail
item_data['brs'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Breast Plate
item_data['spl'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Splint Mail
item_data['plt'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Plate Mail
item_data['fld'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Field Plate
item_data['gth'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Gothic Plate
item_data['ful'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Full Plate Mail
item_data['aar'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Ancient Armor
item_data['ltp'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Light Plate
item_data['xui'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Ghost Armor
item_data['xea'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Serpentskin
item_data['xla'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Demonhide Armor
item_data['xtu'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Trellised Armor
item_data['xng'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Linked Mail
item_data['xcl'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Tigulated Mail
item_data['xhn'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Mesh Armor
item_data['xrs'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Cuirass
item_data['xpl'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Russet Armor
item_data['xlt'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Templar Coat
item_data['xld'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Sharktooth
item_data['xth'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Embossed Plate
item_data['xul'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Chaos Armor
item_data['xar'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Ornate Armor
item_data['xtp'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Mage Plate
item_data['uui'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Dusk Shroud
item_data['uea'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Wyrmhide
item_data['ula'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Scarab Husk
item_data['utu'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Wire Fleece
item_data['ung'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Diamond Mail
item_data['ucl'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Loricated Mail
item_data['uhn'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Boneweave
item_data['urs'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Great Hauberk
item_data['upl'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Balrog Skin
item_data['ult'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Hellforge Plate
item_data['uld'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Kraken Shell
item_data['uth'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Lacquered Plate
item_data['uul'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Shadow Plate
item_data['uar'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Sacred Armor
item_data['utp'] = ItemTypeData(2, 3, ItemGroup.BODY)   # Archon Plate
# SHIELD
item_data['buc'] = ItemTypeData(2, 2, ItemGroup.SHIELD)   # Buckler
item_data['sml'] = ItemTypeData(2, 2, ItemGroup.SHIELD)   # Small Shield
item_data['lrg'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Large Shield
item_data['kit'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Kite Shield
item_data['tow'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Tower Shield
item_data['gts'] = ItemTypeData(2, 4, ItemGroup.SHIELD)   # Gothic Shield
item_data['bsh'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Bone Shield
item_data['spk'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Spiked Shield
item_data['xuc'] = ItemTypeData(2, 2, ItemGroup.SHIELD)   # Defender
item_data['xml'] = ItemTypeData(2, 2, ItemGroup.SHIELD)   # Round Shield
item_data['xrg'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Scutum
item_data['xit'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Dragon Shield
item_data['xow'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Pavise
item_data['xts'] = ItemTypeData(2, 4, ItemGroup.SHIELD)   # Ancient Shield
item_data['xsh'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Grim Shield
item_data['xpk'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Barbed Shield
item_data['uuc'] = ItemTypeData(2, 2, ItemGroup.SHIELD)   # Heater
item_data['uml'] = ItemTypeData(2, 2, ItemGroup.SHIELD)   # Luna
item_data['urg'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Hyperion
item_data['uit'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Monarch
item_data['uow'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Aegis
item_data['uts'] = ItemTypeData(2, 4, ItemGroup.SHIELD)   # Ward
item_data['ush'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Troll Nest
item_data['upk'] = ItemTypeData(2, 3, ItemGroup.SHIELD)   # Blade Barrier
# GLOVES
item_data['lgl'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Leather Gloves
item_data['vgl'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Heavy Gloves
item_data['mgl'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Chain Gloves
item_data['tgl'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Light Gauntlets
item_data['hgl'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Gauntlets
item_data['xlg'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Demonhide Glove
item_data['xvg'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Sharkskin Glove
item_data['xmg'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Heavy Bracers
item_data['xtg'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Battle Gauntlet
item_data['xhg'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # War Gauntlets
item_data['ulg'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Bramble Mitts
item_data['uvg'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Vampirebone Gl
item_data['umg'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Vambraces
item_data['utg'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Crusader Gaunt
item_data['uhg'] = ItemTypeData(2, 2, ItemGroup.GLOVES)   # Ogre Gauntlets
# BOOTS
item_data['lbt'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Boots
item_data['vbt'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Heavy Boots
item_data['mbt'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Chain Boots
item_data['tbt'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Light Plate
item_data['hbt'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Greaves
item_data['xlb'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Demonhide Boots
item_data['xvb'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Sharkskin Boots
item_data['xmb'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Mesh Boots
item_data['xtb'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Battle Boots
item_data['xhb'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # War Boots
item_data['ulb'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Wyrmhide Boots
item_data['uvb'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Scarabshell Bts
item_data['umb'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Boneweave Boots
item_data['utb'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Mirrored Boots
item_data['uhb'] = ItemTypeData(2, 2, ItemGroup.BOOTS)   # Myrmidon Greave
# BELT
item_data['lbl'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Sash
item_data['vbl'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Light Belt
item_data['mbl'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Belt
item_data['tbl'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Heavy Belt
item_data['hbl'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Plated Belt
item_data['zlb'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Demonhide Sash
item_data['zvb'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Sharkskin Belt
item_data['zmb'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Mesh Belt
item_data['ztb'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Battle Belt
item_data['zhb'] = ItemTypeData(2, 1, ItemGroup.BELT)   # War Belt
item_data['ulc'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Spiderweb Sash
item_data['uvc'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Vampirefang Blt
item_data['umc'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Mithril Coil
item_data['utc'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Troll Belt
item_data['uhc'] = ItemTypeData(2, 1, ItemGroup.BELT)   # Colossus Girdle
# PELT
item_data['dr1'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Wolf Head
item_data['dr2'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Hawk Helm
item_data['dr3'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Antlers
item_data['dr4'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Falcon Mask
item_data['dr5'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Spirit Mask
item_data['dr6'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Alpha Helm
item_data['dr7'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Griffon Headress
item_data['dr8'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Hunter’s Guise
item_data['dr9'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Sacred Feathers
item_data['dra'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Totemic Mask
item_data['drb'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Blood Spirit
item_data['drc'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Sun Spirit
item_data['drd'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Earth Spirit
item_data['dre'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Sky Spirit
item_data['drf'] = ItemTypeData(2, 2, ItemGroup.PELT)   # Dream Spirit
# BARB
item_data['ba1'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Jawbone Cap
item_data['ba2'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Fanged Helm
item_data['ba3'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Horned Helm
item_data['ba4'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Assualt Helmet
item_data['ba5'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Avenger Guard
item_data['ba6'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Jawbone Visor
item_data['ba7'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Lion Helm
item_data['ba8'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Rage Mask
item_data['ba9'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Savage Helmet
item_data['baa'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Slayer Guard
item_data['bab'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Carnage Helm
item_data['bac'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Fury Visor
item_data['bad'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Destroyer Helm
item_data['bae'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Conqueror Crown
item_data['baf'] = ItemTypeData(2, 2, ItemGroup.BARB)   # Guardian Crown
# PAL
item_data['pa1'] = ItemTypeData(2, 2, ItemGroup.PAL)   # Targe
item_data['pa2'] = ItemTypeData(2, 2, ItemGroup.PAL)   # Rondache
item_data['pa3'] = ItemTypeData(2, 4, ItemGroup.PAL)   # Heraldic Shield
item_data['pa4'] = ItemTypeData(2, 4, ItemGroup.PAL)   # Aerin Shield
item_data['pa5'] = ItemTypeData(2, 2, ItemGroup.PAL)   # Crown Shield
item_data['pa6'] = ItemTypeData(2, 2, ItemGroup.PAL)   # Akaran Targe
item_data['pa7'] = ItemTypeData(2, 2, ItemGroup.PAL)   # Akaran Rondache
item_data['pa8'] = ItemTypeData(2, 4, ItemGroup.PAL)   # Protector Shld
item_data['pa9'] = ItemTypeData(2, 4, ItemGroup.PAL)   # Guilded Shield
item_data['paa'] = ItemTypeData(2, 2, ItemGroup.PAL)   # Royal Shield
item_data['pab'] = ItemTypeData(2, 2, ItemGroup.PAL)   # Sacred Targe
item_data['pac'] = ItemTypeData(2, 2, ItemGroup.PAL)   # Sacred Rondache
item_data['pad'] = ItemTypeData(2, 4, ItemGroup.PAL)   # Kurast Shield
item_data['pae'] = ItemTypeData(2, 4, ItemGroup.PAL)   # Zakarum Shield
item_data['paf'] = ItemTypeData(2, 2, ItemGroup.PAL)   # Vortex Shield
# NEC
item_data['ne1'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Preserved Head
item_data['ne2'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Zombie Head
item_data['ne3'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Unraveller Head
item_data['ne4'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Gargoyle Head
item_data['ne5'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Demon Head
item_data['ne6'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Mummified Trphy
item_data['ne7'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Fetish Trophy
item_data['ne8'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Sexton Trophy
item_data['ne9'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Cantor Trophy
item_data['nea'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Heirophant Trphy
item_data['neb'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Minion Skull
item_data['nec'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Hellspawn Skull
item_data['ned'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Overseer Skull
item_data['nee'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Succubae Skull
item_data['nef'] = ItemTypeData(2, 2, ItemGroup.NEC)   # Bloodlord Skull
# AXE
item_data['hax'] = ItemTypeData(1, 3, ItemGroup.AXE)   # Hand Axe
item_data['axe'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Axe
item_data['2ax'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Double Axe
item_data['mpi'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Military Pick
item_data['wax'] = ItemTypeData(2, 3, ItemGroup.AXE)   # War Axe
item_data['lax'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Large Axe
item_data['bax'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Broad Axe
item_data['btx'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Battle Axe
item_data['gax'] = ItemTypeData(2, 4, ItemGroup.AXE)   # Great Axe
item_data['gix'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Giant Axe
item_data['9ha'] = ItemTypeData(1, 3, ItemGroup.AXE)   # Hatchet
item_data['9ax'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Cleaver
item_data['92a'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Twin Axe
item_data['9mp'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Crowbill
item_data['9wa'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Naga
item_data['9la'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Military Axe
item_data['9ba'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Bearded Axe
item_data['9bt'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Tabar
item_data['9ga'] = ItemTypeData(2, 4, ItemGroup.AXE)   # Gothic Axe
item_data['9gi'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Ancient Axe
item_data['7ha'] = ItemTypeData(1, 3, ItemGroup.AXE)   # Tomahawk
item_data['7ax'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Small Crescent
item_data['72a'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Ettin Axe
item_data['7mp'] = ItemTypeData(2, 3, ItemGroup.AXE)   # War Spike
item_data['7wa'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Berserker Axe
item_data['7la'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Feral Axe
item_data['7ba'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Silver Edged Ax
item_data['7bt'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Decapitator
item_data['7ga'] = ItemTypeData(2, 4, ItemGroup.AXE)   # Champion Axe
item_data['7gi'] = ItemTypeData(2, 3, ItemGroup.AXE)   # Glorious Axe
# MACE
item_data['clb'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Club
item_data['spc'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Spiked Club
item_data['mac'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Mace
item_data['mst'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Morning Star
item_data['fla'] = ItemTypeData(2, 3, ItemGroup.MACE)   # Flail
item_data['whm'] = ItemTypeData(2, 3, ItemGroup.MACE)   # War Hammer
item_data['mau'] = ItemTypeData(2, 4, ItemGroup.MACE)   # Maul
item_data['gma'] = ItemTypeData(2, 3, ItemGroup.MACE)   # Great Maul
item_data['9cl'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Cudgel
item_data['9sp'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Barbed Club
item_data['9ma'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Flanged Mace
item_data['9mt'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Jagged Star
item_data['9fl'] = ItemTypeData(2, 3, ItemGroup.MACE)   # Knout
item_data['9wh'] = ItemTypeData(2, 3, ItemGroup.MACE)   # Battle Hammer
item_data['9m9'] = ItemTypeData(2, 4, ItemGroup.MACE)   # War Club
item_data['9gm'] = ItemTypeData(2, 3, ItemGroup.MACE)   # Martel de Fer
item_data['7cl'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Truncheon
item_data['7sp'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Tyrant Club
item_data['7ma'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Reinforced Mace
item_data['7mt'] = ItemTypeData(1, 3, ItemGroup.MACE)   # Devil Star
item_data['7fl'] = ItemTypeData(2, 3, ItemGroup.MACE)   # Scourge
item_data['7wh'] = ItemTypeData(2, 3, ItemGroup.MACE)   # Legendary Mallet
item_data['7m7'] = ItemTypeData(2, 4, ItemGroup.MACE)   # Ogre Maul
item_data['7gm'] = ItemTypeData(2, 3, ItemGroup.MACE)   # Thunder Maul
# SWORD
item_data['ssd'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Short Sword
item_data['scm'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Scimitar
item_data['sbr'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Saber
item_data['flc'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Falchion
item_data['crs'] = ItemTypeData(2, 3, ItemGroup.SWORD)   # Crystal Sword
item_data['bsd'] = ItemTypeData(2, 3, ItemGroup.SWORD)   # Broad Sword
item_data['lsd'] = ItemTypeData(2, 3, ItemGroup.SWORD)   # Long Sword
item_data['wsd'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # War Sword
item_data['2hs'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Two-handed Swrd
item_data['clm'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Claymore
item_data['gis'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Giant Sword
item_data['bsw'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Bastard Sword
item_data['flb'] = ItemTypeData(2, 4, ItemGroup.SWORD)   # Flamberge
item_data['gsd'] = ItemTypeData(2, 4, ItemGroup.SWORD)   # Great Sword
item_data['9ss'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Gladius
item_data['9sm'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Cutlass
item_data['9sb'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Shamshir
item_data['9fc'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Tulwar
item_data['9cr'] = ItemTypeData(2, 3, ItemGroup.SWORD)   # Dimensional Bld
item_data['9bs'] = ItemTypeData(2, 3, ItemGroup.SWORD)   # Battle Sword
item_data['9ls'] = ItemTypeData(2, 3, ItemGroup.SWORD)   # Rune Sword
item_data['9wd'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Ancient Sword
item_data['92h'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Espadon
item_data['9cm'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Dacian Falx
item_data['9gs'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Tusk Sword
item_data['9b9'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Gothic Sword
item_data['9fb'] = ItemTypeData(2, 4, ItemGroup.SWORD)   # Zweihander
item_data['9gd'] = ItemTypeData(2, 4, ItemGroup.SWORD)   # Executioner Swr
item_data['7ss'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Falcata
item_data['7sm'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Ataghan
item_data['7sb'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Elegant Blade
item_data['7fc'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Hydra Edge
item_data['7cr'] = ItemTypeData(2, 3, ItemGroup.SWORD)   # Phase Blade
item_data['7bs'] = ItemTypeData(2, 3, ItemGroup.SWORD)   # Conquest Sword
item_data['7ls'] = ItemTypeData(2, 3, ItemGroup.SWORD)   # Cryptic Sword
item_data['7wd'] = ItemTypeData(1, 3, ItemGroup.SWORD)   # Mythical Sword
item_data['72h'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Legend Sword
item_data['7cm'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Highland Blade
item_data['7gs'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Balrog Blade
item_data['7b7'] = ItemTypeData(1, 4, ItemGroup.SWORD)   # Champion Sword
item_data['7fb'] = ItemTypeData(2, 4, ItemGroup.SWORD)   # Colossal Sword
item_data['7gd'] = ItemTypeData(2, 4, ItemGroup.SWORD)   # Colossus Blade
# DAGGER
item_data['dgr'] = ItemTypeData(1, 2, ItemGroup.DAGGER)   # Dagger
item_data['dir'] = ItemTypeData(1, 2, ItemGroup.DAGGER)   # Dirk
item_data['kri'] = ItemTypeData(1, 3, ItemGroup.DAGGER)   # Kriss
item_data['bld'] = ItemTypeData(1, 3, ItemGroup.DAGGER)   # Blade
item_data['9dg'] = ItemTypeData(1, 2, ItemGroup.DAGGER)   # Poignard
item_data['9di'] = ItemTypeData(1, 2, ItemGroup.DAGGER)   # Rondel
item_data['9kr'] = ItemTypeData(1, 3, ItemGroup.DAGGER)   # Cinquedeas
item_data['9bl'] = ItemTypeData(1, 3, ItemGroup.DAGGER)   # Stilleto
item_data['7dg'] = ItemTypeData(1, 2, ItemGroup.DAGGER)   # Bone Knife
item_data['7di'] = ItemTypeData(1, 2, ItemGroup.DAGGER)   # Mithral Point
item_data['7kr'] = ItemTypeData(1, 3, ItemGroup.DAGGER)   # Fanged Knife
item_data['7bl'] = ItemTypeData(1, 3, ItemGroup.DAGGER)   # Legend Spike
# THROW
item_data['tkf'] = ItemTypeData(1, 2, ItemGroup.THROW)   # Throwing Knife
item_data['tax'] = ItemTypeData(1, 2, ItemGroup.THROW)   # Throwing Axe
item_data['bkf'] = ItemTypeData(1, 2, ItemGroup.THROW)   # Balanced Knife
item_data['bal'] = ItemTypeData(2, 3, ItemGroup.THROW)   # Balanced Axe
item_data['9tk'] = ItemTypeData(1, 2, ItemGroup.THROW)   # Battle Dart
item_data['9ta'] = ItemTypeData(1, 2, ItemGroup.THROW)   # Francisca
item_data['9bk'] = ItemTypeData(1, 2, ItemGroup.THROW)   # War Dart
item_data['9b8'] = ItemTypeData(2, 3, ItemGroup.THROW)   # Hurlbat
item_data['7tk'] = ItemTypeData(1, 2, ItemGroup.THROW)   # Flying Knife
item_data['7ta'] = ItemTypeData(1, 2, ItemGroup.THROW)   # Flying Axe
item_data['7bk'] = ItemTypeData(1, 2, ItemGroup.THROW)   # Winged Knife
item_data['7b8'] = ItemTypeData(2, 3, ItemGroup.THROW)   # Winged Axe
# JAV
item_data['jav'] = ItemTypeData(1, 3, ItemGroup.JAV)   # Javelin
item_data['pil'] = ItemTypeData(1, 3, ItemGroup.JAV)   # Pilum
item_data['ssp'] = ItemTypeData(1, 3, ItemGroup.JAV)   # Short Spear
item_data['glv'] = ItemTypeData(1, 4, ItemGroup.JAV)   # Glaive
item_data['tsp'] = ItemTypeData(1, 4, ItemGroup.JAV)   # Throwing Spear
item_data['9ja'] = ItemTypeData(1, 3, ItemGroup.JAV)   # War Javelin
item_data['9pi'] = ItemTypeData(1, 3, ItemGroup.JAV)   # Great Pilum
item_data['9s9'] = ItemTypeData(1, 3, ItemGroup.JAV)   # Simbilan
item_data['9gl'] = ItemTypeData(1, 4, ItemGroup.JAV)   # Spiculum
item_data['9ts'] = ItemTypeData(1, 4, ItemGroup.JAV)   # Harpoon
item_data['7ja'] = ItemTypeData(1, 3, ItemGroup.JAV)   # Hyperion Javeln
item_data['7pi'] = ItemTypeData(1, 3, ItemGroup.JAV)   # Stygian Pilum
item_data['7s7'] = ItemTypeData(1, 3, ItemGroup.JAV)   # Balrog Spear
item_data['7gl'] = ItemTypeData(1, 4, ItemGroup.JAV)   # Ghost Glaive
item_data['7ts'] = ItemTypeData(1, 4, ItemGroup.JAV)   # Winged Harpoon
# SPEAR
item_data['spr'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Spear
item_data['tri'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Trident
item_data['brn'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Brandistock
item_data['spt'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Spetum
item_data['pik'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Pike
item_data['9sr'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # War Spear
item_data['9tr'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Fuscina
item_data['9br'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # War Fork
item_data['9st'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Yari
item_data['9p9'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Lance
item_data['7sr'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Hyperion Spear
item_data['7tr'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Stygian Pike
item_data['7br'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Mancatcher
item_data['7st'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # Ghost Spear
item_data['7p7'] = ItemTypeData(2, 4, ItemGroup.SPEAR)   # War Pike
# POLEARM
item_data['bar'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Bardiche
item_data['vou'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Voulge
item_data['scy'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Scythe
item_data['pax'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Poleaxe
item_data['hal'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Halberd
item_data['wsc'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # War Scythe
item_data['9b7'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Lochaber Axe
item_data['9vo'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Bill
item_data['9s8'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Battle Scythe
item_data['9pa'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Partizan
item_data['9h9'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Bec-de-Corbin
item_data['9wc'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Grim Scythe
item_data['7o7'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Ogre Axe
item_data['7vo'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Colossus Voulge
item_data['7s8'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Thresher
item_data['7pa'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Cryptic Axe
item_data['7h7'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Great Poleaxe
item_data['7wc'] = ItemTypeData(2, 4, ItemGroup.POLEARM)   # Giant Thresher
# BOW
item_data['sbw'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Short Bow
item_data['hbw'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Hunter’s Bow
item_data['lbw'] = ItemTypeData(2, 4, ItemGroup.BOW)   # Long Bow
item_data['cbw'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Composite Bow
item_data['sbb'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Shrt Battle Bow
item_data['lbb'] = ItemTypeData(2, 4, ItemGroup.BOW)   # Long Battle Bow
item_data['swb'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Short War Bow
item_data['lwb'] = ItemTypeData(2, 4, ItemGroup.BOW)   # Long War Bow
item_data['8sb'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Edge Bow
item_data['8hb'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Razor Bow
item_data['8lb'] = ItemTypeData(2, 4, ItemGroup.BOW)   # Cedar Bow
item_data['8cb'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Double Bow
item_data['8s8'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Short Siege Bow
item_data['8l8'] = ItemTypeData(2, 4, ItemGroup.BOW)   # Long Siege Bow
item_data['8sw'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Rune Bow
item_data['8lw'] = ItemTypeData(2, 4, ItemGroup.BOW)   # Gothic Bow
item_data['6sb'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Spider Bow
item_data['6hb'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Blade Bow
item_data['6lb'] = ItemTypeData(2, 4, ItemGroup.BOW)   # Shadow Bow
item_data['6cb'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Great Bow
item_data['6s7'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Diamond Bow
item_data['6l7'] = ItemTypeData(2, 4, ItemGroup.BOW)   # Crusader Bow
item_data['6sw'] = ItemTypeData(2, 3, ItemGroup.BOW)   # Ward Bow
item_data['6lw'] = ItemTypeData(2, 4, ItemGroup.BOW)   # Hydra Bow
# XBOW
item_data['lxb'] = ItemTypeData(2, 3, ItemGroup.XBOW)   # Light Crossbow
item_data['mxb'] = ItemTypeData(2, 3, ItemGroup.XBOW)   # Crossbow
item_data['hxb'] = ItemTypeData(2, 4, ItemGroup.XBOW)   # Heavy Crossbow
item_data['rxb'] = ItemTypeData(2, 3, ItemGroup.XBOW)   # Repeating X-bow
item_data['8lx'] = ItemTypeData(2, 3, ItemGroup.XBOW)   # Arbalest
item_data['8mx'] = ItemTypeData(2, 3, ItemGroup.XBOW)   # Siege Crossbow
item_data['8hx'] = ItemTypeData(2, 4, ItemGroup.XBOW)   # Ballista
item_data['8rx'] = ItemTypeData(2, 3, ItemGroup.XBOW)   # Chu-Ko-Nu
item_data['6lx'] = ItemTypeData(2, 3, ItemGroup.XBOW)   # Pellet Bow
item_data['6mx'] = ItemTypeData(2, 3, ItemGroup.XBOW)   # Gorgon Crossbow
item_data['6hx'] = ItemTypeData(2, 4, ItemGroup.XBOW)   # Colossus x-bow
item_data['6rx'] = ItemTypeData(2, 3, ItemGroup.XBOW)   # Demon Crossbow
# STAFF
item_data['sst'] = ItemTypeData(1, 3, ItemGroup.STAFF)   # Short Staff
item_data['lst'] = ItemTypeData(1, 4, ItemGroup.STAFF)   # Long Staff
item_data['cst'] = ItemTypeData(1, 4, ItemGroup.STAFF)   # Gnarled Staff
item_data['bst'] = ItemTypeData(1, 4, ItemGroup.STAFF)   # Battle Staff
item_data['wst'] = ItemTypeData(2, 4, ItemGroup.STAFF)   # War Staff
item_data['8ss'] = ItemTypeData(1, 3, ItemGroup.STAFF)   # Jo Staff
item_data['8ls'] = ItemTypeData(1, 4, ItemGroup.STAFF)   # Quarterstaff
item_data['8cs'] = ItemTypeData(1, 4, ItemGroup.STAFF)   # Cedar Staff
item_data['8bs'] = ItemTypeData(1, 4, ItemGroup.STAFF)   # Gothic Staff
item_data['8ws'] = ItemTypeData(2, 4, ItemGroup.STAFF)   # Rune Staff
item_data['6ss'] = ItemTypeData(1, 3, ItemGroup.STAFF)   # Walking Stick
item_data['6ls'] = ItemTypeData(1, 4, ItemGroup.STAFF)   # Stalagmite
item_data['6cs'] = ItemTypeData(1, 4, ItemGroup.STAFF)   # Elder Staff
item_data['6bs'] = ItemTypeData(1, 4, ItemGroup.STAFF)   # Shillelagh
item_data['6ws'] = ItemTypeData(2, 4, ItemGroup.STAFF)   # Archon Staff
# WAND
item_data['wnd'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Wand
item_data['ywn'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Yew Wand
item_data['bwn'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Bone Wand
item_data['gwn'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Grim Wand
item_data['9wn'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Burnt Wand
item_data['9yw'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Petrified Wand
item_data['9bw'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Tomb Wand
item_data['9gw'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Grave Wand
item_data['7wn'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Polished Wand
item_data['7yw'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Ghost Wand
item_data['7bw'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Lich Wand
item_data['7gw'] = ItemTypeData(1, 2, ItemGroup.WAND)   # Unearthed Wand
# SCEPTER
item_data['scp'] = ItemTypeData(1, 3, ItemGroup.SCEPTER)   # Sceptre
item_data['gsc'] = ItemTypeData(1, 3, ItemGroup.SCEPTER)   # Grand Sceptre
item_data['wsp'] = ItemTypeData(2, 3, ItemGroup.SCEPTER)   # War Sceptre
item_data['9sc'] = ItemTypeData(1, 3, ItemGroup.SCEPTER)   # Rune Sceptre
item_data['9qs'] = ItemTypeData(1, 3, ItemGroup.SCEPTER)   # Holy Water Spri
item_data['9ws'] = ItemTypeData(2, 3, ItemGroup.SCEPTER)   # Divine Sceptre
item_data['7sc'] = ItemTypeData(1, 3, ItemGroup.SCEPTER)   # Mighty Sceptre
item_data['7qs'] = ItemTypeData(1, 3, ItemGroup.SCEPTER)   # Seraph Rod
item_data['7ws'] = ItemTypeData(2, 3, ItemGroup.SCEPTER)   # Caduceus
# ASN
item_data['ktr'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Katar
item_data['wrb'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Wrist Blade
item_data['axf'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Hatchet Hands
item_data['ces'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Cestus
item_data['clw'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Claws
item_data['btl'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Blade Talons
item_data['skr'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Scissors Katar
item_data['9ar'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Quhab
item_data['9wb'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Wrist Spike
item_data['9xf'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Fascia
item_data['9cs'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Hand Scythe
item_data['9lw'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Greater Claws
item_data['9tw'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Greater Talons
item_data['9qr'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Scissors Quhab
item_data['7ar'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Suwayyah
item_data['7wb'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Wrist Sword
item_data['7xf'] = ItemTypeData(1, 3, ItemGroup.ASN)   # War Fist
item_data['7cs'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Battle Cestus
item_data['7lw'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Feral Claws
item_data['7tw'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Runic Talons
item_data['7qr'] = ItemTypeData(1, 3, ItemGroup.ASN)   # Scissors Suwayh
# SORC
item_data['ob1'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Eagle Orb
item_data['ob2'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Sacred Globe
item_data['ob3'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Smoked Sphere
item_data['ob4'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Clasped Orb
item_data['ob5'] = ItemTypeData(1, 3, ItemGroup.SORC)   # Jared's Stone
item_data['ob6'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Glowing Orb
item_data['ob7'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Crystalline Glb
item_data['ob8'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Cloudy Sphere
item_data['ob9'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Sparkling Ball
item_data['oba'] = ItemTypeData(1, 3, ItemGroup.SORC)   # Swirling Crystl
item_data['obb'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Heavenly Stone
item_data['obc'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Eldritch Orb
item_data['obd'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Demon Heart
item_data['obe'] = ItemTypeData(1, 2, ItemGroup.SORC)   # Vortex Orb
item_data['obf'] = ItemTypeData(1, 3, ItemGroup.SORC)   # Dimensional Shrd
# AMA
item_data['am1'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Stag Bow
item_data['am2'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Reflex Bow
item_data['am3'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Maiden Spear
item_data['am4'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Maiden Pike
item_data['am5'] = ItemTypeData(1, 3, ItemGroup.AMA)   # Maiden Javelin
item_data['am6'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Ashwood Bow
item_data['am7'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Ceremonial Bow
item_data['am8'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Ceremonial Spr
item_data['am9'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Ceremonial Pike
item_data['ama'] = ItemTypeData(1, 3, ItemGroup.AMA)   # Ceremonial Jav
item_data['amb'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Matriarchal Bow
item_data['amc'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Grnd Matron Bow
item_data['amd'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Matriarchal Spr
item_data['ame'] = ItemTypeData(2, 4, ItemGroup.AMA)   # Matriarchal Pik
item_data['amf'] = ItemTypeData(1, 3, ItemGroup.AMA)   # Matriarchal Jav
# CIRCLET
item_data['ci0'] = ItemTypeData(2, 2, ItemGroup.CIRCLET)   # Circlet
item_data['ci1'] = ItemTypeData(2, 2, ItemGroup.CIRCLET)   # Coronet
item_data['ci2'] = ItemTypeData(2, 2, ItemGroup.CIRCLET)   # Tiara
item_data['ci3'] = ItemTypeData(2, 2, ItemGroup.CIRCLET)   # Diadem
# THROWPOT
item_data['gps'] = ItemTypeData(1, 1, ItemGroup.THROWPOT)   # Rancid Gas Pot
item_data['ops'] = ItemTypeData(1, 1, ItemGroup.THROWPOT)   # Oil Potion
item_data['gpm'] = ItemTypeData(1, 1, ItemGroup.THROWPOT)   # Choking Gas Pot
item_data['opm'] = ItemTypeData(1, 1, ItemGroup.THROWPOT)   # Exploding Pot
item_data['gpl'] = ItemTypeData(1, 1, ItemGroup.THROWPOT)   # Strangling Gas
item_data['opl'] = ItemTypeData(1, 1, ItemGroup.THROWPOT)   # Fulminating Pot
# QUEST
item_data['leg'] = ItemTypeData(1, 3, ItemGroup.QUEST)   # Wirt’s Leg
item_data['hdm'] = ItemTypeData(1, 2, ItemGroup.QUEST)   # Horadric Malus
item_data['bks'] = ItemTypeData(2, 2, ItemGroup.QUEST)   # Scroll of Inifuss 1
item_data['bkd'] = ItemTypeData(2, 2, ItemGroup.QUEST)   # Scroll of Inifuss 2
item_data['ass'] = ItemTypeData(2, 2, ItemGroup.QUEST)   # Book of Skill
item_data['box'] = ItemTypeData(2, 2, ItemGroup.QUEST)   # Horadric Cube
item_data['tr1'] = ItemTypeData(2, 2, ItemGroup.QUEST)   # Horadric Scroll
item_data['msf'] = ItemTypeData(1, 3, ItemGroup.QUEST)   # Staff of Kings
item_data['vip'] = ItemTypeData(1, 1, ItemGroup.QUEST)   # Viper Amulet
item_data['hst'] = ItemTypeData(1, 4, ItemGroup.QUEST)   # Horadric Staff
item_data['xyz'] = ItemTypeData(1, 1, ItemGroup.QUEST)   # Potion of Life
item_data['j34'] = ItemTypeData(1, 2, ItemGroup.QUEST)   # A Jade Figurine
item_data['g34'] = ItemTypeData(1, 2, ItemGroup.QUEST)   # The Golden Bird
item_data['bbb'] = ItemTypeData(2, 2, ItemGroup.QUEST)   # Lam Esen’s Tome
item_data['g33'] = ItemTypeData(1, 2, ItemGroup.QUEST)   # Gidbinn
item_data['qf1'] = ItemTypeData(2, 3, ItemGroup.QUEST)   # Khalim’s Flail
item_data['qf2'] = ItemTypeData(2, 3, ItemGroup.QUEST)   # Khalim’s Will
item_data['qey'] = ItemTypeData(1, 1, ItemGroup.QUEST)   # Khalim’s Eye
item_data['qhr'] = ItemTypeData(1, 1, ItemGroup.QUEST)   # Khalim’s Heart
item_data['qbr'] = ItemTypeData(1, 1, ItemGroup.QUEST)   # Khalim’s Brain
item_data['mss'] = ItemTypeData(1, 1, ItemGroup.QUEST)   # Mephisto’s Soulstone
item_data['hfh'] = ItemTypeData(2, 3, ItemGroup.QUEST)   # Hellforge Hammr
item_data['ice'] = ItemTypeData(1, 1, ItemGroup.QUEST)   # Malah’s Potion
item_data['tr2'] = ItemTypeData(2, 2, ItemGroup.QUEST)   # Scroll of Resistance
# GEMS
item_data['gcv'] = ItemTypeData(1, 1, ItemGroup.GEM_AMETHYST)   # Chipped Amethyst
item_data['gfv'] = ItemTypeData(1, 1, ItemGroup.GEM_AMETHYST)   # Flawed Amethyst
item_data['gsv'] = ItemTypeData(1, 1, ItemGroup.GEM_AMETHYST)   # Amethyst
item_data['gzv'] = ItemTypeData(1, 1, ItemGroup.GEM_AMETHYST)   # Flawless Amethyst
item_data['gpv'] = ItemTypeData(1, 1, ItemGroup.GEM_AMETHYST)   # Perfect Amethyst
item_data['gcw'] = ItemTypeData(1, 1, ItemGroup.GEM_DIAMOND)   # Chipped Diamond
item_data['gfw'] = ItemTypeData(1, 1, ItemGroup.GEM_DIAMOND)   # Flawed Diamond
item_data['gsw'] = ItemTypeData(1, 1, ItemGroup.GEM_DIAMOND)   # Diamond
item_data['glw'] = ItemTypeData(1, 1, ItemGroup.GEM_DIAMOND)   # Flawless Diamond
item_data['gpw'] = ItemTypeData(1, 1, ItemGroup.GEM_DIAMOND)   # Perfect Diamond
item_data['gcg'] = ItemTypeData(1, 1, ItemGroup.GEM_EMERALD)   # Chipped Emerald
item_data['gfg'] = ItemTypeData(1, 1, ItemGroup.GEM_EMERALD)   # Flawed Emerald
item_data['gsg'] = ItemTypeData(1, 1, ItemGroup.GEM_EMERALD)   # Emerald
item_data['glg'] = ItemTypeData(1, 1, ItemGroup.GEM_EMERALD)   # Flawless Emerald
item_data['gpg'] = ItemTypeData(1, 1, ItemGroup.GEM_EMERALD)   # Perfect Emerald
item_data['gcr'] = ItemTypeData(1, 1, ItemGroup.GEM_RUBY)   # Chipped Ruby
item_data['gfr'] = ItemTypeData(1, 1, ItemGroup.GEM_RUBY)   # Flawed Ruby
item_data['gsr'] = ItemTypeData(1, 1, ItemGroup.GEM_RUBY)   # Ruby
item_data['glr'] = ItemTypeData(1, 1, ItemGroup.GEM_RUBY)   # Flawless Ruby
item_data['gpr'] = ItemTypeData(1, 1, ItemGroup.GEM_RUBY)   # Perfect Ruby
item_data['gcb'] = ItemTypeData(1, 1, ItemGroup.GEM_SAPPHIRE)   # Chipped Sapphire
item_data['gfb'] = ItemTypeData(1, 1, ItemGroup.GEM_SAPPHIRE)   # Flawed Sapphire
item_data['gsb'] = ItemTypeData(1, 1, ItemGroup.GEM_SAPPHIRE)   # Sapphire
item_data['glb'] = ItemTypeData(1, 1, ItemGroup.GEM_SAPPHIRE)   # Flawless Sapphire
item_data['gpb'] = ItemTypeData(1, 1, ItemGroup.GEM_SAPPHIRE)   # Perfect Sapphire
item_data['skc'] = ItemTypeData(1, 1, ItemGroup.GEM_SKULL)   # Chipped Skull
item_data['skf'] = ItemTypeData(1, 1, ItemGroup.GEM_SKULL)   # Flawed Skull
item_data['sku'] = ItemTypeData(1, 1, ItemGroup.GEM_SKULL)   # Skull
item_data['skl'] = ItemTypeData(1, 1, ItemGroup.GEM_SKULL)   # Flawless Skull
item_data['skz'] = ItemTypeData(1, 1, ItemGroup.GEM_SKULL)   # Perfect Skull
item_data['gcy'] = ItemTypeData(1, 1, ItemGroup.GEM_TOPAZ)   # Chipped Topaz
item_data['gfy'] = ItemTypeData(1, 1, ItemGroup.GEM_TOPAZ)   # Flawed Topaz
item_data['gsy'] = ItemTypeData(1, 1, ItemGroup.GEM_TOPAZ)   # Topaz
item_data['gly'] = ItemTypeData(1, 1, ItemGroup.GEM_TOPAZ)   # Flawless Topaz
item_data['gpy'] = ItemTypeData(1, 1, ItemGroup.GEM_TOPAZ)   # Perfect Topaz


class GemQuality(IntEnum):
    CHIPPED = 1
    FLAWED = 2
    NORM = 3
    FLAWLESS = 4
    PERFECT = 5


def get_gem_quality(item_code):
    if item_code in ['gcv', 'gcw', 'gcg', 'gcr', 'gcb', 'skc', 'gcy']:
        return GemQuality.CHIPPED
    if item_code in ['gfv', 'gfw', 'gfg', 'gfr', 'gfb', 'skf', 'gfy']:
        return GemQuality.FLAWED
    if item_code in ['gsv', 'gsw', 'gsg', 'gsr', 'gsb', 'sku', 'gsy']:
        return GemQuality.NORM
    if item_code in ['gzv', 'glw', 'glg', 'glr', 'glb', 'skl', 'gly']:
        return GemQuality.FLAWLESS
    if item_code in ['gpw', 'gpv', 'gpb', 'gpy', 'gpr', 'skz', 'gpg']:
        return GemQuality.PERFECT
    return None


def get_pgem_code(flawless_code):
    if flawless_code == 'gzv':
        return 'gpv'
    if flawless_code == 'glw':
        return 'gpw'
    if flawless_code == 'glg':
        return 'gpg'
    if flawless_code == 'glr':
        return 'gpr'
    if flawless_code == 'glb':
        return 'gpb'
    if flawless_code == 'skl':
        return 'skz'
    if flawless_code == 'gly':
        return 'gpy'
    return None


# RUNE
item_data['r01'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # El Rune
item_data['r02'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Eld Rune
item_data['r03'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Tir Rune
item_data['r04'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Nef Rune
item_data['r05'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Eth Rune
item_data['r06'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Ith Rune
item_data['r07'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Tal Rune
item_data['r08'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Ral Rune
item_data['r09'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Ort Rune
item_data['r10'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Thul Rune
item_data['r11'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Amn Rune
item_data['r12'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Sol Rune
item_data['r13'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Shael Rune
item_data['r14'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Dol Rune
item_data['r15'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Hel Rune
item_data['r16'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Io Rune
item_data['r17'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Lum Rune
item_data['r18'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Ko Rune
item_data['r19'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Fal Rune
item_data['r20'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Lem Rune
item_data['r21'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Pul Rune
item_data['r22'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Um Rune
item_data['r23'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Mal Rune
item_data['r24'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Ist Rune
item_data['r25'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Gul Rune
item_data['r26'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Vex Rune
item_data['r27'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Ohm Rune
item_data['r28'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Lo Rune
item_data['r29'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Sur Rune
item_data['r30'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Ber Rune
item_data['r31'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Jah Rune
item_data['r32'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Cham Rune
item_data['r33'] = ItemTypeData(1, 1, ItemGroup.RUNE)   # Zod Rune
# POTION
item_data['yps'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Antidote Potion
item_data['vps'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Stamina Potion
item_data['wms'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Thawing Potion
item_data['hp1'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Minor Healing Potion
item_data['mp1'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Minor Mana Potion
item_data['hp2'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Light Healing Potion
item_data['mp2'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Light Mana Potion
item_data['hp3'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Healing Potion
item_data['mp3'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Mana Potion
item_data['hp4'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Greater Healing Potion
item_data['mp4'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Greater Mana Potion
item_data['hp5'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Super Healing Potion
item_data['mp5'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Super Mana Potion
item_data['rvs'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Rejuv Potion
item_data['rvl'] = ItemTypeData(1, 1, ItemGroup.POTION)   # Full Rejuv Potion
# CHARM
item_data['cm1'] = ItemTypeData(1, 1, ItemGroup.CHARM)   # Charm Small
item_data['cm2'] = ItemTypeData(1, 2, ItemGroup.CHARM)   # Charm Large
item_data['cm3'] = ItemTypeData(1, 3, ItemGroup.CHARM)   # Charm Grand
# SCROLL
item_data['isc'] = ItemTypeData(1, 1, ItemGroup.SCROLL)   # Identify Scroll
item_data['tsc'] = ItemTypeData(1, 1, ItemGroup.SCROLL)   # Town Portal Scroll
item_data['tbk'] = ItemTypeData(1, 2, ItemGroup.SCROLL)   # Tome of Town Portal
item_data['ibk'] = ItemTypeData(1, 2, ItemGroup.SCROLL)   # Tome of Identify
# MISC
item_data['aqv'] = ItemTypeData(1, 3, ItemGroup.MISC)   # Arrows
item_data['cqv'] = ItemTypeData(1, 3, ItemGroup.MISC)   # Bolts
item_data['key'] = ItemTypeData(1, 1, ItemGroup.MISC)   # Key
item_data['gld'] = ItemTypeData(1, 1, ItemGroup.MISC)   # gold
item_data['ear'] = ItemTypeData(1, 1, ItemGroup.MISC)   # Ear
item_data['std'] = ItemTypeData(1, 1, ItemGroup.MISC)   # Standard of Heroes
# JEWEL
item_data['jew'] = ItemTypeData(1, 1, ItemGroup.JEWEL)   # Jewel
# AMULET
item_data['amu'] = ItemTypeData(1, 1, ItemGroup.AMULET)   # amulet
# RING
item_data['rin'] = ItemTypeData(1, 1, ItemGroup.RING)   # ring
# UBERKEY
item_data['pk1'] = ItemTypeData(1, 2, ItemGroup.UBERKEY)   # Key of Terror
item_data['pk2'] = ItemTypeData(1, 2, ItemGroup.UBERKEY)   # Key of Hate
item_data['pk3'] = ItemTypeData(1, 2, ItemGroup.UBERKEY)   # Key of Destruction
# UBERPART
item_data['bey'] = ItemTypeData(1, 2, ItemGroup.UBERPART)   # Baal's Eye
item_data['dhn'] = ItemTypeData(1, 2, ItemGroup.UBERPART)   # Diablo's Horn
item_data['mbr'] = ItemTypeData(1, 2, ItemGroup.UBERPART)   # Mephisto's Brain
# ESSENCE
item_data['bet'] = ItemTypeData(1, 1, ItemGroup.ESSENCE)   # Burning Essence of Terror
item_data['ceh'] = ItemTypeData(1, 1, ItemGroup.ESSENCE)   # Charged Essence of Hatred
item_data['fed'] = ItemTypeData(1, 1, ItemGroup.ESSENCE)   # Festering Essence of Destruction
item_data['tes'] = ItemTypeData(1, 1, ItemGroup.ESSENCE)   # Twisted Essence of Suffering
item_data['toa'] = ItemTypeData(1, 1, ItemGroup.ESSENCE)   # Token of Absolution


# ITEM SET DATA
set_id: Dict[int, int] = {}


def get_true_set_id(specific_set_id):
    return set_id[specific_set_id]


set_id[0] = 1  # Civerb's Ward
set_id[1] = 1  # Civerb's Icon
set_id[2] = 1  # Civerb's Cudgel
set_id[3] = 2  # Hsarus' Iron Heel
set_id[4] = 2  # Hsarus' Iron Fist
set_id[5] = 2  # Hsarus' Iron Stay
set_id[6] = 3  # Cleglaw's Tooth
set_id[7] = 3  # Cleglaw's Claw
set_id[8] = 3  # Cleglaw's Pincers
set_id[9] = 4  # Iratha's Collar
set_id[10] = 4  # Iratha's Cuff
set_id[11] = 4  # Iratha's Coil
set_id[12] = 4  # Iratha's Cord
set_id[13] = 5  # Isenhart's Lightbrand
set_id[14] = 5  # Isenhart's Parry
set_id[15] = 5  # Isenhart's Case
set_id[16] = 5  # Isenhart's Horns
set_id[17] = 6  # Vidala's Barb
set_id[18] = 6  # Vidala's Fetlock
set_id[19] = 6  # Vidala's Ambush
set_id[20] = 6  # Vidala's Snare
set_id[21] = 7  # Milabrega's Orb
set_id[22] = 7  # Milabrega's Rod
set_id[23] = 7  # Milabrega's Diadem
set_id[24] = 7  # Milabrega's Robe
set_id[25] = 8  # Cathan's Rule
set_id[26] = 8  # Cathan's Mesh
set_id[27] = 8  # Cathan's Visage
set_id[28] = 8  # Cathan's Sigil
set_id[29] = 8  # Cathan's Seal
set_id[30] = 9  # Tancred's Crowbill
set_id[31] = 9  # Tancred's Spine
set_id[32] = 9  # Tancred's Hobnails
set_id[33] = 9  # Tancred's Weird
set_id[34] = 9  # Tancred's Skull
set_id[35] = 10  # Sigon's Gage
set_id[36] = 10  # Sigon's Visor
set_id[37] = 10  # Sigon's Shelter
set_id[38] = 10  # Sigon's Sabot
set_id[39] = 10  # Sigon's Wrap
set_id[40] = 10  # Sigon's Guard
set_id[41] = 11  # Infernal Cranium
set_id[42] = 11  # Infernal Torch
set_id[43] = 11  # Infernal Sign
set_id[44] = 12  # Berserker's Headgear
set_id[45] = 12  # Berserker's Hauberk
set_id[46] = 12  # Berserker's Hatchet
set_id[47] = 13  # Death's Hand
set_id[48] = 13  # Death's Guard
set_id[49] = 13  # Death's Touch
set_id[50] = 14  # Angelic Sickle
set_id[51] = 14  # Angelic Mantle
set_id[52] = 14  # Angelic Halo
set_id[53] = 14  # Angelic Wings
set_id[54] = 15  # Arctic Horn
set_id[55] = 15  # Arctic Furs
set_id[56] = 15  # Arctic Binding
set_id[57] = 15  # Arctic Mitts
set_id[58] = 16  # Arcanna's Sign
set_id[59] = 16  # Arcanna's Deathwand
set_id[60] = 16  # Arcanna's Head
set_id[61] = 16  # Arcanna's Flesh
set_id[62] = 17  # Natalya's Totem
set_id[63] = 17  # Natalya's Mark
set_id[64] = 17  # Natalya's Shadow
set_id[65] = 17  # Natalya's Soul
set_id[66] = 18  # Aldur's Stony Gaze
set_id[67] = 18  # Aldur's Deception
set_id[68] = 18  # Aldur's Gauntlet
set_id[69] = 18  # Aldur's Advance
set_id[70] = 19  # Immortal King's Will
set_id[71] = 19  # Immortal King's Soul Cage
set_id[72] = 19  # Immortal King's Detail
set_id[73] = 19  # Immortal King's Forge
set_id[74] = 19  # Immortal King's Pillar
set_id[75] = 19  # Immortal King's Stone
set_id[76] = 20  # Tal Rasha's Fire-Spun Cloth
set_id[77] = 20  # Tal Rasha's Adjudication
set_id[78] = 20  # Tal Rasha's Lidless Eye
set_id[79] = 20  # Tal Rasha's Guardianship
set_id[80] = 20  # Tal Rasha's Horadric Crest
set_id[81] = 21  # Griswold's Valor
set_id[82] = 21  # Griswold's Heart
set_id[83] = 21  # Griswolds's Redemption
set_id[84] = 21  # Griswold's Honor
set_id[85] = 22  # Trang-Oul's Guise
set_id[86] = 22  # Trang-Oul's Scales
set_id[87] = 22  # Trang-Oul's Wing
set_id[88] = 22  # Trang-Oul's Claws
set_id[89] = 22  # Trang-Oul's Girth
set_id[90] = 23  # M'avina's True Sight
set_id[91] = 23  # M'avina's Embrace
set_id[92] = 23  # M'avina's Icy Clutch
set_id[93] = 23  # M'avina's Tenet
set_id[94] = 23  # M'avina's Caster
set_id[95] = 24  # Telling of Beads
set_id[96] = 24  # Laying of Hands
set_id[97] = 24  # Rite of Passage
set_id[98] = 24  # Dark Adherent
set_id[99] = 24  # Credendum
set_id[100] = 25  # Dangoon's Teaching
set_id[101] = 25  # Heaven's Taebaek
set_id[102] = 25  # Haemosu's Adament
set_id[103] = 25  # Ondal's Almighty
set_id[104] = 26  # Guillaume's Face
set_id[105] = 26  # Wilhelm's Pride
set_id[106] = 26  # Magnus' Skin
set_id[107] = 26  # Wihtstan's Guard
set_id[108] = 27  # Hwanin's Splendor
set_id[109] = 27  # Hwanin's Refuge
set_id[110] = 27  # Hwanin's Seal
set_id[111] = 27  # Hwanin's Justice
set_id[112] = 28  # Sazabi's Cobalt Redeemer
set_id[113] = 28  # Sazabi's Ghost Liberator
set_id[114] = 28  # Sazabi's Mental Sheath
set_id[115] = 29  # Bul-Kathos' Sacred Charge
set_id[116] = 29  # Bul-Kathos' Tribal Guardian
set_id[117] = 30  # Cow King's Horns
set_id[118] = 30  # Cow King's Hide
set_id[119] = 30  # Cow King's Hoofs
set_id[120] = 31  # Naj's Puzzler
set_id[121] = 31  # Naj's Light Plate
set_id[122] = 31  # Naj's Circlet
set_id[123] = 32  # Sander's Paragon
set_id[124] = 32  # Sander's Riprap
set_id[125] = 32  # Sander's Taboo
set_id[126] = 32  # Sander's Superstition
