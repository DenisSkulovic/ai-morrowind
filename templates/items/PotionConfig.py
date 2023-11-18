from enum.items.PotionEnum import PotionEnum as PotE
from classes.items.consumable.Potion import Potion
from enum.EffectEnum import EffectEnum as E


class PotionConfig:
    """
    This class represents the mapping of potion items to their details.
    Each potion is represented by a tuple of seven values: item, base_price, base_weight, effect, magnitude, duration.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._cols = {"item": 0, "base_price": 1, "base_weight": 2, "effect": 3, "magnitude": 4, "duration": 5}
        self._config = {
            PotE.SMALL_RESTORE_HEALTH.value: (Potion, 30, 0.3, E.RESTORE_HEALTH, 15, None),
            PotE.MEDIUM_RESTORE_HEALTH.value: (Potion, 50, 0.5, E.RESTORE_HEALTH, 25, None),
            PotE.LARGE_RESTORE_HEALTH.value: (Potion, 70, 0.7, E.RESTORE_HEALTH, 35, None),
            PotE.SMALL_FORTIFY_STRENGTH.value: (Potion, 45, 0.3, E.FORTIFY_STRENGTH, 6, 60),
            PotE.MEDIUM_FORTIFY_STRENGTH.value: (Potion, 75, 0.5, E.FORTIFY_STRENGTH, 10, 60),
            PotE.LARGE_FORTIFY_STRENGTH.value: (Potion, 105, 0.7, E.FORTIFY_STRENGTH, 14, 60),
            PotE.SMALL_RESTORE_MAGICKA.value: (Potion, 30, 0.3, E.RESTORE_MAGICKA, 15, None),
            PotE.MEDIUM_RESTORE_MAGICKA.value: (Potion, 50, 0.5, E.RESTORE_MAGICKA, 25, None),
            PotE.LARGE_RESTORE_MAGICKA.value: (Potion, 70, 0.7, E.RESTORE_MAGICKA, 35, None),
            PotE.SMALL_INVISIBILITY.value: (Potion, 60, 0.3, E.INVISIBILITY, 0, 18),
            PotE.MEDIUM_INVISIBILITY.value: (Potion, 100, 0.5, E.INVISIBILITY, 0, 30),
            PotE.LARGE_INVISIBILITY.value: (Potion, 140, 0.7, E.INVISIBILITY, 0, 42),
            PotE.SMALL_FORTIFY_UNARMORED.value: (Potion, 45, 0.3, E.FORTIFY_UNARMORED, 6, 60),
            PotE.MEDIUM_FORTIFY_UNARMORED.value: (Potion, 75, 0.5, E.FORTIFY_UNARMORED, 10, 60),
            PotE.LARGE_FORTIFY_UNARMORED.value: (Potion, 105, 0.7, E.FORTIFY_UNARMORED, 14, 60),
            PotE.SMALL_POISON.value: (Potion, 30, 0.3, E.POISON_DAMAGE, 9, None),
            PotE.MEDIUM_POISON.value: (Potion, 50, 0.5, E.POISON_DAMAGE, 15, None),
            PotE.LARGE_POISON.value: (Potion, 70, 0.7, E.POISON_DAMAGE, 21, None),
            PotE.SMALL_SWIFT_SWIM.value: (Potion, 45, 0.3, E.FORTIFY_SPEED, 6, 60),
            PotE.MEDIUM_SWIFT_SWIM.value: (Potion, 75, 0.5, E.FORTIFY_SPEED, 10, 60),
            PotE.LARGE_SWIFT_SWIM.value: (Potion, 105, 0.7, E.FORTIFY_SPEED, 14, 60),
            PotE.SMALL_FORTIFY_PERSONALITY.value: (Potion, 45, 0.3, E.FORTIFY_PERSONALITY, 6, 60),
            PotE.MEDIUM_FORTIFY_PERSONALITY.value: (Potion, 75, 0.5, E.FORTIFY_PERSONALITY, 10, 60),
            PotE.LARGE_FORTIFY_PERSONALITY.value: (Potion, 105, 0.7, E.FORTIFY_PERSONALITY, 14, 60),
            PotE.SMALL_FORTIFY_ATTACK.value: (Potion, 45, 0.3, E.FORTIFY_ATTACK, 6, 60),
            PotE.MEDIUM_FORTIFY_ATTACK.value: (Potion, 75, 0.5, E.FORTIFY_ATTACK, 10, 60),
            PotE.LARGE_FORTIFY_ATTACK.value: (Potion, 105, 0.7, E.FORTIFY_ATTACK, 14, 60),
            PotE.SMALL_FORTIFY_ENDURANCE.value: (Potion, 45, 0.3, E.FORTIFY_ENDURANCE, 6, 60),
            PotE.MEDIUM_FORTIFY_ENDURANCE.value: (Potion, 75, 0.5, E.FORTIFY_ENDURANCE, 10, 60),
            PotE.LARGE_FORTIFY_ENDURANCE.value: (Potion, 105, 0.7, E.FORTIFY_ENDURANCE, 14, 60),
            PotE.SMALL_RESTORE_FATIGUE.value: (Potion, 30, 0.3, E.RESTORE_FATIGUE, 15, None),
            PotE.MEDIUM_RESTORE_FATIGUE.value: (Potion, 50, 0.5, E.RESTORE_FATIGUE, 25, None),
            PotE.LARGE_RESTORE_FATIGUE.value: (Potion, 70, 0.7, E.RESTORE_FATIGUE, 35, None),
            PotE.SMALL_CHAMELEON.value: (Potion, 60, 0.3, E.CHAMELEON, 0, 18),
            PotE.MEDIUM_CHAMELEON.value: (Potion, 100, 0.5, E.CHAMELEON, 0, 30),
            PotE.LARGE_CHAMELEON.value: (Potion, 140, 0.7, E.CHAMELEON, 0, 42),
            PotE.SMALL_FORTIFY_AGILITY.value: (Potion, 45, 0.3, E.FORTIFY_AGILITY, 6, 60),
            PotE.MEDIUM_FORTIFY_AGILITY.value: (Potion, 75, 0.5, E.FORTIFY_AGILITY, 10, 60),
            PotE.LARGE_FORTIFY_AGILITY.value: (Potion, 105, 0.7, E.FORTIFY_AGILITY, 14, 60),
            PotE.SMALL_CURE_COMMON_DISEASE.value: (Potion, 30, 0.3, E.CURE_COMMON_DISEASE, 0, None),
            PotE.MEDIUM_CURE_COMMON_DISEASE.value: (Potion, 50, 0.5, E.CURE_COMMON_DISEASE, 0, None),
            PotE.LARGE_CURE_COMMON_DISEASE.value: (Potion, 70, 0.7, E.CURE_COMMON_DISEASE, 0, None),
            PotE.SMALL_BLESSED_WATER.value: (Potion, 60, 0.3, E.TURN_UNDEAD, 12, None),
            PotE.MEDIUM_BLESSED_WATER.value: (Potion, 100, 0.5, E.TURN_UNDEAD, 20, None),
            PotE.LARGE_BLESSED_WATER.value: (Potion, 140, 0.7, E.TURN_UNDEAD, 28, None)
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
        return {key: value for key, value in zip(self._cols.keys(), self._config[item_name])}