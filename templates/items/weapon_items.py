from classes.items.consumable.Arrow import Arrow
from classes.items.weapon.MeleeWeapon import MeleeWeapon
from classes.items.weapon.RangedWeapon import RangedWeapon


weapon_items = {
    # Swords
    "long_sword": {
        "class": MeleeWeapon,
        "skill": "long_blade",
        "category": "weapon",
        "subcategory": "sword",
        "params": {
            "name": "Long Sword",
            "base_price": 160,  # average value
            "base_durability": 700,
            "base_attack": 10
        }
    },
    "short_sword": {
        "class": MeleeWeapon,
        "skill": "short_blade",
        "category": "weapon",
        "subcategory": "sword",
        "params": {
            "name": "Short Sword",
            "base_price": 100,
            "base_durability": 600,
            "base_attack": 8
        }
    },
    "dagger": {
        "class": MeleeWeapon,
        "skill": "short_blade",
        "category": "weapon",
        "subcategory": "dagger",
        "params": {
            "name": "Dagger",
            "base_price": 40,
            "base_durability": 300,
            "base_attack": 4
        }
    },

    # Blunt Weapons
    "mace": {
        "class": MeleeWeapon,
        "skill": "blunt_weapon",
        "category": "weapon",
        "subcategory": "mace",
        "params": {
            "name": "Mace",
            "base_price": 150,
            "base_durability": 800,
            "base_attack": 12
        }
    },
    "warhammer": {
        "class": MeleeWeapon,
        "skill": "blunt_weapon",
        "category": "weapon",
        "subcategory": "hammer",
        "params": {
            "name": "Warhammer",
            "base_price": 200,
            "base_durability": 850,
            "base_attack": 14
        }
    },
    "staff": {
        "class": MeleeWeapon,
        "skill": "blunt_weapon",
        "category": "weapon",
        "subcategory": "staff",
        "params": {
            "name": "Staff",
            "base_price": 80,
            "base_durability": 500,
            "base_attack": 6
        }
    },

    # Spears and Polearms
    "spear": {
        "class": MeleeWeapon,
        "skill": "spear",
        "category": "weapon",
        "subcategory": "spear",
        "params": {
            "name": "Spear",
            "base_price": 120,
            "base_durability": 750,
            "base_attack": 9
        }
    },
    "halberd": {
        "class": MeleeWeapon,
        "skill": "spear",
        "category": "weapon",
        "subcategory": "halberd",
        "params": {
            "name": "Halberd",
            "base_price": 180,
            "base_durability": 800,
            "base_attack": 11
        }
    },

    # Ranged Weapons
    "bow": {
        "class": RangedWeapon,
        "category": "weapon",
        "subcategory": "bow",
        "params": {
            "name": "Bow",
            "base_price": 150,
            "base_durability": 400,
            "base_attack": 10
        }
    },
    "crossbow": {
        "class": RangedWeapon,
        "category": "weapon",
        "subcategory": "crossbow",
        "params": {
            "name": "Crossbow",
            "base_price": 170,
            "base_durability": 400,
            "base_attack": 11
        }
    },
    "arrow": {
        "class": Arrow,
        "category": "consumable",
        "subcategory": "arrow",
        "params": {
            "name": "Arrow",
            "base_price": 2,
            "base_attack": 1
        }
    },
    "bolt": {
        "class": Arrow,  # Bolt class can be created if different mechanics are needed
        "category": "consumable",
        "subcategory": "bolt",
        "params": {
            "name": "Bolt",
            "base_price": 3,
            "base_attack": 2
        }
    },

    # Axes
    "battle_axe": {
        "class": MeleeWeapon,
        "skill": "axe",
        "category": "weapon",
        "subcategory": "axe",
        "params": {
            "name": "Battle Axe",
            "base_price": 160,
            "base_durability": 800,
            "base_attack": 13
        }
    },
    "war_axe": {
        "class": MeleeWeapon,
        "skill": "axe",
        "category": "weapon",
        "subcategory": "axe",
        "params": {
            "name": "War Axe",
            "base_price": 140,
            "base_durability": 700,
            "base_attack": 11
        }
    }
}