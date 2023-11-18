from classes.items.SoulGem import SoulGem
from enum.items.SoulGemEnum import SoulGemEnum as SGemE


class SoulGemConfig:
    """
    This class represents the mapping of soul gem items to their details.
    Each soul gem is represented by a tuple of three values: item, base_price, base_weight.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._cols = {"item": 0, "base_price": 1, "base_weight": 2}
        self._config = {
            SGemE.PETTY_SOUL_GEM.value: (SoulGem, 40, 0.5),  # Petty Soul Gem
            SGemE.LESSER_SOUL_GEM.value: (SoulGem, 150, 0.5),  # Lesser Soul Gem
            SGemE.COMMON_SOUL_GEM.value: (SoulGem, 400, 0.5),  # Common Soul Gem
            SGemE.GREATER_SOUL_GEM.value: (SoulGem, 1200, 0.5),  # Greater Soul Gem
            SGemE.GRAND_SOUL_GEM.value: (SoulGem, 3500, 0.5),  # Grand Soul Gem
            SGemE.AZURAS_STAR.value: (SoulGem, 5000, 0.5),  # Azura's Star, unique soul gem
        }
        
    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given soul gem item.
        The method takes one parameter: the name of the soul gem item.
        The item_name parameter should be a string representing the name of the soul gem item.
        The method returns a dictionary with keys: item, base_price, base_weight.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.SoulGem'>,
            'base_price': 100,
            'base_weight': None,
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Soul gem item name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._cols.keys(), self._config[item_name])}
