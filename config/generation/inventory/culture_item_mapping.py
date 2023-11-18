from enum.culture_enum import CultureEnum as CuE
from enum.items.ArmorEnum import ArmorEnum as ArE
from enum.items.WeaponEnum import WeaponEnum as WeE

from enum.ExperienceLevelEnum import ExperienceLevelEnum as ExE



weapon_experience_mapping = {
    WeE.IRON_SABER: ExE.BEGINNER,
    WeE.STEEL_SABER: ExE.AMATEUR,
    WeE.IRON_LONGSWORD: ExE.BEGINNER,
    WeE.STEEL_LONGSWORD: ExE.AMATEUR,
    WeE.IRON_MACE: ExE.BEGINNER,
    WeE.STEEL_MACE: ExE.AMATEUR,
    WeE.IRON_DAGGER: ExE.BEGINNER,
    WeE.STEEL_DAGGER: ExE.AMATEUR,
    WeE.IRON_WARHAMMER: ExE.BEGINNER,
    WeE.STEEL_WARHAMMER: ExE.AMATEUR,
    WeE.IRON_STAFF: ExE.BEGINNER,
    WeE.STEEL_STAFF: ExE.AMATEUR,
    WeE.IRON_SPEAR: ExE.BEGINNER,
    WeE.STEEL_SPEAR: ExE.AMATEUR,
    WeE.IRON_HALBERD: ExE.BEGINNER,
    WeE.STEEL_HALBERD: ExE.AMATEUR,
    WeE.IRON_BOW: ExE.BEGINNER,
    WeE.STEEL_BOW: ExE.AMATEUR,
    WeE.IRON_BATTLE_AXE: ExE.BEGINNER,
    WeE.STEEL_BATTLE_AXE: ExE.AMATEUR,
    WeE.SILVER_SABER: ExE.ADEPT,
    WeE.SILVER_LONGSWORD: ExE.ADEPT,
    WeE.SILVER_DAGGER: ExE.ADEPT,
    WeE.SILVER_MACE: ExE.ADEPT,
    WeE.SILVER_WARHAMMER: ExE.ADEPT,
    WeE.SILVER_STAFF: ExE.ADEPT,
    WeE.SILVER_SPEAR: ExE.ADEPT,
    WeE.SILVER_HALBERD: ExE.ADEPT,
    WeE.SILVER_BOW: ExE.ADEPT,
    WeE.SILVER_BATTLE_AXE: ExE.ADEPT,
    WeE.DWARVEN_SABER: ExE.EXPERT,
    WeE.DWARVEN_LONGSWORD: ExE.EXPERT,
    WeE.DWARVEN_DAGGER: ExE.EXPERT,
    WeE.DWARVEN_MACE: ExE.EXPERT,
    WeE.DWARVEN_WARHAMMER: ExE.EXPERT,
    WeE.DWARVEN_STAFF: ExE.EXPERT,
    WeE.DWARVEN_SPEAR: ExE.EXPERT,
    WeE.DWARVEN_HALBERD: ExE.EXPERT,
    WeE.DWARVEN_BOW: ExE.EXPERT,
    WeE.DWARVEN_BATTLE_AXE: ExE.EXPERT,
    WeE.GLASS_SABER: ExE.MASTER,
    WeE.GLASS_LONGSWORD: ExE.MASTER,
    WeE.GLASS_DAGGER: ExE.MASTER,
    WeE.GLASS_MACE: ExE.MASTER,
    WeE.GLASS_WARHAMMER: ExE.MASTER,
    WeE.GLASS_STAFF: ExE.MASTER,
    WeE.GLASS_SPEAR: ExE.MASTER,
    WeE.GLASS_HALBERD: ExE.MASTER,
    WeE.GLASS_BOW: ExE.MASTER,
    WeE.GLASS_BATTLE_AXE: ExE.MASTER,
    WeE.EBONY_SABER: ExE.LEGEND,
    WeE.EBONY_LONGSWORD: ExE.LEGEND,
    WeE.EBONY_DAGGER: ExE.LEGEND,
    WeE.EBONY_MACE: ExE.LEGEND,
    WeE.EBONY_WARHAMMER: ExE.LEGEND,
    WeE.EBONY_STAFF: ExE.LEGEND,
    WeE.EBONY_SPEAR: ExE.LEGEND,
    WeE.EBONY_HALBERD: ExE.LEGEND,
    WeE.EBONY_BOW: ExE.LEGEND,
    WeE.EBONY_BATTLE_AXE: ExE.LEGEND,
    WeE.DAEDRIC_SABER: ExE.LEGEND,
    WeE.DAEDRIC_LONGSWORD: ExE.LEGEND,
    WeE.DAEDRIC_DAGGER: ExE.LEGEND,
    WeE.DAEDRIC_MACE: ExE.LEGEND,
    WeE.DAEDRIC_WARHAMMER: ExE.LEGEND,
    WeE.DAEDRIC_STAFF: ExE.LEGEND,
    WeE.DAEDRIC_SPEAR: ExE.LEGEND,
    WeE.DAEDRIC_HALBERD: ExE.LEGEND,
    WeE.DAEDRIC_BOW: ExE.LEGEND,
    WeE.DAEDRIC_BATTLE_AXE: ExE.LEGEND,
}


