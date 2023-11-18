from enum.items.ToolEnum import ToolEnum as ToolE
from classes.items.Lockpick import Lockpick
from classes.items.RepairTool import RepairTool
from classes.items.Probe import Probe


class ToolConfig:
    """
    This class represents the mapping of tool items to their details.
    Each tool is represented by a tuple of three values: item, base_price, base_weight.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._cols = {"item": 0, "base_price": 1, "base_weight": 2}
        self._config = {
            ToolE.APPRENTICE_LOCKPICK.value: (Lockpick, 25, 0.1),  # Apprentice's Lockpick is very light
            ToolE.JOURNEYMAN_LOCKPICK.value: (Lockpick, 50, 0.1),  # Journeyman's Lockpick is very light
            ToolE.MASTER_LOCKPICK.value: (Lockpick, 100, 0.1),  # Master's Lockpick is very light
            ToolE.GRANDMASTER_LOCKPICK.value: (Lockpick, 200, 0.1),  # Grandmaster's Lockpick is very light

            ToolE.APPRENTICE_PROBE.value: (Probe, 30, 0.1),  # Apprentice's Probe is used to disarm traps
            ToolE.JOURNEYMAN_PROBE.value: (Probe, 60, 0.1),  # Journeyman's Probe is used to disarm traps
            ToolE.MASTER_PROBE.value: (Probe, 120, 0.1),  # Master's Probe is used to disarm traps
            ToolE.GRANDMASTER_PROBE.value: (Probe, 240, 0.1),  # Grandmaster's Probe is used to disarm traps
            
            ToolE.APPRENTICE_ARMORERS_HAMMER.value: (RepairTool, 75, 2.0),  # Apprentice's Armorer's Hammer is used to repair armor
            ToolE.JOURNEYMAN_ARMORERS_HAMMER.value: (RepairTool, 150, 2.0),  # Journeyman's Armorer's Hammer is used to repair armor
            ToolE.MASTER_ARMORERS_HAMMER.value: (RepairTool, 300, 2.0),  # Master's Armorer's Hammer is used to repair armor
            ToolE.GRANDMASTER_ARMORERS_HAMMER.value: (RepairTool, 600, 2.0),  # Grandmaster's Armorer's Hammer is used to repair armor
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
        return {key: value for key, value in zip(self._cols.keys(), self._config[item_name])}
