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
            ScrE.FIREBALL.value: (Scroll, 100, 0.1, E.FIRE_DAMAGE.value, 30, None, "distance"),
            ScrE.FROSTBITE.value: (Scroll, 100, 0.1, E.FROST_DAMAGE.value, 25, None, "touch"),
            ScrE.LEVITATION.value: (Scroll, 150, 0.1, E.LEVITATE.value, 10, None, "self"),
            ScrE.SUMMON_SCAMP.value: (Scroll, 200, 0.1, E.SUMMON_CREATURE.value, 15, None, "self"),
            ScrE.HEAL.value: (Scroll, 100, 0.1, E.RESTORE_HEALTH.value, 20, None, "self"),
            ScrE.NIGHT_EYE.value: (Scroll, 100, 0.1, E.NIGHT_EYE.value, 10, None, "self"),
            ScrE.BOUND_SWORD.value: (Scroll, 200, 0.1, E.BOUND_ITEM.value, 15, None, "self"),
            ScrE.WATER_BREATHING.value: (Scroll, 150, 0.1, E.WATER_BREATHING.value, 10, None, "self"),
            ScrE.PARALYSIS.value: (Scroll, 200, 0.1, E.PARALYSIS.value, 20, None, "touch"),
            ScrE.CHAMELEON.value: (Scroll, 150, 0.1, E.CHAMELEON.value, 10, None, "self"),
            ScrE.BOUND_BOW.value: (Scroll, 200, 0.1, E.BOUND_ITEM.value, 15, None, "self"),
            ScrE.SUMMON_SKELETON.value: (Scroll, 200, 0.1, E.SUMMON_CREATURE.value, 15, None, "self"),
            ScrE.CURE_COMMON_DISEASE.value: (Scroll, 200, 0.1, E.CURE_COMMON_DISEASE.value, 20, None, "touch"),
            ScrE.DETECT_CREATURE.value: (Scroll, 150, 0.1, E.DETECT_CREATURE.value, 10, None, "self"),
            ScrE.DISPEL.value: (Scroll, 200, 0.1, E.DISPEL.value, 15, None, "self"),
            ScrE.FIRE_SHIELD.value: (Scroll, 150, 0.1, E.SHIELD.value, 20, None, "self"),
            ScrE.FROST_SHIELD.value: (Scroll, 150, 0.1, E.SHIELD.value, 20, None, "self"),
            ScrE.LIGHTNING_SHIELD.value: (Scroll, 150, 0.1, E.SHIELD.value, 20, None, "self"),
            ScrE.MARK.value: (Scroll, 150, 0.1, E.MARK.value, 10, None, "self"),
            ScrE.RECALL.value: (Scroll, 150, 0.1, E.RECALL.value, 10, None, "self"),
            ScrE.TELEKINESIS.value: (Scroll, 200, 0.1, E.TELEKINESIS.value, 15, None, "self"),
            ScrE.WATER_WALKING.value: (Scroll, 150, 0.1, E.WATER_WALKING.value, 10, None, "self"),
            ScrE.FORTIFY_STRENGTH.value: (Scroll, 200, 0.1, E.FORTIFY_STRENGTH.value, 20, None, "self"),
            ScrE.FORTIFY_INTELLIGENCE.value: (Scroll, 200, 0.1, E.FORTIFY_INTELLIGENCE.value, 20, None, "self"),
            ScrE.FORTIFY_WILLPOWER.value: (Scroll, 200, 0.1, E.FORTIFY_WILLPOWER.value, 20, None, "self"),
            ScrE.FORTIFY_AGILITY.value: (Scroll, 200, 0.1, E.FORTIFY_AGILITY.value, 20, None, "self"),
            ScrE.FORTIFY_SPEED.value: (Scroll, 200, 0.1, E.FORTIFY_SPEED.value, 20, None, "self"),
            ScrE.FORTIFY_ENDURANCE.value: (Scroll, 200, 0.1, E.FORTIFY_ENDURANCE.value, 20, None, "self"),
            ScrE.FORTIFY_PERSONALITY.value: (Scroll, 200, 0.1, E.FORTIFY_PERSONALITY.value, 20, None, "self"),
            ScrE.FORTIFY_LUCK.value: (Scroll, 200, 0.1, E.FORTIFY_LUCK.value, 20, None, "self"),
            ScrE.FORTIFY_LONG_BLADE.value: (Scroll, 200, 0.1, E.FORTIFY_LONG_BLADE.value, 20, None, "self"),
            ScrE.FORTIFY_SHORT_BLADE.value: (Scroll, 200, 0.1, E.FORTIFY_SHORT_BLADE.value, 20, None, "self"),
            ScrE.FORTIFY_LIGHT_ARMOR.value: (Scroll, 200, 0.1, E.FORTIFY_LIGHT_ARMOR.value, 20, None, "self"),
            ScrE.FORTIFY_HEAVY_ARMOR.value: (Scroll, 200, 0.1, E.FORTIFY_HEAVY_ARMOR.value, 20, None, "self"),
            ScrE.FORTIFY_BLOCK.value: (Scroll, 200, 0.1, E.FORTIFY_BLOCK.value, 20, None, "self"),
            ScrE.FORTIFY_AXE.value: (Scroll, 200, 0.1, E.FORTIFY_AXE.value, 20, None, "self"),
            ScrE.FORTIFY_BOW.value: (Scroll, 200, 0.1, E.FORTIFY_BOW.value, 20, None, "self"),
            ScrE.FORTIFY_SPEAR.value: (Scroll, 200, 0.1, E.FORTIFY_SPEAR.value, 20, None, "self"),
            ScrE.FORTIFY_ARMORER.value: (Scroll, 200, 0.1, E.FORTIFY_ARMORER.value, 20, None, "self"),
            ScrE.FORTIFY_DESTRUCTION.value: (Scroll, 200, 0.1, E.FORTIFY_DESTRUCTION.value, 20, None, "self"),
            ScrE.FORTIFY_ALTERATION.value: (Scroll, 200, 0.1, E.FORTIFY_ALTERATION.value, 20, None, "self"),
            ScrE.FORTIFY_ILLUSION.value: (Scroll, 200, 0.1, E.FORTIFY_ILLUSION.value, 20, None, "self"),
            ScrE.FORTIFY_CONJURATION.value: (Scroll, 200, 0.1, E.FORTIFY_CONJURATION.value, 20, None, "self"),
            ScrE.FORTIFY_MYSTICISM.value: (Scroll, 200, 0.1, E.FORTIFY_MYSTICISM.value, 20, None, "self"),
            ScrE.FORTIFY_ENCHANT.value: (Scroll, 200, 0.1, E.FORTIFY_ENCHANT.value, 20, None, "self"),
            ScrE.FORTIFY_RESTORATION.value: (Scroll, 200, 0.1, E.FORTIFY_RESTORATION.value, 20, None, "self"),
            ScrE.FORTIFY_ALCHEMY.value: (Scroll, 200, 0.1, E.FORTIFY_ALCHEMY.value, 20, None, "self"),
            ScrE.FORTIFY_UNARMORED.value: (Scroll, 200, 0.1, E.FORTIFY_UNARMORED.value, 20, None, "self"),
            ScrE.FORTIFY_SECURITY.value: (Scroll, 200, 0.1, E.FORTIFY_SECURITY.value, 20, None, "self"),
            ScrE.FORTIFY_SNEAK.value: (Scroll, 200, 0.1, E.FORTIFY_SNEAK.value, 20, None, "self"),
            ScrE.FORTIFY_ACROBATICS.value: (Scroll, 200, 0.1, E.FORTIFY_ACROBATICS.value, 20, None, "self"),
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
