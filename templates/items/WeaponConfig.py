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
            WpnE.LONG_SWORD.value: (MeleeWeapon, 160, 3.0, 700, "weapon", "sword", 10, "long_blade"),
            WpnE.SHORT_SWORD.value: (MeleeWeapon, 100, 2.0, 600, "weapon", "sword", 8, "short_blade"),
            WpnE.DAGGER.value: (MeleeWeapon, 40, 1.0, 300, "weapon", "dagger", 4, "short_blade"),
            WpnE.MACE.value: (MeleeWeapon, 150, 4.0, 800, "weapon", "mace", 12, "blunt_weapon"),
            WpnE.WARHAMMER.value: (MeleeWeapon, 200, 5.0, 850, "weapon", "hammer", 14, "blunt_weapon"),
            WpnE.STAFF.value: (MeleeWeapon, 80, 2.0, 500, "weapon", "staff", 6, "blunt_weapon"),
            WpnE.SPEAR.value: (MeleeWeapon, 120, 3.0, 750, "weapon", "spear", 9, "spear"),
            WpnE.HALBERD.value: (MeleeWeapon, 180, 4.0, 800, "weapon", "halberd", 11, "spear"),
            WpnE.BOW.value: (RangedWeapon, 150, 2.0, 400, "weapon", "bow", 10, "marksman"),
            WpnE.CROSSBOW.value: (RangedWeapon, 170, 2.0, 400, "weapon", "crossbow", 11, "marksman"),
            WpnE.BATTLE_AXE.value: (MeleeWeapon, 160, 5.0, 800, "weapon", "axe", 13, "axe"),
            WpnE.WAR_AXE.value: (MeleeWeapon, 140, 4.0, 700, "weapon", "axe", 11, "axe"),
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