chitin_armor = [ArE.CHITIN_CUIRASS, ArE.CHITIN_HELMET, ArE.CHITIN_GAUNTLETS, ArE.CHITIN_BOOTS, ArE.CHITIN_PAULDRONS]
bonemold_armor = [ArE.BONEMOLD_CUIRASS, ArE.BONEMOLD_HELMET, ArE.BONEMOLD_GAUNTLETS, ArE.BONEMOLD_BOOTS, ArE.BONEMOLD_PAULDRONS]
iron_armor = [ArE.IRON_CUIRASS, ArE.IRON_HELMET, ArE.IRON_GAUNTLETS, ArE.IRON_BOOTS, ArE.IRON_PAULDRONS]
steel_armor = [ArE.STEEL_CUIRASS, ArE.STEEL_HELMET, ArE.STEEL_GAUNTLETS, ArE.STEEL_BOOTS, ArE.STEEL_PAULDRONS]
dreugh_armor = [ArE.DREUGH_CUIRASS, ArE.DREUGH_HELMET, ArE.DREUGH_GAUNTLETS, ArE.DREUGH_BOOTS, ArE.DREUGH_PAULDRONS]
imperial_armor = [ArE.IMPERIAL_CUIRASS, ArE.IMPERIAL_HELMET, ArE.IMPERIAL_GAUNTLETS, ArE.IMPERIAL_BOOTS, ArE.IMPERIAL_PAULDRONS]
orcish_armor = [ArE.ORCISH_CUIRASS, ArE.ORCISH_HELMET, ArE.ORCISH_GAUNTLETS, ArE.ORCISH_BOOTS, ArE.ORCISH_PAULDRONS]
leather_armor = [ArE.LEATHER_CUIRASS, ArE.LEATHER_HELMET, ArE.LEATHER_GAUNTLETS, ArE.LEATHER_BOOTS, ArE.LEATHER_PAULDRONS]

culture_item_mapping = {
    CuE.ASHLANDER: {
        "weapon": [WeE.IRON_SABER, WeE.STEEL_SABER],
        "armor": [*leather_armor, *chitin_armor]
    },
    CuE.HLAALU: {
        "weapon": [WeE.STEEL_LONGSWORD, WeE.IRON_DAGGER],
        "armor": [*leather_armor, *bonemold_armor]
    },
    CuE.REDORAN: {
        "weapon": [WeE.IRON_MACE, WeE.STEEL_MACE],
        "armor": [*leather_armor, *bonemold_armor]
    },
    CuE.TELVANNI: {
        "weapon": [WeE.SILVER_STAFF, WeE.DWARVEN_STAFF],
        "armor": [*leather_armor, *bonemold_armor, *dreugh_armor]
    },
    CuE.IMPERIAL_CYR: {
        "weapon": [WeE.STEEL_LONGSWORD, WeE.IRON_DAGGER],
        "armor": [*leather_armor, *iron_armor, *steel_armor, *imperial_armor]
    },
    CuE.NORD: {
        "weapon": [WeE.IRON_BATTLE_AXE, WeE.STEEL_BATTLE_AXE],
        "armor": [*leather_armor, *iron_armor, *steel_armor]
    },
    CuE.ORC_TRIBAL: {
        "weapon": [WeE.IRON_WARHAMMER, WeE.STEEL_WARHAMMER],
        "armor": [*leather_armor, *iron_armor, *steel_armor, *orcish_armor]
    },
    CuE.REDGUARD_CROWN: {
        "weapon": [WeE.IRON_SABER, WeE.STEEL_SABER],
        "armor": [*leather_armor, *iron_armor, *steel_armor]
    },
    CuE.BOSMER_VAL: {
        "weapon": [WeE.IRON_BOW, WeE.STEEL_BOW],
        "armor": [*leather_armor, *iron_armor, *steel_armor]
    },
    CuE.COSMOP: {
        "weapon": [WeE.IRON_LONGSWORD, WeE.STEEL_LONGSWORD],
        "armor": [*leather_armor, *iron_armor, *steel_armor]
    },
}