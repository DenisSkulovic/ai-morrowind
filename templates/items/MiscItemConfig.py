from classes.items.Item import Item
from enum.items.MiscItemEnum import MiscItemEnum as MiscE


class MiscItemConfig:
    """
    This class represents the mapping of misc items to their details.
    Each misc item is represented by a tuple of three values: item, base_price, base_weight.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._cols = {"item": 0, "base_price": 1, "base_weight": 2}
        self._config = {
            MiscE.DRAKE.value: (Item, 1, 0.01),
            MiscE.BROOM.value: (Item, 10, 1.0),
            MiscE.PAPER.value: (Item, 2, 0.01),
            MiscE.BUCKET.value: (Item, 5, 2.0),
            MiscE.CANDLE.value: (Item, 3, 0.5),
            MiscE.LANTERN.value: (Item, 20, 3.0),
            MiscE.PROBE.value: (Item, 60, 0.1),
            MiscE.SKULL.value: (Item, 100, 5.0),
            MiscE.TORCH.value: (Item, 5, 1.0),
            MiscE.TRAINING_DUMMY.value: (Item, 200, 10.0),
            MiscE.WEAPON_RACK.value: (Item, 500, 20.0),
        }
        
    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given misc item.
        The method takes one parameter: the name of the misc item.
        The item_name parameter should be a string representing the name of the misc item.
        The method returns a dictionary with keys: item, base_price, base_weight.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.Item'>,
            'base_price': 1,
            'base_weight': 0.01,
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Misc item name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._cols.keys(), self._config[item_name])}