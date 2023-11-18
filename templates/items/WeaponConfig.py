from enum.items.WeaponEnum import WeaponEnum as WpnE
from classes.items.weapon.MeleeWeapon import MeleeWeapon
from classes.items.weapon.RangedWeapon import RangedWeapon


class WeaponConfig:
    """
    This class represents the mapping of weapon items to their details.
    Each weapon is represented by a tuple of nine values: item, base_price, base_weight, durability, category, subcategory, base_attack, skill.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._index = {"item": 0, "base_price": 1, "base_weight": 2, "durability": 3, "category": 4, "subcategory": 5, "base_attack": 6, "skill": 7}
        self._config = {
            WpnE.IRON_SABER.value: (MeleeWeapon, 60, 1.5, 300, "weapon", "saber", 6, "long_blade"),
            WpnE.STEEL_SABER.value: (MeleeWeapon, 80, 2.0, 400, "weapon", "saber", 8, "long_blade"),
            WpnE.SILVER_SABER.value: (MeleeWeapon, 100, 2.5, 500, "weapon", "saber", 10, "long_blade"),
            WpnE.DWARVEN_SABER.value: (MeleeWeapon, 120, 3.0, 600, "weapon", "saber", 12, "long_blade"),
            WpnE.GLASS_SABER.value: (MeleeWeapon, 140, 3.5, 700, "weapon", "saber", 14, "long_blade"),
            WpnE.EBONY_SABER.value: (MeleeWeapon, 160, 4.0, 800, "weapon", "saber", 16, "long_blade"),
            WpnE.DAEDRIC_SABER.value: (MeleeWeapon, 180, 4.5, 900, "weapon", "saber", 18, "long_blade"),
            WpnE.IRON_LONGSWORD.value: (MeleeWeapon, 70, 2.0, 350, "weapon", "longsword", 7, "long_blade"),
            WpnE.STEEL_LONGSWORD.value: (MeleeWeapon, 90, 2.5, 450, "weapon", "longsword", 9, "long_blade"),
            WpnE.SILVER_LONGSWORD.value: (MeleeWeapon, 110, 3.0, 550, "weapon", "longsword", 11, "long_blade"),
            WpnE.DWARVEN_LONGSWORD.value: (MeleeWeapon, 130, 3.5, 650, "weapon", "longsword", 13, "long_blade"),
            WpnE.GLASS_LONGSWORD.value: (MeleeWeapon, 150, 4.0, 750, "weapon", "longsword", 15, "long_blade"),
            WpnE.EBONY_LONGSWORD.value: (MeleeWeapon, 170, 4.5, 850, "weapon", "longsword", 17, "long_blade"),
            WpnE.DAEDRIC_LONGSWORD.value: (MeleeWeapon, 190, 5.0, 950, "weapon", "longsword", 19, "long_blade"),
            WpnE.IRON_SHORTSWORD.value: (MeleeWeapon, 50, 1.0, 250, "weapon", "shortsword", 5, "short_blade"),
            WpnE.STEEL_SHORTSWORD.value: (MeleeWeapon, 70, 1.5, 350, "weapon", "shortsword", 7, "short_blade"),
            WpnE.SILVER_SHORTSWORD.value: (MeleeWeapon, 90, 2.0, 450, "weapon", "shortsword", 9, "short_blade"),
            WpnE.DWARVEN_SHORTSWORD.value: (MeleeWeapon, 110, 2.5, 550, "weapon", "shortsword", 11, "short_blade"),
            WpnE.GLASS_SHORTSWORD.value: (MeleeWeapon, 130, 3.0, 650, "weapon", "shortsword", 13, "short_blade"),
            WpnE.EBONY_SHORTSWORD.value: (MeleeWeapon, 150, 3.5, 750, "weapon", "shortsword", 15, "short_blade"),
            WpnE.DAEDRIC_SHORTSWORD.value: (MeleeWeapon, 170, 4.0, 850, "weapon", "shortsword", 17, "short_blade"),
            WpnE.IRON_DAGGER.value: (MeleeWeapon, 30, 0.5, 150, "weapon", "dagger", 3, "short_blade"),
            WpnE.STEEL_DAGGER.value: (MeleeWeapon, 50, 1.0, 250, "weapon", "dagger", 5, "short_blade"),
            WpnE.SILVER_DAGGER.value: (MeleeWeapon, 70, 1.5, 350, "weapon", "dagger", 7, "short_blade"),
            WpnE.DWARVEN_DAGGER.value: (MeleeWeapon, 90, 2.0, 450, "weapon", "dagger", 9, "short_blade"),
            WpnE.GLASS_DAGGER.value: (MeleeWeapon, 110, 2.5, 550, "weapon", "dagger", 11, "short_blade"),
            WpnE.EBONY_DAGGER.value: (MeleeWeapon, 130, 3.0, 650, "weapon", "dagger", 13, "short_blade"),
            WpnE.DAEDRIC_DAGGER.value: (MeleeWeapon, 150, 3.5, 750, "weapon", "dagger", 15, "short_blade"),
            WpnE.IRON_MACE.value: (MeleeWeapon, 80, 2.5, 400, "weapon", "mace", 8, "blunt_weapon"),
            WpnE.STEEL_MACE.value: (MeleeWeapon, 100, 3.0, 500, "weapon", "mace", 10, "blunt_weapon"),
            WpnE.SILVER_MACE.value: (MeleeWeapon, 120, 3.5, 600, "weapon", "mace", 12, "blunt_weapon"),
            WpnE.DWARVEN_MACE.value: (MeleeWeapon, 140, 4.0, 700, "weapon", "mace", 14, "blunt_weapon"),
            WpnE.GLASS_MACE.value: (MeleeWeapon, 160, 4.5, 800, "weapon", "mace", 16, "blunt_weapon"),
            WpnE.EBONY_MACE.value: (MeleeWeapon, 180, 5.0, 900, "weapon", "mace", 18, "blunt_weapon"),
            WpnE.DAEDRIC_MACE.value: (MeleeWeapon, 200, 5.5, 1000, "weapon", "mace", 20, "blunt_weapon"),
            WpnE.IRON_WARHAMMER.value: (MeleeWeapon, 90, 3.0, 450, "weapon", "warhammer", 9, "blunt_weapon"),
            WpnE.STEEL_WARHAMMER.value: (MeleeWeapon, 110, 3.5, 550, "weapon", "warhammer", 11, "blunt_weapon"),
            WpnE.SILVER_WARHAMMER.value: (MeleeWeapon, 130, 4.0, 650, "weapon", "warhammer", 13, "blunt_weapon"),
            WpnE.DWARVEN_WARHAMMER.value: (MeleeWeapon, 150, 4.5, 750, "weapon", "warhammer", 15, "blunt_weapon"),
            WpnE.GLASS_WARHAMMER.value: (MeleeWeapon, 170, 5.0, 850, "weapon", "warhammer", 17, "blunt_weapon"),
            WpnE.EBONY_WARHAMMER.value: (MeleeWeapon, 190, 5.5, 950, "weapon", "warhammer", 19, "blunt_weapon"),
            WpnE.DAEDRIC_WARHAMMER.value: (MeleeWeapon, 210, 6.0, 1050, "weapon", "warhammer", 21, "blunt_weapon"),
            WpnE.IRON_STAFF.value: (MeleeWeapon, 60, 1.5, 300, "weapon", "staff", 6, "blunt_weapon"),
            WpnE.STEEL_STAFF.value: (MeleeWeapon, 80, 2.0, 400, "weapon", "staff", 8, "blunt_weapon"),
            WpnE.SILVER_STAFF.value: (MeleeWeapon, 100, 2.5, 500, "weapon", "staff", 10, "blunt_weapon"),
            WpnE.DWARVEN_STAFF.value: (MeleeWeapon, 120, 3.0, 600, "weapon", "staff", 12, "blunt_weapon"),
            WpnE.GLASS_STAFF.value: (MeleeWeapon, 140, 3.5, 700, "weapon", "staff", 14, "blunt_weapon"),
            WpnE.EBONY_STAFF.value: (MeleeWeapon, 160, 4.0, 800, "weapon", "staff", 16, "blunt_weapon"),
            WpnE.DAEDRIC_STAFF.value: (MeleeWeapon, 180, 4.5, 900, "weapon", "staff", 18, "blunt_weapon"),
            WpnE.IRON_SPEAR.value: (MeleeWeapon, 70, 2.0, 350, "weapon", "spear", 7, "spear"),
            WpnE.STEEL_SPEAR.value: (MeleeWeapon, 90, 2.5, 450, "weapon", "spear", 9, "spear"),
            WpnE.SILVER_SPEAR.value: (MeleeWeapon, 110, 3.0, 550, "weapon", "spear", 11, "spear"),
            WpnE.DWARVEN_SPEAR.value: (MeleeWeapon, 130, 3.5, 650, "weapon", "spear", 13, "spear"),
            WpnE.GLASS_SPEAR.value: (MeleeWeapon, 150, 4.0, 750, "weapon", "spear", 15, "spear"),
            WpnE.EBONY_SPEAR.value: (MeleeWeapon, 170, 4.5, 850, "weapon", "spear", 17, "spear"),
            WpnE.DAEDRIC_SPEAR.value: (MeleeWeapon, 190, 5.0, 950, "weapon", "spear", 19, "spear"),
            WpnE.IRON_HALBERD.value: (MeleeWeapon, 80, 2.5, 400, "weapon", "halberd", 8, "spear"),
            WpnE.STEEL_HALBERD.value: (MeleeWeapon, 100, 3.0, 500, "weapon", "halberd", 10, "spear"),
            WpnE.SILVER_HALBERD.value: (MeleeWeapon, 120, 3.5, 600, "weapon", "halberd", 12, "spear"),
            WpnE.DWARVEN_HALBERD.value: (MeleeWeapon, 140, 4.0, 700, "weapon", "halberd", 14, "spear"),
            WpnE.GLASS_HALBERD.value: (MeleeWeapon, 160, 4.5, 800, "weapon", "halberd", 16, "spear"),
            WpnE.EBONY_HALBERD.value: (MeleeWeapon, 180, 5.0, 900, "weapon", "halberd", 18, "spear"),
            WpnE.DAEDRIC_HALBERD.value: (MeleeWeapon, 200, 5.5, 1000, "weapon", "halberd", 20, "spear"),
            WpnE.IRON_BOW.value: (RangedWeapon, 70, 1.5, 350, "weapon", "bow", 7, "marksman"),
            WpnE.STEEL_BOW.value: (RangedWeapon, 90, 2.0, 450, "weapon", "bow", 9, "marksman"),
            WpnE.SILVER_BOW.value: (RangedWeapon, 110, 2.5, 550, "weapon", "bow", 11, "marksman"),
            WpnE.DWARVEN_BOW.value: (RangedWeapon, 130, 3.0, 650, "weapon", "bow", 13, "marksman"),
            WpnE.GLASS_BOW.value: (RangedWeapon, 150, 3.5, 750, "weapon", "bow", 15, "marksman"),
            WpnE.EBONY_BOW.value: (RangedWeapon, 170, 4.0, 850, "weapon", "bow", 17, "marksman"),
            WpnE.DAEDRIC_BOW.value: (RangedWeapon, 190, 4.5, 950, "weapon", "bow", 19, "marksman"),
            WpnE.IRON_CROSSBOW.value: (RangedWeapon, 80, 2.0, 400, "weapon", "crossbow", 8, "marksman"),
            WpnE.STEEL_CROSSBOW.value: (RangedWeapon, 100, 2.5, 500, "weapon", "crossbow", 10, "marksman"),
            WpnE.SILVER_CROSSBOW.value: (RangedWeapon, 120, 3.0, 600, "weapon", "crossbow", 12, "marksman"),
            WpnE.DWARVEN_CROSSBOW.value: (RangedWeapon, 140, 3.5, 700, "weapon", "crossbow", 14, "marksman"),
            WpnE.GLASS_CROSSBOW.value: (RangedWeapon, 160, 4.0, 800, "weapon", "crossbow", 16, "marksman"),
            WpnE.EBONY_CROSSBOW.value: (RangedWeapon, 180, 4.5, 900, "weapon", "crossbow", 18, "marksman"),
            WpnE.DAEDRIC_CROSSBOW.value: (RangedWeapon, 200, 5.0, 1000, "weapon", "crossbow", 20, "marksman"),
            WpnE.IRON_BATTLE_AXE.value: (MeleeWeapon, 90, 3.0, 450, "weapon", "battle_axe", 9, "axe"),
            WpnE.STEEL_BATTLE_AXE.value: (MeleeWeapon, 110, 3.5, 550, "weapon", "battle_axe", 11, "axe"),
            WpnE.SILVER_BATTLE_AXE.value: (MeleeWeapon, 130, 4.0, 650, "weapon", "battle_axe", 13, "axe"),
            WpnE.DWARVEN_BATTLE_AXE.value: (MeleeWeapon, 150, 4.5, 750, "weapon", "battle_axe", 15, "axe"),
            WpnE.GLASS_BATTLE_AXE.value: (MeleeWeapon, 170, 5.0, 850, "weapon", "battle_axe", 17, "axe"),
            WpnE.EBONY_BATTLE_AXE.value: (MeleeWeapon, 190, 5.5, 950, "weapon", "battle_axe", 19, "axe"),
            WpnE.DAEDRIC_BATTLE_AXE.value: (MeleeWeapon, 210, 6.0, 1050, "weapon", "battle_axe", 21, "axe"),
            WpnE.IRON_WAR_AXE.value: (MeleeWeapon, 80, 2.5, 400, "weapon", "war_axe", 8, "axe"),
            WpnE.STEEL_WAR_AXE.value: (MeleeWeapon, 100, 3.0, 500, "weapon", "war_axe", 10, "axe"),
            WpnE.SILVER_WAR_AXE.value: (MeleeWeapon, 120, 3.5, 600, "weapon", "war_axe", 12, "axe"),
            WpnE.DWARVEN_WAR_AXE.value: (MeleeWeapon, 140, 4.0, 700, "weapon", "war_axe", 14, "axe"),
        }
        
    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given weapon.
        The method takes one parameter: the name of the weapon.
        The item_name parameter should be a string representing the name of the weapon.
        The method returns a dictionary with keys: item, base_price, base_weight, durability, category, subcategory, base_attack, skill.
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
            'skill': 'long_blade'
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Weapon name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._index.keys(), self._config[item_name])}
