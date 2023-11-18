from enum.items.ArmorEnum import ArmorEnum as ArmE
from classes.items.armor.Boots import Boots
from classes.items.armor.Cuirass import Cuirass
from classes.items.armor.Gauntlets import Gauntlets
from classes.items.armor.Greaves import Greaves
from classes.items.armor.Helmet import Helmet
from classes.items.armor.Pauldrons import Pauldrons
from classes.items.armor.Shield import Shield


class ArmorConfig:
    """
    This class represents the mapping of armor items to their details.
    Each armor is represented by a tuple of nine values: item, base_price, base_weight, durability, category, subcategory, base_defence, skill.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._index = {"item": 0, "base_price": 1, "base_weight": 2, "durability": 3, "category": 4, "subcategory": 5, "base_defence": 6, "skill": 7}
        self._config = {
            ArmE.HELMET_LIGHT.value: (Helmet, 50, 1.0, 300, "armor", "helmet", 3, "light_armor"),
            ArmE.HELMET_MEDIUM.value: (Helmet, 100, 2.0, 500, "armor", "helmet", 5, "medium_armor"),
            ArmE.HELMET_HEAVY.value: (Helmet, 150, 3.0, 700, "armor", "helmet", 8, "heavy_armor"),
            ArmE.CUIRASS_LIGHT.value: (Cuirass, 80, 2.0, 350, "armor", "cuirass", 4, "light_armor"),
            ArmE.CUIRASS_MEDIUM.value: (Cuirass, 150, 3.0, 600, "armor", "cuirass", 7, "medium_armor"),
            ArmE.CUIRASS_HEAVY.value: (Cuirass, 250, 4.0, 800, "armor", "cuirass", 10, "heavy_armor"),
            ArmE.GREAVES_LIGHT.value: (Greaves, 60, 1.5, 300, "armor", "greaves", 3, "light_armor"),
            ArmE.GREAVES_MEDIUM.value: (Greaves, 120, 2.5, 550, "armor", "greaves", 6, "medium_armor"),
            ArmE.GREAVES_HEAVY.value: (Greaves, 200, 3.5, 750, "armor", "greaves", 9, "heavy_armor"),
            ArmE.GAUNTLETS_LIGHT.value: (Gauntlets, 40, 1.0, 250, "armor", "gauntlets", 2, "light_armor"),
            ArmE.GAUNTLETS_MEDIUM.value: (Gauntlets, 90, 2.0, 450, "armor", "gauntlets", 4, "medium_armor"),
            ArmE.GAUNTLETS_HEAVY.value: (Gauntlets, 140, 3.0, 650, "armor", "gauntlets", 7, "heavy_armor"),
            ArmE.BOOTS_LIGHT.value: (Boots, 40, 1.0, 250, "armor", "boots", 2, "light_armor"),
            ArmE.BOOTS_MEDIUM.value: (Boots, 90, 2.0, 450, "armor", "boots", 4, "medium_armor"),
            ArmE.BOOTS_HEAVY.value: (Boots, 140, 3.0, 650, "armor", "boots", 7, "heavy_armor"),
            ArmE.PAULDRONS_LIGHT.value: (Pauldrons, 55, 1.5, 280, "armor", "pauldrons", 2.5, "light_armor"),
            ArmE.PAULDRONS_MEDIUM.value: (Pauldrons, 105, 2.5, 480, "armor", "pauldrons", 5, "medium_armor"),
            ArmE.PAULDRONS_HEAVY.value: (Pauldrons, 155, 3.5, 680, "armor", "pauldrons", 7.5, "heavy_armor"),
            ArmE.SHIELD_LIGHT.value: (Shield, 70, 1.5, 350, "armor", "shield", 4, "block"),
            ArmE.SHIELD_MEDIUM.value: (Shield, 140, 2.5, 600, "armor", "shield", 6, "block"),
            ArmE.SHIELD_HEAVY.value: (Shield, 210, 3.5, 850, "armor", "shield", 9, "block")
        }

    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given armor.
        The method takes one parameter: the name of the armor.
        The item_name parameter should be a string representing the name of the armor.
        The method returns a dictionary with keys: item, base_price, base_weight, durability, category, subcategory, base_defence, skill.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.armor.Helmet'>,
            'base_price': 50,
            'base_weight': 1.0,
            'durability': 300,
            'category': 'armor',
            'subcategory': 'helmet',
            'base_defence': 3,
            'skill': 'light_armor'
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Armor name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._index.keys(), self._config[item_name])}
