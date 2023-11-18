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
            ArmE.CHITIN_HELMET.value: (Helmet, 15, 2.0, 100, "armor", "helmet", 10, "light_armor"),
            ArmE.BONEMOLD_HELMET.value: (Helmet, 60, 4.5, 200, "armor", "helmet", 18, "medium_armor"),
            ArmE.IRON_HELMET.value: (Helmet, 30, 5.0, 150, "armor", "helmet", 14, "heavy_armor"),
            ArmE.STEEL_HELMET.value: (Helmet, 45, 6.0, 200, "armor", "helmet", 16, "heavy_armor"),
            ArmE.ORCISH_HELMET.value: (Helmet, 75, 7.0, 250, "armor", "helmet", 20, "heavy_armor"),
            ArmE.DREUGH_HELMET.value: (Helmet, 90, 8.0, 300, "armor", "helmet", 22, "heavy_armor"),
            ArmE.GLASS_HELMET.value: (Helmet, 105, 1.5, 350, "armor", "helmet", 24, "light_armor"),
            ArmE.EBONY_HELMET.value: (Helmet, 120, 10.0, 400, "armor", "helmet", 26, "heavy_armor"),
            ArmE.DAEDRIC_HELMET.value: (Helmet, 135, 15.0, 450, "armor", "helmet", 28, "heavy_armor"),
            ArmE.CHITIN_CUIRASS.value: (Cuirass, 50, 10.0, 200, "armor", "cuirass", 20, "light_armor"),
            ArmE.BONEMOLD_CUIRASS.value: (Cuirass, 200, 20.0, 400, "armor", "cuirass", 36, "medium_armor"),
            ArmE.IRON_CUIRASS.value: (Cuirass, 100, 30.0, 300, "armor", "cuirass", 28, "heavy_armor"),
            ArmE.STEEL_CUIRASS.value: (Cuirass, 150, 35.0, 400, "armor", "cuirass", 32, "heavy_armor"),
            ArmE.ORCISH_CUIRASS.value: (Cuirass, 250, 40.0, 500, "armor", "cuirass", 40, "heavy_armor"),
            ArmE.DREUGH_CUIRASS.value: (Cuirass, 300, 45.0, 600, "armor", "cuirass", 44, "heavy_armor"),
            ArmE.GLASS_CUIRASS.value: (Cuirass, 350, 7.5, 700, "armor", "cuirass", 48, "light_armor"),
            ArmE.EBONY_CUIRASS.value: (Cuirass, 400, 50.0, 800, "armor", "cuirass", 52, "heavy_armor"),
            ArmE.DAEDRIC_CUIRASS.value: (Cuirass, 450, 60.0, 900, "armor", "cuirass", 56, "heavy_armor"),
            ArmE.CHITIN_GREAVES.value: (Greaves, 30, 6.0, 150, "armor", "greaves", 12, "light_armor"),
            ArmE.BONEMOLD_GREAVES.value: (Greaves, 120, 13.5, 300, "armor", "greaves", 24, "medium_armor"),
            ArmE.IRON_GREAVES.value: (Greaves, 60, 15.0, 225, "armor", "greaves", 18, "heavy_armor"),
            ArmE.STEEL_GREAVES.value: (Greaves, 90, 18.0, 300, "armor", "greaves", 22, "heavy_armor"),
            ArmE.ORCISH_GREAVES.value: (Greaves, 150, 21.0, 375, "armor", "greaves", 26, "heavy_armor"),
            ArmE.DREUGH_GREAVES.value: (Greaves, 180, 24.0, 450, "armor", "greaves", 30, "heavy_armor"),
            ArmE.GLASS_GREAVES.value: (Greaves, 210, 4.5, 525, "armor", "greaves", 34, "light_armor"),
            ArmE.EBONY_GREAVES.value: (Greaves, 240, 27.0, 600, "armor", "greaves", 38, "heavy_armor"),
            ArmE.DAEDRIC_GREAVES.value: (Greaves, 270, 30.0, 675, "armor", "greaves", 42, "heavy_armor"),
            ArmE.CHITIN_GAUNTLETS.value: (Gauntlets, 20, 2.0, 100, "armor", "gauntlets", 8, "light_armor"),
            ArmE.BONEMOLD_GAUNTLETS.value: (Gauntlets, 80, 4.5, 200, "armor", "gauntlets", 16, "medium_armor"),
            ArmE.IRON_GAUNTLETS.value: (Gauntlets, 40, 5.0, 150, "armor", "gauntlets", 12, "heavy_armor"),
            ArmE.STEEL_GAUNTLETS.value: (Gauntlets, 60, 6.0, 200, "armor", "gauntlets", 16, "heavy_armor"),
            ArmE.ORCISH_GAUNTLETS.value: (Gauntlets, 100, 7.0, 250, "armor", "gauntlets", 20, "heavy_armor"),
            ArmE.DREUGH_GAUNTLETS.value: (Gauntlets, 120, 8.0, 300, "armor", "gauntlets", 24, "heavy_armor"),
            ArmE.GLASS_GAUNTLETS.value: (Gauntlets, 140, 1.5, 350, "armor", "gauntlets", 28, "light_armor"),
            ArmE.EBONY_GAUNTLETS.value: (Gauntlets, 160, 9.0, 400, "armor", "gauntlets", 32, "heavy_armor"),
            ArmE.DAEDRIC_GAUNTLETS.value: (Gauntlets, 180, 10.0, 450, "armor", "gauntlets", 36, "heavy_armor"),
            ArmE.CHITIN_BOOTS.value: (Boots, 20, 2.0, 100, "armor", "boots", 8, "light_armor"),
            ArmE.BONEMOLD_BOOTS.value: (Boots, 80, 4.5, 200, "armor", "boots", 16, "medium_armor"),
            ArmE.IRON_BOOTS.value: (Boots, 40, 5.0, 150, "armor", "boots", 12, "heavy_armor"),
            ArmE.STEEL_BOOTS.value: (Boots, 60, 6.0, 200, "armor", "boots", 16, "heavy_armor"),
            ArmE.ORCISH_BOOTS.value: (Boots, 100, 7.0, 250, "armor", "boots", 20, "heavy_armor"),
            ArmE.DREUGH_BOOTS.value: (Boots, 120, 8.0, 300, "armor", "boots", 24, "heavy_armor"),
            ArmE.GLASS_BOOTS.value: (Boots, 140, 1.5, 350, "armor", "boots", 28, "light_armor"),
            ArmE.EBONY_BOOTS.value: (Boots, 160, 9.0, 400, "armor", "boots", 32, "heavy_armor"),
            ArmE.DAEDRIC_BOOTS.value: (Boots, 180, 10.0, 450, "armor", "boots", 36, "heavy_armor"),
            ArmE.CHITIN_PAULDRONS.value: (Pauldrons, 25, 3.0, 125, "armor", "pauldrons", 10, "light_armor"),
            ArmE.BONEMOLD_PAULDRONS.value: (Pauldrons, 100, 6.75, 250, "armor", "pauldrons", 20, "medium_armor"),
            ArmE.IRON_PAULDRONS.value: (Pauldrons, 50, 7.5, 187.5, "armor", "pauldrons", 15, "heavy_armor"),
            ArmE.STEEL_PAULDRONS.value: (Pauldrons, 75, 9.0, 250, "armor", "pauldrons", 20, "heavy_armor"),
            ArmE.ORCISH_PAULDRONS.value: (Pauldrons, 125, 10.5, 312.5, "armor", "pauldrons", 25, "heavy_armor"),
            ArmE.DREUGH_PAULDRONS.value: (Pauldrons, 150, 12.0, 375, "armor", "pauldrons", 30, "heavy_armor"),
            ArmE.GLASS_PAULDRONS.value: (Pauldrons, 175, 2.25, 437.5, "armor", "pauldrons", 35, "light_armor"),
            ArmE.EBONY_PAULDRONS.value: (Pauldrons, 200, 13.5, 500, "armor", "pauldrons", 40, "heavy_armor"),
            ArmE.DAEDRIC_PAULDRONS.value: (Pauldrons, 225, 15.0, 562.5, "armor", "pauldrons", 45, "heavy_armor"),
            ArmE.CHITIN_SHIELD.value: (Shield, 35, 3.0, 175, "armor", "shield", 14, "block"),
            ArmE.BONEMOLD_SHIELD.value: (Shield, 140, 6.75, 350, "armor", "shield", 28, "block"),
            ArmE.IRON_SHIELD.value: (Shield, 70, 7.5, 262.5, "armor", "shield", 21, "block"),
            ArmE.STEEL_SHIELD.value: (Shield, 105, 9.0, 350, "armor", "shield", 28, "block"),
            ArmE.ORCISH_SHIELD.value: (Shield, 150, 10.5, 437.5, "armor", "shield", 33, "block"),
            ArmE.DREUGH_SHIELD.value: (Shield, 175, 12.0, 525, "armor", "shield", 38, "block"),
            ArmE.GLASS_SHIELD.value: (Shield, 200, 2.25, 612.5, "armor", "shield", 43, "block"),
            ArmE.EBONY_SHIELD.value: (Shield, 225, 13.5, 700, "armor", "shield", 48, "block"),
            ArmE.DAEDRIC_SHIELD.value: (Shield, 250, 15.0, 787.5, "armor", "shield", 53, "block"),
            ArmE.IMPERIAL_HELMET.value: (Helmet, 200, 2.0, 400, "armor", "helmet", 40, "heavy_armor"),
            ArmE.IMPERIAL_CUIRASS.value: (Cuirass, 400, 10.0, 800, "armor", "cuirass", 80, "heavy_armor"),
            ArmE.IMPERIAL_GREAVES.value: (Greaves, 200, 5.0, 400, "armor", "greaves", 40, "heavy_armor"),
            ArmE.IMPERIAL_GAUNTLETS.value: (Gauntlets, 100, 2.5, 200, "armor", "gauntlets", 20, "heavy_armor"),
            ArmE.IMPERIAL_BOOTS.value: (Boots, 100, 2.5, 200, "armor", "boots", 20, "heavy_armor"),
            ArmE.IMPERIAL_PAULDRONS.value: (Pauldrons, 150, 3.75, 300, "armor", "pauldrons", 30, "heavy_armor"),
            ArmE.IMPERIAL_SHIELD.value: (Shield, 250, 5.0, 500, "armor", "shield", 50, "block"),
            ArmE.ASSASSIN_SHIELD.value: (Shield, 275, 2.75, 550, "armor", "shield", 55, "block"),
            ArmE.MORAG_TONG_SHIELD.value: (Shield, 300, 3.0, 600, "armor", "shield", 60, "block"),
            ArmE.NETCH_LEATHER_SHIELD.value: (Shield, 325, 1.625, 650, "armor", "shield", 65, "block"),
            ArmE.ASSASSIN_GREAVES.value: (Greaves, 225, 2.25, 450, "armor", "greaves", 45, "light_armor"),
            ArmE.MORAG_TONG_GREAVES.value: (Greaves, 250, 2.5, 500, "armor", "greaves", 50, "light_armor"),
            ArmE.NETCH_LEATHER_GREAVES.value: (Greaves, 275, 1.375, 550, "armor", "greaves", 55, "light_armor"),
            ArmE.ASSASSIN_GAUNTLETS.value: (Gauntlets, 125, 1.25, 250, "armor", "gauntlets", 25, "light_armor"),
            ArmE.MORAG_TONG_GAUNTLETS.value: (Gauntlets, 150, 1.5, 300, "armor", "gauntlets", 30, "light_armor"),
            ArmE.NETCH_LEATHER_GAUNTLETS.value: (Gauntlets, 175, 0.875, 350, "armor", "gauntlets", 35, "light_armor"),
            ArmE.ASSASSIN_BOOTS.value: (Boots, 125, 1.25, 250, "armor", "boots", 25, "light_armor"),
            ArmE.MORAG_TONG_BOOTS.value: (Boots, 150, 1.5, 300, "armor", "boots", 30, "light_armor"),
            ArmE.NETCH_LEATHER_BOOTS.value: (Boots, 175, 0.875, 350, "armor", "boots", 35, "light_armor"),
            ArmE.ASSASSIN_PAULDRONS.value: (Pauldrons, 200, 2.0, 400, "armor", "pauldrons", 40, "light_armor"),
            ArmE.MORAG_TONG_PAULDRONS.value: (Pauldrons, 225, 2.25, 450, "armor", "pauldrons", 45, "light_armor"),
            ArmE.NETCH_LEATHER_PAULDRONS.value: (Pauldrons, 250, 1.25, 500, "armor", "pauldrons", 50, "light_armor"),
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
