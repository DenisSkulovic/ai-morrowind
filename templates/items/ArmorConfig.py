from enum.ExperienceLevelEnum import ExperienceLevelEnum as ExE
from enum.SkillEnum import SkillEnum as SkE
from enum.items.ArmorEnum import ArmorEnum as ArmE
from classes.items.armor.Boots import Boots
from classes.items.armor.Cuirass import Cuirass
from classes.items.armor.Gauntlets import Gauntlets
from classes.items.armor.Greaves import Greaves
from classes.items.armor.Helmet import Helmet
from classes.items.armor.Pauldrons import Pauldrons
from classes.items.armor.Shield import Shield
from enum.items.ArmorPartEnum import ArmorPartEnum as ArPE


class ArmorConfig:
    """
    This class represents the mapping of armor items to their details.
    Each armor is represented by a tuple of ten values: item, base_price, base_weight, durability, category, subcategory, base_defence, skill, experience.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._cols = {"item": 0, "base_price": 1, "base_weight": 2, "durability": 3, "category": 4, "subcategory": 5, "base_defence": 6, "skill": 7, "experience": 8}
        self._config = {
            ArmE.LEATHER_HELMET.value: (Helmet, 15, 2.0, 75, "armor", ArPE.HELMET.value, 7, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.LEATHER_PAULDRONS.value: (Pauldrons, 25, 3.75, 93.75, "armor", ArPE.PAULDRONS.value, 7.5, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.LEATHER_CUIRASS.value: (Cuirass, 50, 15.0, 150, "armor", ArPE.CUIRASS.value, 14, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.LEATHER_GAUNTLETS.value: (Gauntlets, 20, 2.5, 75, "armor", ArPE.GAUNTLETS.value, 6, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.LEATHER_GREAVES.value: (Greaves, 30, 7.5, 112.5, "armor", ArPE.GREAVES.value, 9, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.LEATHER_BOOTS.value: (Boots, 20, 2.5, 75, "armor", ArPE.BOOTS.value, 6, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.LEATHER_SHIELD.value: (Shield, 35, 3.75, 131.25, "armor", ArPE.SHIELD.value, 10.5, SkE.BLOCK.value, ExE.BEGINNER.value),

            ArmE.CHITIN_HELMET.value: (Helmet, 15, 2.0, 100, "armor", ArPE.HELMET.value, 10, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.CHITIN_PAULDRONS.value: (Pauldrons, 25, 3.0, 125, "armor", ArPE.PAULDRONS.value, 10, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.CHITIN_CUIRASS.value: (Cuirass, 50, 10.0, 200, "armor", ArPE.CUIRASS.value, 20, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.CHITIN_GAUNTLETS.value: (Gauntlets, 20, 2.0, 100, "armor", ArPE.GAUNTLETS.value, 8, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.CHITIN_GREAVES.value: (Greaves, 30, 6.0, 150, "armor", ArPE.GREAVES.value, 12, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.CHITIN_BOOTS.value: (Boots, 20, 2.0, 100, "armor", ArPE.BOOTS.value, 8, SkE.LIGHT_ARMOR.value, ExE.BEGINNER.value),
            ArmE.CHITIN_SHIELD.value: (Shield, 35, 3.0, 175, "armor", ArPE.SHIELD.value, 14, SkE.BLOCK.value, ExE.BEGINNER.value),

            ArmE.BONEMOLD_HELMET.value: (Helmet, 60, 4.5, 200, "armor", ArPE.HELMET.value, 18, SkE.MEDIUM_ARMOR, ExE.AMATEUR.value),
            ArmE.BONEMOLD_PAULDRONS.value: (Pauldrons, 100, 6.75, 250, "armor", ArPE.PAULDRONS.value, 20, SkE.MEDIUM_ARMOR, ExE.AMATEUR.value),
            ArmE.BONEMOLD_CUIRASS.value: (Cuirass, 200, 20.0, 400, "armor", ArPE.CUIRASS.value, 36, SkE.MEDIUM_ARMOR, ExE.AMATEUR.value),
            ArmE.BONEMOLD_GAUNTLETS.value: (Gauntlets, 80, 4.5, 200, "armor", ArPE.GAUNTLETS.value, 16, SkE.MEDIUM_ARMOR, ExE.AMATEUR.value),
            ArmE.BONEMOLD_GREAVES.value: (Greaves, 120, 13.5, 300, "armor", ArPE.GREAVES.value, 24, SkE.MEDIUM_ARMOR, ExE.AMATEUR.value),
            ArmE.BONEMOLD_BOOTS.value: (Boots, 80, 4.5, 200, "armor", ArPE.BOOTS.value, 16, SkE.MEDIUM_ARMOR, ExE.AMATEUR.value),
            ArmE.BONEMOLD_SHIELD.value: (Shield, 140, 6.75, 350, "armor", ArPE.SHIELD.value, 28, SkE.BLOCK.value, ExE.AMATEUR.value),

            ArmE.ASSASSIN_PAULDRONS.value: (Pauldrons, 200, 2.0, 400, "armor", ArPE.PAULDRONS.value, 40, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            ArmE.ASSASSIN_GAUNTLETS.value: (Gauntlets, 125, 1.25, 250, "armor", ArPE.GAUNTLETS.value, 25, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            ArmE.ASSASSIN_GREAVES.value: (Greaves, 225, 2.25, 450, "armor", ArPE.GREAVES.value, 45, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            ArmE.ASSASSIN_BOOTS.value: (Boots, 125, 1.25, 250, "armor", ArPE.BOOTS.value, 25, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            ArmE.ASSASSIN_SHIELD.value: (Shield, 275, 2.75, 550, "armor", ArPE.SHIELD.value, 55, SkE.BLOCK.value, ExE.AMATEUR.value),

            ArmE.NETCH_LEATHER_SHIELD.value: (Shield, 325, 1.625, 650, "armor", ArPE.SHIELD.value, 65, SkE.BLOCK.value, ExE.AMATEUR.value),
            ArmE.NETCH_LEATHER_GREAVES.value: (Greaves, 275, 1.375, 550, "armor", ArPE.GREAVES.value, 55, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            ArmE.NETCH_LEATHER_GAUNTLETS.value: (Gauntlets, 175, 0.875, 350, "armor", ArPE.GAUNTLETS.value, 35, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            ArmE.NETCH_LEATHER_BOOTS.value: (Boots, 175, 0.875, 350, "armor", ArPE.BOOTS.value, 35, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            ArmE.NETCH_LEATHER_PAULDRONS.value: (Pauldrons, 250, 1.25, 500, "armor", ArPE.PAULDRONS.value, 50, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            
            ArmE.MORAG_TONG_PAULDRONS.value: (Pauldrons, 225, 2.25, 450, "armor", ArPE.PAULDRONS.value, 45, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            ArmE.MORAG_TONG_GAUNTLETS.value: (Gauntlets, 150, 1.5, 300, "armor", ArPE.GAUNTLETS.value, 30, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            ArmE.MORAG_TONG_GREAVES.value: (Greaves, 250, 2.5, 500, "armor", ArPE.GREAVES.value, 50, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            ArmE.MORAG_TONG_BOOTS.value: (Boots, 150, 1.5, 300, "armor", ArPE.BOOTS.value, 30, SkE.LIGHT_ARMOR.value, ExE.AMATEUR.value),
            ArmE.MORAG_TONG_SHIELD.value: (Shield, 300, 3.0, 600, "armor", ArPE.SHIELD.value, 60, SkE.BLOCK.value, ExE.AMATEUR.value),

            ArmE.IRON_HELMET.value: (Helmet, 30, 5.0, 150, "armor", ArPE.HELMET.value, 14, SkE.HEAVY_ARMOR, ExE.AMATEUR.value),
            ArmE.IRON_PAULDRONS.value: (Pauldrons, 50, 7.5, 187.5, "armor", ArPE.PAULDRONS.value, 15, SkE.HEAVY_ARMOR, ExE.AMATEUR.value),
            ArmE.IRON_CUIRASS.value: (Cuirass, 100, 30.0, 300, "armor", ArPE.CUIRASS.value, 28, SkE.HEAVY_ARMOR, ExE.AMATEUR.value),
            ArmE.IRON_GAUNTLETS.value: (Gauntlets, 40, 5.0, 150, "armor", ArPE.GAUNTLETS.value, 12, SkE.HEAVY_ARMOR, ExE.AMATEUR.value),
            ArmE.IRON_GREAVES.value: (Greaves, 60, 15.0, 225, "armor", ArPE.GREAVES.value, 18, SkE.HEAVY_ARMOR, ExE.AMATEUR.value),
            ArmE.IRON_BOOTS.value: (Boots, 40, 5.0, 150, "armor", ArPE.BOOTS.value, 12, SkE.HEAVY_ARMOR, ExE.AMATEUR.value),
            ArmE.IRON_SHIELD.value: (Shield, 70, 7.5, 262.5, "armor", ArPE.SHIELD.value, 21, SkE.BLOCK.value, ExE.AMATEUR.value),

            ArmE.STEEL_HELMET.value: (Helmet, 45, 6.0, 200, "armor", ArPE.HELMET.value, 16, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.STEEL_PAULDRONS.value: (Pauldrons, 75, 9.0, 250, "armor", ArPE.PAULDRONS.value, 20, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.STEEL_CUIRASS.value: (Cuirass, 150, 35.0, 400, "armor", ArPE.CUIRASS.value, 32, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.STEEL_GAUNTLETS.value: (Gauntlets, 60, 6.0, 200, "armor", ArPE.GAUNTLETS.value, 16, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.STEEL_GREAVES.value: (Greaves, 90, 18.0, 300, "armor", ArPE.GREAVES.value, 22, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.STEEL_BOOTS.value: (Boots, 60, 6.0, 200, "armor", ArPE.BOOTS.value, 16, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.STEEL_SHIELD.value: (Shield, 105, 9.0, 350, "armor", ArPE.SHIELD.value, 28, SkE.BLOCK.value, ExE.ADEPT.value),

            ArmE.IMPERIAL_HELMET.value: (Helmet, 200, 2.0, 400, "armor", ArPE.HELMET.value, 40, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.IMPERIAL_PAULDRONS.value: (Pauldrons, 150, 3.75, 300, "armor", ArPE.PAULDRONS.value, 30, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.IMPERIAL_CUIRASS.value: (Cuirass, 400, 10.0, 800, "armor", ArPE.CUIRASS.value, 80, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.IMPERIAL_GAUNTLETS.value: (Gauntlets, 100, 2.5, 200, "armor", ArPE.GAUNTLETS.value, 20, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.IMPERIAL_GREAVES.value: (Greaves, 200, 5.0, 400, "armor", ArPE.GREAVES.value, 40, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.IMPERIAL_BOOTS.value: (Boots, 100, 2.5, 200, "armor", ArPE.BOOTS.value, 20, SkE.HEAVY_ARMOR, ExE.ADEPT.value),
            ArmE.IMPERIAL_SHIELD.value: (Shield, 250, 5.0, 500, "armor", ArPE.SHIELD.value, 50, SkE.BLOCK.value, ExE.ADEPT.value),

            ArmE.ORCISH_HELMET.value: (Helmet, 75, 7.0, 250, "armor", ArPE.HELMET.value, 20, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.ORCISH_PAULDRONS.value: (Pauldrons, 125, 10.5, 312.5, "armor", ArPE.PAULDRONS.value, 25, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.ORCISH_CUIRASS.value: (Cuirass, 250, 40.0, 500, "armor", ArPE.CUIRASS.value, 40, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.ORCISH_GAUNTLETS.value: (Gauntlets, 100, 7.0, 250, "armor", ArPE.GAUNTLETS.value, 20, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.ORCISH_GREAVES.value: (Greaves, 150, 21.0, 375, "armor", ArPE.GREAVES.value, 26, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.ORCISH_BOOTS.value: (Boots, 100, 7.0, 250, "armor", ArPE.BOOTS.value, 20, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.ORCISH_SHIELD.value: (Shield, 150, 10.5, 437.5, "armor", ArPE.SHIELD.value, 33, SkE.BLOCK.value, ExE.EXPERT.value),

            ArmE.EBONY_HELMET.value: (Helmet, 120, 10.0, 400, "armor", ArPE.HELMET.value, 26, SkE.HEAVY_ARMOR, ExE.MASTER.value),
            ArmE.EBONY_PAULDRONS.value: (Pauldrons, 200, 13.5, 500, "armor", ArPE.PAULDRONS.value, 40, SkE.HEAVY_ARMOR, ExE.MASTER.value),
            ArmE.EBONY_CUIRASS.value: (Cuirass, 400, 50.0, 800, "armor", ArPE.CUIRASS.value, 52, SkE.HEAVY_ARMOR, ExE.MASTER.value),
            ArmE.EBONY_GAUNTLETS.value: (Gauntlets, 160, 9.0, 400, "armor", ArPE.GAUNTLETS.value, 32, SkE.HEAVY_ARMOR, ExE.MASTER.value),
            ArmE.EBONY_GREAVES.value: (Greaves, 240, 27.0, 600, "armor", ArPE.GREAVES.value, 38, SkE.HEAVY_ARMOR, ExE.MASTER.value),
            ArmE.EBONY_BOOTS.value: (Boots, 160, 9.0, 400, "armor", ArPE.BOOTS.value, 32, SkE.HEAVY_ARMOR, ExE.MASTER.value),
            ArmE.EBONY_SHIELD.value: (Shield, 225, 13.5, 700, "armor", ArPE.SHIELD.value, 48, SkE.BLOCK.value),

            ArmE.DREUGH_HELMET.value: (Helmet, 90, 8.0, 300, "armor", ArPE.HELMET.value, 22, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.DREUGH_PAULDRONS.value: (Pauldrons, 150, 12.0, 375, "armor", ArPE.PAULDRONS.value, 30, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.DREUGH_CUIRASS.value: (Cuirass, 300, 45.0, 600, "armor", ArPE.CUIRASS.value, 44, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.DREUGH_GAUNTLETS.value: (Gauntlets, 120, 8.0, 300, "armor", ArPE.GAUNTLETS.value, 24, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.DREUGH_GREAVES.value: (Greaves, 180, 24.0, 450, "armor", ArPE.GREAVES.value, 30, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.DREUGH_BOOTS.value: (Boots, 120, 8.0, 300, "armor", ArPE.BOOTS.value, 24, SkE.HEAVY_ARMOR, ExE.EXPERT.value),
            ArmE.DREUGH_SHIELD.value: (Shield, 175, 12.0, 525, "armor", ArPE.SHIELD.value, 38, SkE.BLOCK.value, ExE.EXPERT.value),
            
            ArmE.GLASS_HELMET.value: (Helmet, 105, 1.5, 350, "armor", ArPE.HELMET.value, 24, SkE.LIGHT_ARMOR.value, ExE.MASTER.value),
            ArmE.GLASS_PAULDRONS.value: (Pauldrons, 175, 2.25, 437.5, "armor", ArPE.PAULDRONS.value, 35, SkE.LIGHT_ARMOR.value, ExE.MASTER.value),
            ArmE.GLASS_CUIRASS.value: (Cuirass, 350, 7.5, 700, "armor", ArPE.CUIRASS.value, 48, SkE.LIGHT_ARMOR.value, ExE.MASTER.value),
            ArmE.GLASS_GAUNTLETS.value: (Gauntlets, 140, 1.5, 350, "armor", ArPE.GAUNTLETS.value, 28, SkE.LIGHT_ARMOR.value, ExE.MASTER.value),
            ArmE.GLASS_GREAVES.value: (Greaves, 210, 4.5, 525, "armor", ArPE.GREAVES.value, 34, SkE.LIGHT_ARMOR.value, ExE.MASTER.value),
            ArmE.GLASS_BOOTS.value: (Boots, 140, 1.5, 350, "armor", ArPE.BOOTS.value, 28, SkE.LIGHT_ARMOR.value, ExE.MASTER.value),
            ArmE.GLASS_SHIELD.value: (Shield, 200, 2.25, 612.5, "armor", ArPE.SHIELD.value, 43, SkE.BLOCK.value),

            ArmE.DAEDRIC_HELMET.value: (Helmet, 135, 15.0, 450, "armor", ArPE.HELMET.value, 28, SkE.HEAVY_ARMOR, ExE.LEGEND.value),
            ArmE.DAEDRIC_PAULDRONS.value: (Pauldrons, 225, 15.0, 562.5, "armor", ArPE.PAULDRONS.value, 45, SkE.HEAVY_ARMOR, ExE.LEGEND.value),
            ArmE.DAEDRIC_CUIRASS.value: (Cuirass, 450, 60.0, 900, "armor", ArPE.CUIRASS.value, 56, SkE.HEAVY_ARMOR, ExE.LEGEND.value),
            ArmE.DAEDRIC_GAUNTLETS.value: (Gauntlets, 180, 10.0, 450, "armor", ArPE.GAUNTLETS.value, 36, SkE.HEAVY_ARMOR, ExE.LEGEND.value),
            ArmE.DAEDRIC_GREAVES.value: (Greaves, 270, 30.0, 675, "armor", ArPE.GREAVES.value, 42, SkE.HEAVY_ARMOR, ExE.LEGEND.value),
            ArmE.DAEDRIC_BOOTS.value: (Boots, 180, 10.0, 450, "armor", ArPE.BOOTS.value, 36, SkE.HEAVY_ARMOR, ExE.LEGEND.value),
            ArmE.DAEDRIC_SHIELD.value: (Shield, 250, 15.0, 787.5, "armor", ArPE.SHIELD.value, 53, SkE.BLOCK.value, ExE.LEGEND.value),

        }

    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given armor.
        The method takes one parameter: the name of the armor.
        The item_name parameter should be a string representing the name of the armor.
        The method returns a dictionary with keys: item, base_price, base_weight, durability, category, subcategory, base_defence, skill, experience.
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
            'skill': 'light_armor',
            'experience': 'BEGINNER'
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Armor name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._cols.keys(), self._config[item_name])}
