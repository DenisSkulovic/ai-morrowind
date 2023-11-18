from enum.items.AlchemyIngredientEnum import AlchemyIngredientEnum as AlchE
from enum.EffectEnum import EffectEnum as EfE
from classes.items.Item import Item

# TODO create a class for AlchemyIngredient

class AlchemyIngredientConfig:
    """
    This class represents the mapping of alchemy ingredient items to their details.
    Each alchemy ingredient is represented by a tuple of seven values: item, base_price, base_weight, effect_duration, effect1, effect2, effect3, effect4.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._cols = {"item": 0, "base_price": 1, "base_weight": 2, "effect_duration": 3, "effect1": 4, "effect2": 5, "effect3": 6, "effect4": 7}
        self._config = {
            AlchE.CRAB_MEAT.value: (Item, 1, 0.1, 30, EfE.RESTORE_FATIGUE.value, None, None, None),
            AlchE.DAEDRA_HEART.value: (Item, 200, 2.0, 60, EfE.RESTORE_HEALTH.value, EfE.FORTIFY_ENDURANCE.value, EfE.NIGHT_EYE.value, EfE.DRAIN_AGILITY.value),
            AlchE.KWAMA_CUTTLE.value: (Item, 2, 0.1, 30, EfE.RESIST_POISON.value, EfE.WATER_BREATHING.value, None, None),
            AlchE.SCAMP_SKIN.value: (Item, 10, 0.1, 45, EfE.DRAIN_PERSONALITY.value, EfE.RESTORE_HEALTH.value, None, None),
        }
        
    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given alchemy ingredient item.
        The method takes one parameter: the name of the alchemy ingredient item.
        The item_name parameter should be a string representing the name of the alchemy ingredient item.
        The method returns a dictionary with keys: item, base_price, base_weight, effect_duration, effect1, effect2, effect3, effect4.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.Item'>,
            'base_price': 200,
            'base_weight': 2.0,
            'effect_duration': 60,
            'effect1': 'restore_health',
            'effect2': 'fortify_endurance',
            'effect3': 'night_eye',
            'effect4': 'drain_agility',
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Alchemy ingredient item name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._cols.keys(), self._config[item_name])}
