from enum.SkillEnum import SkillEnum as SkE
from enum.items.WeaponEnum import WeaponEnum as WpnE
from classes.items.weapon.MeleeWeapon import MeleeWeapon
from classes.items.weapon.RangedWeapon import RangedWeapon
from enum.ExperienceLevelEnum import ExperienceLevelEnum as ExE
from enum.items.WeaponKindEnum import WeaponKindEnum as WeKE


class WeaponConfig:
    """
    This class represents the mapping of weapon items to their details.
    Each weapon is represented by a tuple of ten values: item, base_price, base_weight, durability, category, subcategory, base_attack, skill, experience.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._cols = {"item": 0, "base_price": 1, "base_weight": 2, "durability": 3, "category": 4, "subcategory": 5, "base_attack": 6, "skill": 7, "experience": 8}
        self._config = {
            WpnE.IRON_SABER.value: (MeleeWeapon, 60, 1.5, 300, "weapon", WeKE.SABER.value, 6, SkE.LONG_BLADE.value, ExE.BEGINNER.value),
            WpnE.IRON_SABER.value: (MeleeWeapon, 60, 1.5, 300, "weapon", WeKE.SABER.value, 6, SkE.LONG_BLADE.value, ExE.BEGINNER.value),
            WpnE.IRON_LONGSWORD.value: (MeleeWeapon, 70, 2.0, 350, "weapon", WeKE.LONGSWORD.value, 7, SkE.LONG_BLADE.value, ExE.BEGINNER.value),
            WpnE.IRON_SHORTSWORD.value: (MeleeWeapon, 50, 1.0, 250, "weapon", WeKE.SHORTSWORD.value, 5, SkE.SHORT_BLADE.value, ExE.BEGINNER.value),
            WpnE.IRON_LONGSWORD.value: (MeleeWeapon, 70, 2.0, 350, "weapon", WeKE.LONGSWORD.value, 7, SkE.LONG_BLADE.value, ExE.BEGINNER.value),
            WpnE.IRON_SHORTSWORD.value: (MeleeWeapon, 50, 1.0, 250, "weapon", WeKE.SHORTSWORD.value, 5, SkE.SHORT_BLADE.value, ExE.BEGINNER.value),
            WpnE.IRON_DAGGER.value: (MeleeWeapon, 30, 0.5, 150, "weapon", WeKE.DAGGER.value, 3, SkE.SHORT_BLADE.value, ExE.BEGINNER.value),
            WpnE.IRON_MACE.value: (MeleeWeapon, 80, 2.5, 400, "weapon", WeKE.MACE.value, 8, SkE.BLUNT_WEAPON.value, ExE.BEGINNER.value),
            WpnE.IRON_WARHAMMER.value: (MeleeWeapon, 90, 3.0, 450, "weapon", WeKE.WARHAMMER.value, 9, SkE.BLUNT_WEAPON.value, ExE.BEGINNER.value),
            WpnE.IRON_STAFF.value: (MeleeWeapon, 60, 1.5, 300, "weapon", WeKE.STAFF.value, 6, SkE.BLUNT_WEAPON.value, ExE.BEGINNER.value),
            WpnE.IRON_SPEAR.value: (MeleeWeapon, 70, 2.0, 350, "weapon", WeKE.SPEAR, 7, SkE.SPEAR.value, ExE.BEGINNER.value),
            WpnE.IRON_HALBERD.value: (MeleeWeapon, 80, 2.5, 400, "weapon", WeKE.HALBERD, 8, SkE.SPEAR.value, ExE.BEGINNER.value),
            WpnE.IRON_BOW.value: (RangedWeapon, 70, 1.5, 350, "weapon", WeKE.BOW, 7, SkE.MARKSMAN.value, ExE.BEGINNER.value),
            WpnE.IRON_CROSSBOW.value: (RangedWeapon, 80, 2.0, 400, "weapon", WeKE.CROSSBOW, 8, SkE.MARKSMAN.value, ExE.BEGINNER.value),
            WpnE.IRON_BATTLE_AXE.value: (MeleeWeapon, 90, 3.0, 450, "weapon", WeKE.BATTLE_AXE, 9, SkE.AXE.value, ExE.BEGINNER.value),
            WpnE.IRON_WAR_AXE.value: (MeleeWeapon, 80, 2.5, 400, "weapon", WeKE.WAR_AXE, 8, SkE.AXE.value, ExE.BEGINNER.value),

            WpnE.STEEL_SHORTSWORD.value: (MeleeWeapon, 70, 1.5, 350, "weapon", WeKE.SHORTSWORD.value, 7, SkE.SHORT_BLADE.value, ExE.AMATEUR.value),
            WpnE.STEEL_DAGGER.value: (MeleeWeapon, 50, 1.0, 250, "weapon", WeKE.DAGGER.value, 5, SkE.SHORT_BLADE.value, ExE.AMATEUR.value),
            WpnE.STEEL_MACE.value: (MeleeWeapon, 100, 3.0, 500, "weapon", WeKE.MACE.value, 10, SkE.BLUNT_WEAPON.value, ExE.AMATEUR.value),
            WpnE.STEEL_WARHAMMER.value: (MeleeWeapon, 110, 3.5, 550, "weapon", WeKE.WARHAMMER.value, 11, SkE.BLUNT_WEAPON.value, ExE.AMATEUR.value),
            WpnE.STEEL_STAFF.value: (MeleeWeapon, 80, 2.0, 400, "weapon", WeKE.STAFF.value, 8, SkE.BLUNT_WEAPON.value, ExE.AMATEUR.value),
            WpnE.STEEL_SPEAR.value: (MeleeWeapon, 90, 2.5, 450, "weapon", WeKE.SPEAR, 9, SkE.SPEAR.value, ExE.AMATEUR.value),
            WpnE.STEEL_HALBERD.value: (MeleeWeapon, 100, 3.0, 500, "weapon", WeKE.HALBERD, 10, SkE.SPEAR.value, ExE.AMATEUR.value),
            WpnE.STEEL_BOW.value: (RangedWeapon, 90, 2.0, 450, "weapon", WeKE.BOW, 9, SkE.MARKSMAN.value, ExE.AMATEUR.value),
            WpnE.STEEL_CROSSBOW.value: (RangedWeapon, 100, 2.5, 500, "weapon", WeKE.CROSSBOW, 10, SkE.MARKSMAN.value, ExE.AMATEUR.value),
            WpnE.STEEL_BATTLE_AXE.value: (MeleeWeapon, 110, 3.5, 550, "weapon", WeKE.BATTLE_AXE, 11, SkE.AXE.value, ExE.AMATEUR.value),
            WpnE.STEEL_SABER.value: (MeleeWeapon, 80, 2.0, 400, "weapon", WeKE.SABER.value, 8, SkE.LONG_BLADE.value, ExE.AMATEUR.value),
            WpnE.STEEL_LONGSWORD.value: (MeleeWeapon, 90, 2.5, 450, "weapon", WeKE.LONGSWORD.value, 9, SkE.LONG_BLADE.value, ExE.AMATEUR.value),
            WpnE.STEEL_SHORTSWORD.value: (MeleeWeapon, 70, 1.5, 350, "weapon", WeKE.SHORTSWORD.value, 7, SkE.SHORT_BLADE.value, ExE.AMATEUR.value),
            WpnE.STEEL_SABER.value: (MeleeWeapon, 80, 2.0, 400, "weapon", WeKE.SABER.value, 8, SkE.LONG_BLADE.value, ExE.AMATEUR.value),
            WpnE.STEEL_LONGSWORD.value: (MeleeWeapon, 90, 2.5, 450, "weapon", WeKE.LONGSWORD.value, 9, SkE.LONG_BLADE.value, ExE.AMATEUR.value),
            WpnE.STEEL_WAR_AXE.value: (MeleeWeapon, 100, 3.0, 500, "weapon", WeKE.WAR_AXE, 10, SkE.AXE.value, ExE.AMATEUR.value),

            WpnE.SILVER_SABER.value: (MeleeWeapon, 100, 2.5, 500, "weapon", WeKE.SABER.value, 10, SkE.LONG_BLADE.value, ExE.ADEPT.value),
            WpnE.SILVER_LONGSWORD.value: (MeleeWeapon, 110, 3.0, 550, "weapon", WeKE.LONGSWORD.value, 11, SkE.LONG_BLADE.value, ExE.ADEPT.value),
            WpnE.SILVER_SHORTSWORD.value: (MeleeWeapon, 90, 2.0, 450, "weapon", WeKE.SHORTSWORD.value, 9, SkE.SHORT_BLADE.value, ExE.ADEPT.value),
            WpnE.SILVER_SABER.value: (MeleeWeapon, 100, 2.5, 500, "weapon", WeKE.SABER.value, 10, SkE.LONG_BLADE.value, ExE.ADEPT.value),
            WpnE.SILVER_LONGSWORD.value: (MeleeWeapon, 110, 3.0, 550, "weapon", WeKE.LONGSWORD.value, 11, SkE.LONG_BLADE.value, ExE.ADEPT.value),
            WpnE.SILVER_SHORTSWORD.value: (MeleeWeapon, 90, 2.0, 450, "weapon", WeKE.SHORTSWORD.value, 9, SkE.SHORT_BLADE.value, ExE.ADEPT.value),
            WpnE.SILVER_DAGGER.value: (MeleeWeapon, 70, 1.5, 350, "weapon", WeKE.DAGGER.value, 7, SkE.SHORT_BLADE.value, ExE.ADEPT.value),
            WpnE.SILVER_MACE.value: (MeleeWeapon, 120, 3.5, 600, "weapon", WeKE.MACE.value, 12, SkE.BLUNT_WEAPON.value, ExE.ADEPT.value),
            WpnE.SILVER_WARHAMMER.value: (MeleeWeapon, 130, 4.0, 650, "weapon", WeKE.WARHAMMER.value, 13, SkE.BLUNT_WEAPON.value, ExE.ADEPT.value),
            WpnE.SILVER_STAFF.value: (MeleeWeapon, 100, 2.5, 500, "weapon", WeKE.STAFF.value, 10, SkE.BLUNT_WEAPON.value, ExE.ADEPT.value),
            WpnE.SILVER_SPEAR.value: (MeleeWeapon, 110, 3.0, 550, "weapon", WeKE.SPEAR, 11, SkE.SPEAR.value, ExE.ADEPT.value),
            WpnE.SILVER_HALBERD.value: (MeleeWeapon, 120, 3.5, 600, "weapon", WeKE.HALBERD, 12, SkE.SPEAR.value, ExE.ADEPT.value),
            WpnE.SILVER_BOW.value: (RangedWeapon, 110, 2.5, 550, "weapon", WeKE.BOW, 11, SkE.MARKSMAN.value, ExE.ADEPT.value),
            WpnE.SILVER_CROSSBOW.value: (RangedWeapon, 120, 3.0, 600, "weapon", WeKE.CROSSBOW, 12, SkE.MARKSMAN.value, ExE.ADEPT.value),
            WpnE.SILVER_BATTLE_AXE.value: (MeleeWeapon, 130, 4.0, 650, "weapon", WeKE.BATTLE_AXE, 13, SkE.AXE.value, ExE.ADEPT.value),
            WpnE.SILVER_WAR_AXE.value: (MeleeWeapon, 120, 3.5, 600, "weapon", WeKE.WAR_AXE, 12, SkE.AXE.value, ExE.ADEPT.value),

            WpnE.DWARVEN_LONGSWORD.value: (MeleeWeapon, 130, 3.5, 650, "weapon", WeKE.LONGSWORD.value, 13, SkE.LONG_BLADE.value, ExE.EXPERT.value),
            WpnE.DWARVEN_SABER.value: (MeleeWeapon, 120, 3.0, 600, "weapon", WeKE.SABER.value, 12, SkE.LONG_BLADE.value, ExE.EXPERT.value),
            WpnE.DWARVEN_LONGSWORD.value: (MeleeWeapon, 130, 3.5, 650, "weapon", WeKE.LONGSWORD.value, 13, SkE.LONG_BLADE.value, ExE.EXPERT.value),
            WpnE.DWARVEN_SHORTSWORD.value: (MeleeWeapon, 110, 2.5, 550, "weapon", WeKE.SHORTSWORD.value, 11, SkE.SHORT_BLADE.value, ExE.EXPERT.value),
            WpnE.DWARVEN_DAGGER.value: (MeleeWeapon, 90, 2.0, 450, "weapon", WeKE.DAGGER.value, 9, SkE.SHORT_BLADE.value, ExE.EXPERT.value),
            WpnE.DWARVEN_MACE.value: (MeleeWeapon, 140, 4.0, 700, "weapon", WeKE.MACE.value, 14, SkE.BLUNT_WEAPON.value, ExE.EXPERT.value),
            WpnE.DWARVEN_WARHAMMER.value: (MeleeWeapon, 150, 4.5, 750, "weapon", WeKE.WARHAMMER.value, 15, SkE.BLUNT_WEAPON.value, ExE.EXPERT.value),
            WpnE.DWARVEN_STAFF.value: (MeleeWeapon, 120, 3.0, 600, "weapon", WeKE.STAFF.value, 12, SkE.BLUNT_WEAPON.value, ExE.EXPERT.value),
            WpnE.DWARVEN_SPEAR.value: (MeleeWeapon, 130, 3.5, 650, "weapon", WeKE.SPEAR, 13, SkE.SPEAR.value, ExE.EXPERT.value),
            WpnE.DWARVEN_HALBERD.value: (MeleeWeapon, 140, 4.0, 700, "weapon", WeKE.HALBERD, 14, SkE.SPEAR.value, ExE.EXPERT.value),
            WpnE.DWARVEN_BOW.value: (RangedWeapon, 130, 3.0, 650, "weapon", WeKE.BOW, 13, SkE.MARKSMAN.value, ExE.EXPERT.value),
            WpnE.DWARVEN_CROSSBOW.value: (RangedWeapon, 140, 3.5, 700, "weapon", WeKE.CROSSBOW, 14, SkE.MARKSMAN.value, ExE.EXPERT.value),
            WpnE.DWARVEN_BATTLE_AXE.value: (MeleeWeapon, 150, 4.5, 750, "weapon", WeKE.BATTLE_AXE, 15, SkE.AXE.value, ExE.EXPERT.value),
            WpnE.DWARVEN_WAR_AXE.value: (MeleeWeapon, 140, 4.0, 700, "weapon", WeKE.WAR_AXE, 14, SkE.AXE.value, ExE.EXPERT.value),
            WpnE.DWARVEN_SABER.value: (MeleeWeapon, 120, 3.0, 600, "weapon", WeKE.SABER.value, 12, SkE.LONG_BLADE.value, ExE.EXPERT.value),

            WpnE.GLASS_LONGSWORD.value: (MeleeWeapon, 150, 4.0, 750, "weapon", WeKE.LONGSWORD.value, 15, SkE.LONG_BLADE.value, ExE.MASTER.value),
            WpnE.GLASS_SABER.value: (MeleeWeapon, 140, 3.5, 700, "weapon", WeKE.SABER.value, 14, SkE.LONG_BLADE.value, ExE.MASTER.value),
            WpnE.GLASS_LONGSWORD.value: (MeleeWeapon, 150, 4.0, 750, "weapon", WeKE.LONGSWORD.value, 15, SkE.LONG_BLADE.value, ExE.MASTER.value),
            WpnE.GLASS_SHORTSWORD.value: (MeleeWeapon, 130, 3.0, 650, "weapon", WeKE.SHORTSWORD.value, 13, SkE.SHORT_BLADE.value, ExE.MASTER.value),
            WpnE.GLASS_DAGGER.value: (MeleeWeapon, 110, 2.5, 550, "weapon", WeKE.DAGGER.value, 11, SkE.SHORT_BLADE.value, ExE.MASTER.value),
            WpnE.GLASS_MACE.value: (MeleeWeapon, 160, 4.5, 800, "weapon", WeKE.MACE.value, 16, SkE.BLUNT_WEAPON.value, ExE.MASTER.value),
            WpnE.GLASS_WARHAMMER.value: (MeleeWeapon, 170, 5.0, 850, "weapon", WeKE.WARHAMMER.value, 17, SkE.BLUNT_WEAPON.value, ExE.MASTER.value),
            WpnE.GLASS_STAFF.value: (MeleeWeapon, 140, 3.5, 700, "weapon", WeKE.STAFF.value, 14, SkE.BLUNT_WEAPON.value, ExE.MASTER.value),
            WpnE.GLASS_SPEAR.value: (MeleeWeapon, 150, 4.0, 750, "weapon", WeKE.SPEAR, 15, SkE.SPEAR.value, ExE.MASTER.value),
            WpnE.GLASS_HALBERD.value: (MeleeWeapon, 160, 4.5, 800, "weapon", WeKE.HALBERD, 16, SkE.SPEAR.value, ExE.MASTER.value),
            WpnE.GLASS_BOW.value: (RangedWeapon, 150, 3.5, 750, "weapon", WeKE.BOW, 15, SkE.MARKSMAN.value, ExE.MASTER.value),
            WpnE.GLASS_CROSSBOW.value: (RangedWeapon, 160, 4.0, 800, "weapon", WeKE.CROSSBOW, 16, SkE.MARKSMAN.value, ExE.MASTER.value),
            WpnE.GLASS_BATTLE_AXE.value: (MeleeWeapon, 170, 5.0, 850, "weapon", WeKE.BATTLE_AXE, 17, SkE.AXE.value, ExE.MASTER.value),
            WpnE.GLASS_SABER.value: (MeleeWeapon, 140, 3.5, 700, "weapon", WeKE.SABER.value, 14, SkE.LONG_BLADE.value, ExE.MASTER.value),

            WpnE.EBONY_SABER.value: (MeleeWeapon, 160, 4.0, 800, "weapon", WeKE.SABER.value, 16, SkE.LONG_BLADE.value, ExE.MASTER.value),
            WpnE.EBONY_LONGSWORD.value: (MeleeWeapon, 170, 4.5, 850, "weapon", WeKE.LONGSWORD.value, 17, SkE.LONG_BLADE.value, ExE.MASTER.value),
            WpnE.EBONY_SABER.value: (MeleeWeapon, 160, 4.0, 800, "weapon", WeKE.SABER.value, 16, SkE.LONG_BLADE.value, ExE.MASTER.value),
            WpnE.EBONY_LONGSWORD.value: (MeleeWeapon, 170, 4.5, 850, "weapon", WeKE.LONGSWORD.value, 17, SkE.LONG_BLADE.value, ExE.MASTER.value),
            WpnE.EBONY_SHORTSWORD.value: (MeleeWeapon, 150, 3.5, 750, "weapon", WeKE.SHORTSWORD.value, 15, SkE.SHORT_BLADE.value, ExE.MASTER.value),
            WpnE.EBONY_DAGGER.value: (MeleeWeapon, 130, 3.0, 650, "weapon", WeKE.DAGGER.value, 13, SkE.SHORT_BLADE.value, ExE.MASTER.value),
            WpnE.EBONY_MACE.value: (MeleeWeapon, 180, 5.0, 900, "weapon", WeKE.MACE.value, 18, SkE.BLUNT_WEAPON.value, ExE.MASTER.value),
            WpnE.EBONY_WARHAMMER.value: (MeleeWeapon, 190, 5.5, 950, "weapon", WeKE.WARHAMMER.value, 19, SkE.BLUNT_WEAPON.value, ExE.MASTER.value),
            WpnE.EBONY_STAFF.value: (MeleeWeapon, 160, 4.0, 800, "weapon", WeKE.STAFF.value, 16, SkE.BLUNT_WEAPON.value, ExE.MASTER.value),
            WpnE.EBONY_SPEAR.value: (MeleeWeapon, 170, 4.5, 850, "weapon", WeKE.SPEAR, 17, SkE.SPEAR.value, ExE.MASTER.value),
            WpnE.EBONY_HALBERD.value: (MeleeWeapon, 180, 5.0, 900, "weapon", WeKE.HALBERD, 18, SkE.SPEAR.value, ExE.MASTER.value),
            WpnE.EBONY_BOW.value: (RangedWeapon, 170, 4.0, 850, "weapon", WeKE.BOW, 17, SkE.MARKSMAN.value, ExE.MASTER.value),
            WpnE.EBONY_CROSSBOW.value: (RangedWeapon, 180, 4.5, 900, "weapon", WeKE.CROSSBOW, 18, SkE.MARKSMAN.value, ExE.MASTER.value),
            WpnE.EBONY_BATTLE_AXE.value: (MeleeWeapon, 190, 5.5, 950, "weapon", WeKE.BATTLE_AXE, 19, SkE.AXE.value, ExE.MASTER.value),

            WpnE.DAEDRIC_SABER.value: (MeleeWeapon, 180, 4.5, 900, "weapon", WeKE.SABER.value, 18, SkE.LONG_BLADE.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_LONGSWORD.value: (MeleeWeapon, 190, 5.0, 950, "weapon", WeKE.LONGSWORD.value, 19, SkE.LONG_BLADE.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_SABER.value: (MeleeWeapon, 180, 4.5, 900, "weapon", WeKE.SABER.value, 18, SkE.LONG_BLADE.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_LONGSWORD.value: (MeleeWeapon, 190, 5.0, 950, "weapon", WeKE.LONGSWORD.value, 19, SkE.LONG_BLADE.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_SHORTSWORD.value: (MeleeWeapon, 170, 4.0, 850, "weapon", WeKE.SHORTSWORD.value, 17, SkE.SHORT_BLADE.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_DAGGER.value: (MeleeWeapon, 150, 3.5, 750, "weapon", WeKE.DAGGER.value, 15, SkE.SHORT_BLADE.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_MACE.value: (MeleeWeapon, 200, 5.5, 1000, "weapon", WeKE.MACE.value, 20, SkE.BLUNT_WEAPON.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_WARHAMMER.value: (MeleeWeapon, 210, 6.0, 1050, "weapon", WeKE.WARHAMMER.value, 21, SkE.BLUNT_WEAPON.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_STAFF.value: (MeleeWeapon, 180, 4.5, 900, "weapon", WeKE.STAFF.value, 18, SkE.BLUNT_WEAPON.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_SPEAR.value: (MeleeWeapon, 190, 5.0, 950, "weapon", WeKE.SPEAR, 19, SkE.SPEAR.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_HALBERD.value: (MeleeWeapon, 200, 5.5, 1000, "weapon", WeKE.HALBERD, 20, SkE.SPEAR.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_BOW.value: (RangedWeapon, 190, 4.5, 950, "weapon", WeKE.BOW, 19, SkE.MARKSMAN.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_CROSSBOW.value: (RangedWeapon, 200, 5.0, 1000, "weapon", WeKE.CROSSBOW, 20, SkE.MARKSMAN.value, ExE.LEGEND.value),
            WpnE.DAEDRIC_BATTLE_AXE.value: (MeleeWeapon, 210, 6.0, 1050, "weapon", WeKE.BATTLE_AXE, 21, SkE.AXE.value, ExE.LEGEND.value),
        }
        
    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given weapon.
        The method takes one parameter: the name of the weapon.
        The item_name parameter should be a string representing the name of the weapon.
        The method returns a dictionary with keys: item, base_price, base_weight, durability, category, subcategory, base_attack, skill, experience.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.weapon.MeleeWeapon'>,
            'base_price': 160,
            'base_weight': 3.0,
            'durability': 700,
            'category': 'weapon',
            'subcategory': 'sword',
            'base_attack': 10,
            'skill': 'long_blade',
            'experience': 'EXPERT'
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Weapon name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._cols.keys(), self._config[item_name])}
