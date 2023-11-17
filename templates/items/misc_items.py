from classes.items.Item import Item
from classes.items.SoulGem import SoulGem
from classes.items.consumable.Scroll import Scroll


misc_items = {
    "drake": {
        "class": Item, 
        "category": "Misc", 
        "params": {
            "name": "Drake", 
            "base_price": 1
        }, 
        "notTradeable": True
    },
    "broom": {
        "class": Item, 
        "category": "Misc", 
        "params": {
            "name": "Broom", 
            "base_price": 10
        }
    },
    "paper": {
        "class": Item, 
        "category": "Misc", 
        "params": {
            "name": "Paper", 
            "base_price": 2
        }
    },
    "bucket": {
        "class": Item, 
        "category": "Misc", 
        "params": {
            "name": "Bucket", 
            "base_price": 5
        }
    },
    "candle": {
        "class": Item, 
        "category": "Misc", 
        "params": {
            "name": "Candle", 
            "base_price": 3
        }
    },
    "lockpick": {
        "class": Item, 
        "category": "Misc", 
        "params": {
            "name": "Lockpick", 
            "base_price": 20
        }
    },
    "repair_tool": {
        "class": Item, 
        "category": "Misc", 
        "params": {
            "name": "Repair Tool", 
            "base_price": 50
        }
    },
    "alchemy_ingredient": {
        "class": Item, 
        "category": "Misc", 
        "params": {
            "name": "Alchemy Ingredient", 
            "base_price": 15  # Placeholder price, varies per ingredient
        }
    },
    "scroll": {
        "class": Scroll, 
        "category": "Misc", 
        "params": {
            "name": "Scroll", 
            "base_price": 40  # Average price, specific scrolls may vary
        }
    },
    "soul_gem": {
        "class": SoulGem, 
        "category": "Misc", 
        "params": {
            "name": "Soul Gem", 
            "base_price": 100  # Placeholder price, varies per gem
        }
    },
    # Additional items can be added here...
}
