from classes.items.armor.Boots import Boots
from classes.items.armor.Cuirass import Cuirass
from classes.items.armor.Gauntlets import Gauntlets
from classes.items.armor.Greaves import Greaves
from classes.items.armor.Helmet import Helmet
from classes.items.armor.Pauldrons import Pauldrons
from classes.items.armor.Shield import Shield


armor_items = {
    # Helmets
    "helmet_light": {
        "class": Helmet,
        "skill": "light_armor",
        "category": "armor",
        "subcategory": "helmet",
        "params": {
            "name": "Light Helmet",
            "base_price": 50,
            "base_durability": 300,
            "base_defense": 3
        }
    },
    "helmet_medium": {
        "class": Helmet,
        "skill": "medium_armor",
        "category": "armor",
        "subcategory": "helmet",
        "params": {
            "name": "Medium Helmet",
            "base_price": 100,
            "base_durability": 500,
            "base_defense": 5
        }
    },
    "helmet_heavy": {
        "class": Helmet,
        "skill": "heavy_armor",
        "category": "armor",
        "subcategory": "helmet",
        "params": {
            "name": "Heavy Helmet",
            "base_price": 150,
            "base_durability": 700,
            "base_defense": 8
        }
    },

    # Cuirasses
    "cuirass_light": {
        "class": Cuirass,
        "skill": "light_armor",
        "category": "armor",
        "subcategory": "cuirass",
        "params": {
            "name": "Light Cuirass",
            "base_price": 80,
            "base_durability": 350,
            "base_defense": 4
        }
    },
    "cuirass_medium": {
        "class": Cuirass,
        "skill": "medium_armor",
        "category": "armor",
        "subcategory": "cuirass",
        "params": {
            "name": "Medium Cuirass",
            "base_price": 150,
            "base_durability": 600,
            "base_defense": 7
        }
    },
    "cuirass_heavy": {
        "class": Cuirass,
        "skill": "heavy_armor",
        "category": "armor",
        "subcategory": "cuirass",
        "params": {
            "name": "Heavy Cuirass",
            "base_price": 250,
            "base_durability": 800,
            "base_defense": 10
        }
    },

    # Greaves
    "greaves_light": {
        "class": Greaves,
        "skill": "light_armor",
        "category": "armor",
        "subcategory": "greaves",
        "params": {
            "name": "Light Greaves",
            "base_price": 60,
            "base_durability": 300,
            "base_defense": 3
        }
    },
    "greaves_medium": {
        "class": Greaves,
        "skill": "medium_armor",
        "category": "armor",
        "subcategory": "greaves",
        "params": {
            "name": "Medium Greaves",
            "base_price": 120,
            "base_durability": 550,
            "base_defense": 6
        }
    },
    "greaves_heavy": {
        "class": Greaves,
        "skill": "heavy_armor",
        "category": "armor",
        "subcategory": "greaves",
        "params": {
            "name": "Heavy Greaves",
            "base_price": 200,
            "base_durability": 750,
            "base_defense": 9
        }
    },

    # Gauntlets
    "gauntlets_light": {
        "class": Gauntlets,
        "skill": "light_armor",
        "category": "armor",
        "subcategory": "gauntlets",
        "params": {
            "name": "Light Gauntlets",
            "base_price": 40,
            "base_durability": 250,
            "base_defense": 2
        }
    },
    "gauntlets_medium": {
        "class": Gauntlets,
        "skill": "medium_armor",
        "category": "armor",
        "subcategory": "gauntlets",
        "params": {
            "name": "Medium Gauntlets",
            "base_price": 90,
            "base_durability": 450,
            "base_defense": 4
        }
    },
    "gauntlets_heavy": {
        "class": Gauntlets,
        "skill": "heavy_armor",
        "category": "armor",
        "subcategory": "gauntlets",
        "params": {
            "name": "Heavy Gauntlets",
            "base_price": 140,
            "base_durability": 650,
            "base_defense": 7
        }
    },

    # Boots
    "boots_light": {
        "class": Boots,
        "skill": "light_armor",
        "category": "armor",
        "subcategory": "boots",
        "params": {
            "name": "Light Boots",
            "base_price": 40,
            "base_durability": 250,
            "base_defense": 2
        }
    },
    "boots_medium": {
        "class": Boots,
        "skill": "medium_armor",
        "category": "armor",
        "subcategory": "boots",
        "params": {
            "name": "Medium Boots",
            "base_price": 90,
            "base_durability": 450,
            "base_defense": 4
        }
    },
    "boots_heavy": {
        "class": Boots,
        "skill": "heavy_armor",
        "category": "armor",
        "subcategory": "boots",
        "params": {
            "name": "Heavy Boots",
            "base_price": 140,
            "base_durability": 650,
            "base_defense": 7
        }
    },

    # Pauldrons
    "pauldrons_light": {
        "class": Pauldrons,
        "skill": "light_armor",
        "category": "armor",
        "subcategory": "pauldrons",
        "params": {
            "name": "Light Pauldrons",
            "base_price": 55,
            "base_durability": 280,
            "base_defense": 2.5
        }
    },
    "pauldrons_medium": {
        "class": Pauldrons,
        "skill": "medium_armor",
        "category": "armor",
        "subcategory": "pauldrons",
        "params": {
            "name": "Medium Pauldrons",
            "base_price": 105,
            "base_durability": 480,
            "base_defense": 5
        }
    },
    "pauldrons_heavy": {
        "class": Pauldrons,
        "skill": "heavy_armor",
        "category": "armor",
        "subcategory": "pauldrons",
        "params": {
            "name": "Heavy Pauldrons",
            "base_price": 155,
            "base_durability": 680,
            "base_defense": 7.5
        }
    },

    # Shields
    "shield_light": {
        "class": Shield,
        "skill": "block",
        "category": "armor",
        "subcategory": "shield",
        "params": {
            "name": "Light Shield",
            "base_price": 70,
            "base_durability": 350,
            "base_defense": 4
        }
    },
    "shield_medium": {
        "class": Shield,
        "skill": "block",
        "category": "armor",
        "subcategory": "shield",
        "params": {
            "name": "Medium Shield",
            "base_price": 140,
            "base_durability": 600,
            "base_defense": 6
        }
    },
    "shield_heavy": {
        "class": Shield,
        "skill": "block",
        "category": "armor",
        "subcategory": "shield",
        "params": {
            "name": "Heavy Shield",
            "base_price": 210,
            "base_durability": 850,
            "base_defense": 9
        }
    }
}
