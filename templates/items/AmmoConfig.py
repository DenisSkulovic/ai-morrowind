from classes.items.consumable.Arrow import Arrow
from enum.items.AmmoEnum import AmmoEnum as AmmoE



class AmmoConfig:
    """
    This class represents the mapping of ammo items to their details.
    Each ammo is represented by a tuple of seven values: item, base_price, base_weight, category, subcategory, base_attack.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._cols = {"item": 0, "base_price": 1, "base_weight": 2, "category": 3, "subcategory": 4, "base_attack": 5}
        self._config = {
            AmmoE.ARROW.value: (Arrow, 2, 0.1, "consumable", "arrow", 1),
            AmmoE.BOLT.value: (Arrow, 3, 0.1, "consumable", "bolt", 2),
        }
        
    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given ammo.
        The method takes one parameter: the name of the ammo.
        The item_name parameter should be a string representing the name of the ammo.
        The method returns a dictionary with keys: item, base_price, base_weight, category, subcategory, base_attack.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.consumable.Arrow'>,
            'base_price': 2,
            'base_weight': 0.1,
            'category': 'consumable',
            'subcategory': 'arrow',
            'base_attack': 1,
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Ammo name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._cols.keys(), self._config[item_name])}

