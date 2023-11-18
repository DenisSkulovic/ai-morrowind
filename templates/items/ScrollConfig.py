from enum.items.ScrollEnum import ScrollEnum as ScrE
from classes.items.consumable.Scroll import Scroll
from enum.EffectEnum import EffectEnum as E


class ScrollConfig:
    """
    This class represents the mapping of scroll items to their details.
    Each scroll is represented by a tuple of seven values: item, base_price, base_weight, effect, magnitude, duration, effect_range.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._index = {"item": 0, "base_price": 1, "base_weight": 2, "effect": 3, "magnitude": 4, "duration": 5, "effect_range": 6}
        self._config = {
            ScrE.FIREBALL.value: (Scroll, 100, 0.1, E.FIRE_DAMAGE, 20, None, "distance"),
            ScrE.LEVITATION.value: (Scroll, 150, 0.1, E.LEVITATE, 0, 60, "self"),
            ScrE.CHAMELEON_SPELL.value: (Scroll, 150, 0.1, E.CHAMELEON, 0, 30, "self"),
            ScrE.FROSTBITE.value: (Scroll, 100, 0.1, E.FROST_DAMAGE, 20, None, "distance"),
            ScrE.SUMMON_SKELETON.value: (Scroll, 200, 0.1, E.SUMMON_CREATURE, 0, 60, "self"),
            ScrE.COMMAND_CREATURE.value: (Scroll, 200, 0.1, E.COMMAND_CREATURE, 0, 60, "touch"),
            ScrE.SHIELD.value: (Scroll, 150, 0.1, E.SHIELD, 0, 60, "self"),
            ScrE.HEAL.value: (Scroll, 100, 0.1, E.RESTORE_HEALTH, 25, None, "self"),
            ScrE.ABSORB_HEALTH.value: (Scroll, 200, 0.1, E.ABSORB_HEALTH, 15, None, "touch")
        }

    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given scroll.
        The method takes one parameter: the name of the scroll.
        The item_name parameter should be a string representing the name of the scroll.
        The method returns a dictionary with keys: item, base_price, base_weight, effect, magnitude, duration, effect_range.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.consumable.Scroll'>,
            'base_price': 100,
            'base_weight': 0.1,
            'effect': <EffectEnum.RESTORE_HEALTH: 1>,
            'magnitude': 25,
            'duration': None,
            'effect_range': 'self'
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Scroll name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._index.keys(), self._config[item_name])}
