from enum.items.PotionEnum import PotionEnum as PotE
from classes.items.consumable.Potion import Potion
from enum.effect_enum import EffectEnum as E


class PotionConfig:
    """
    This class represents the mapping of potion items to their details.
    Each potion is represented by a tuple of seven values: item, base_price, base_weight, effect, magnitude, duration.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._index = {"item": 0, "base_price": 1, "base_weight": 2, "effect": 3, "magnitude": 4, "duration": 5}
        self._config = {
            PotE.RESTORE_HEALTH.value: (Potion, 50, 0.5, E.RESTORE_HEALTH, 25, None),
            PotE.FORTIFY_STRENGTH.value: (Potion, 75, 0.5, E.FORTIFY_STRENGTH, 10, 60),
            PotE.RESTORE_MAGICKA.value: (Potion, 50, 0.5, E.RESTORE_MAGICKA, 25, None),
            PotE.INVISIBILITY.value: (Potion, 100, 0.5, E.INVISIBILITY, 0, 30),
            PotE.FORTIFY_UNARMORED.value: (Potion, 75, 0.5, E.FORTIFY_UNARMORED, 10, 60),
            PotE.POISON.value: (Potion, 50, 0.5, E.POISON_DAMAGE, 15, None),
            PotE.SWIFT_SWIM.value: (Potion, 75, 0.5, E.FORTIFY_SPEED, 10, 60),
            PotE.FORTIFY_PERSONALITY.value: (Potion, 75, 0.5, E.FORTIFY_PERSONALITY, 10, 60),
            PotE.FORTIFY_ATTACK.value: (Potion, 75, 0.5, E.FORTIFY_ATTACK, 10, 60),
            PotE.FORTIFY_ENDURANCE.value: (Potion, 75, 0.5, E.FORTIFY_ENDURANCE, 10, 60),
            PotE.RESTORE_FATIGUE.value: (Potion, 50, 0.5, E.RESTORE_FATIGUE, 25, None),
            PotE.CHAMELEON.value: (Potion, 100, 0.5, E.CHAMELEON, 0, 30),
            PotE.FORTIFY_AGILITY.value: (Potion, 75, 0.5, E.FORTIFY_AGILITY, 10, 60),
            PotE.CURE_COMMON_DISEASE.value: (Potion, 50, 0.5, E.CURE_COMMON_DISEASE, 0, None),
            PotE.BLESSED_WATER.value: (Potion, 100, 0.5, E.TURN_UNDEAD, 20, None)
        }

    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given potion.
        The method takes one parameter: the name of the potion.
        The item_name parameter should be a string representing the name of the potion.
        The method returns a dictionary with keys: item, base_price, base_weight, effect, magnitude, duration.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.consumable.Potion'>,
            'base_price': 50,
            'base_weight': 0.5,
            'effect': <EffectEnum.RESTORE_HEALTH: 1>,
            'magnitude': 25,
            'duration': None
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Potion name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._index.keys(), self._config[item_name])}