from enum.items.ToolEnum import ToolEnum as ToolE
from classes.items.Item import Item

# TODO create a Tool class and use that instead of Item

class ToolConfig:
    """
    This class represents the mapping of tool items to their details.
    Each tool is represented by a tuple of three values: item, base_price, base_weight.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._index = {"item": 0, "base_price": 1, "base_weight": 2}
        self._config = {
            ToolE.LOCKPICK.value: (Item, 20, 0.1),  # Lockpick is very light
            ToolE.REPAIR_TOOL.value: (Item, 50, 1.0),  # Repair Tool is heavier than lockpick
            ToolE.PROBE.value: (Item, 60, 0.1),  # Probe is used to disarm traps
            ToolE.ARMORERS_HAMMER.value: (Item, 75, 2.0),  # Armorer's Hammer is used to repair armor
        }
        
    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given tool item.
        The method takes one parameter: the name of the tool item.
        The item_name parameter should be a string representing the name of the tool item.
        The method returns a dictionary with keys: item, base_price, base_weight.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.tool.Lockpick'>,
            'base_price': 20,
            'base_weight': 0.1,
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Tool item name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._index.keys(), self._config[item_name])}
