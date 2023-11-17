inventory_class_optional_items = {
    "warrior": [
        {"item": "potion", "probability": 0.50, "quantity": 1, "std_dev": 0, "effect": "restore_health"},
        {"item": "potion", "probability": 0.30, "quantity": 1, "std_dev": 0, "effect": "fortify_strength"},
        {"item": "repair_tool", "probability": 0.40, "quantity": 1, "std_dev": 0}
    ],
    "mage": [
        {"item": "potion", "probability": 0.60, "quantity": 1, "std_dev": 0, "effect": "restore_magicka"},
        {"item": "scroll", "probability": 0.30, "quantity": 1, "std_dev": 0, "spell": "fireball"},
        {"item": "scroll", "probability": 0.25, "quantity": 1, "std_dev": 0, "spell": "levitation"}
    ],
    "thief": [
        {"item": "lockpick", "probability": 0.70, "quantity": 1, "std_dev": 0},
        {"item": "probe", "probability": 0.50, "quantity": 1, "std_dev": 0},
        {"item": "potion", "probability": 0.40, "quantity": 1, "std_dev": 0, "effect": "invisibility"}
    ],
    "monk": [
        {"item": "potion", "probability": 0.40, "quantity": 1, "std_dev": 0, "effect": "restore_health"},
        {"item": "potion", "probability": 0.30, "quantity": 1, "std_dev": 0, "effect": "fortify_unarmored"}
    ],
    "assassin": [
        {"item": "potion", "probability": 0.60, "quantity": 1, "std_dev": 0, "effect": "poison"},
        {"item": "potion", "probability": 0.40, "quantity": 1, "std_dev": 0, "effect": "swift_swim"},
        {"item": "chameleon_spell", "probability": 0.50, "quantity": 1, "std_dev": 0, "spell": "chameleon"}
    ],
    "bard": [
        {"item": "potion", "probability": 0.40, "quantity": 1, "std_dev": 0, "effect": "fortify_personality"}
    ],
    "battlemage": [
        {"item": "potion", "probability": 0.60, "quantity": 1, "std_dev": 0, "effect": "restore_magicka"},
        {"item": "scroll", "probability": 0.35, "quantity": 1, "std_dev": 0, "spell": "fireball"},
        {"item": "scroll", "probability": 0.35, "quantity": 1, "std_dev": 0, "spell": "frostbite"}
    ],
    "crusader": [
        {"item": "potion", "probability": 0.55, "quantity": 1, "std_dev": 0, "effect": "restore_health"},
        {"item": "potion", "probability": 0.40, "quantity": 1, "std_dev": 0, "effect": "fortify_attack"}
    ],
    "knight": [
        {"item": "potion", "probability": 0.60, "quantity": 1, "std_dev": 0, "effect": "restore_health"}
    ],
    "pilgrim": [
        {"item": "religious_icon", "probability": 0.50, "quantity": 1, "std_dev": 0},
        {"item": "potion", "probability": 0.30, "quantity": 1, "std_dev": 0, "effect": "fortify_endurance"}
    ],
    "scout": [
        {"item": "lockpick", "probability": 0.60, "quantity": 1, "std_dev": 0},
        {"item": "local_map", "probability": 0.50, "quantity": 1, "std_dev": 0},
        {"item": "potion", "probability": 0.40, "quantity": 1, "std_dev": 0, "effect": "restore_fatigue"}
    ],
    "sorcerer": [
        {"item": "scroll", "probability": 0.45, "quantity": 1, "std_dev": 0, "spell": "summon_skeleton"},
        {"item": "scroll", "probability": 0.30, "quantity": 1, "std_dev": 0, "spell": "command_creature"},
        {"item": "potion", "probability": 0.55, "quantity": 1, "std_dev": 0, "effect": "restore_magicka"}
    ],
    "spellsword": [
        {"item": "potion", "probability": 0.50, "quantity": 1, "std_dev": 0, "effect": "restore_magicka"},
        {"item": "potion", "probability": 0.45, "quantity": 1, "std_dev": 0, "effect": "restore_health"},
        {"item": "scroll", "probability": 0.35, "quantity": 1, "std_dev": 0, "spell": "shield"}
    ],
    "agent": [
        {"item": "lockpick", "probability": 0.60, "quantity": 1, "std_dev": 0},
        {"item": "probe", "probability": 0.40, "quantity": 1, "std_dev": 0},
        {"item": "potion", "probability": 0.35, "quantity": 1, "std_dev": 0, "effect": "chameleon"}
    ],
    "archer": [
        {"item": "bowstring", "probability": 0.50, "quantity": 1, "std_dev": 0},
        {"item": "potion", "probability": 0.35, "quantity": 1, "std_dev": 0, "effect": "fortify_agility"}
    ],
    "healer": [
        {"item": "potion", "probability": 0.70, "quantity": 1, "std_dev": 0, "effect": "restore_health"},
        {"item": "potion", "probability": 0.40, "quantity": 1, "std_dev": 0, "effect": "cure_common_disease"},
        {"item": "scroll", "probability": 0.50, "quantity": 1, "std_dev": 0, "spell": "heal"}
    ],
    "rogue": [
        {"item": "lockpick", "probability": 0.65, "quantity": 1, "std_dev": 0},
        {"item": "potion", "probability": 0.50, "quantity": 1, "std_dev": 0, "effect": "invisibility"},
        {"item": "chameleon_ring", "probability": 0.40, "quantity": 1, "std_dev": 0}
    ],
    "witchhunter": [
        {"item": "holy_water", "probability": 0.55, "quantity": 1, "std_dev": 0},
        {"item": "potion", "probability": 0.45, "quantity": 1, "std_dev": 0, "effect": "restore_magicka"},
        {"item": "scroll", "probability": 0.40, "quantity": 1, "std_dev": 0, "spell": "absorb_health"}
    ]
}
