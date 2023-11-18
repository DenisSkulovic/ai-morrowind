from enum.items.RingEnum import RingEnum as RingE
from classes.items.Ring import Ring
from enum.EffectEnum import EffectEnum as E

class RingEffectConfig:
    """
    This class represents the mapping of ring items to their details.
    Each ring is represented by a tuple of five values: item, base_price, base_weight, effect, magnitude.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._index = {"item": 0, "base_price": 1, "base_weight": 2, "effect": 3, "magnitude": 4}
        self._config = {
            RingE.REGENERATION_HEALTH.value: (Ring, 500, 0.1, E.REGENERATE_HEALTH, 25),
            RingE.REGENERATION_MAGICKA.value: (Ring, 500, 0.1, E.REGENERATE_MAGICKA, 25),
            RingE.REGENERATION_FATIGUE.value: (Ring, 500, 0.1, E.REGENERATE_FATIGUE, 25),
            RingE.FORTIFY_STRENGTH.value: (Ring, 500, 0.1, E.FORTIFY_STRENGTH, 10),
            RingE.FORTIFY_INTELLIGENCE.value: (Ring, 500, 0.1, E.FORTIFY_INTELLIGENCE, 10),
            RingE.FORTIFY_SPEED.value: (Ring, 500, 0.1, E.FORTIFY_SPEED, 10),
            RingE.FORTIFY_ENDURANCE.value: (Ring, 500, 0.1, E.FORTIFY_ENDURANCE, 10),
            RingE.FORTIFY_PERSONALITY.value: (Ring, 500, 0.1, E.FORTIFY_PERSONALITY, 10),
            RingE.FORTIFY_LUCK.value: (Ring, 500, 0.1, E.FORTIFY_LUCK, 10),
            RingE.FORTIFY_AGILITY.value: (Ring, 500, 0.1, E.FORTIFY_AGILITY, 10),
        }

    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given ring.
        The method takes one parameter: the name of the ring.
        The item_name parameter should be a string representing the name of the ring.
        The method returns a dictionary with keys: item, base_price, base_weight, effect, magnitude.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.consumable.Ring'>,
            'base_price': 500,
            'base_weight': 0.1,
            'effect': <EffectEnum.INVISIBILITY: 1>,
            'magnitude': 0,
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Ring name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._index.keys(), self._config[item_name])}


class RingSpellConfig:
    """
    This class represents the mapping of ring items to their details.
    Each ring is represented by a tuple of eight values: item, base_price, base_weight, spell, magnitude, duration, soul_charge, effect_range.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._index = {"item": 0, "base_price": 1, "base_weight": 2, "spell": 3, "magnitude": 4, "duration": 5, "soul_charge": 6, "effect_range": 7}
        self._config = {
            RingE.RESTORE_HEALTH.value: (Ring, 500, 0.1, E.RESTORE_HEALTH, 25, None, "self"),
            RingE.RESTORE_MAGICKA.value: (Ring, 500, 0.1, E.RESTORE_MAGICKA, 25, None, "self"),
            RingE.RESTORE_FATIGUE.value: (Ring, 500, 0.1, E.RESTORE_FATIGUE, 25, None, "self"),
            RingE.CHAMELEON.value: (Ring, 500, 0.1, E.CHAMELEON, 0, 60, 100, "self"),
            RingE.NIGHT_EYE.value: (Ring, 500, 0.1, E.NIGHT_EYE, 0, 60, 100, "self"),
            RingE.LEVITATION.value: (Ring, 500, 0.1, E.LEVITATE, 0, 60, 100, "self"),
            RingE.WATER_BREATHING.value: (Ring, 500, 0.1, E.WATER_BREATHING, 0, 60, 100, "self"),
            RingE.INVISIBILITY.value: (Ring, 500, 0.1, E.INVISIBILITY, 0, 30, 100, "self"),
            RingE.FIRESTORM.value: (Ring, 500, 0.1, E.FIRE_DAMAGE, 20, None, 100, "distance"),
            RingE.FROSTBITE.value: (Ring, 500, 0.1, E.FROST_DAMAGE, 20, None, 100, "distance"),
            RingE.SHOCKWAVE.value: (Ring, 500, 0.1, E.SHOCK_DAMAGE, 20, None, 100, "distance"),
            RingE.POISON_BLOOM.value: (Ring, 500, 0.1, E.POISON_DAMAGE, 15, None, 100, "distance"),
            RingE.TELEKINESIS.value: (Ring, 500, 0.1, E.TELEKINESIS, 0, 60, 100, "distance"),
        }

    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given ring.
        The method takes one parameter: the name of the ring.
        The item_name parameter should be a string representing the name of the ring.
        The method returns a dictionary with keys: item, base_price, base_weight, spell, magnitude, duration, soul_charge, effect_range.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.consumable.Ring'>,
            'base_price': 500,
            'base_weight': 0.1,
            'spell': <SpellEnum.FIRE_DAMAGE: 1>,
            'magnitude': 20,
            'duration': None,
            'soul_charge': 100,
            'effect_range': 'distance'
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Ring name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._index.keys(), self._config[item_name])}

