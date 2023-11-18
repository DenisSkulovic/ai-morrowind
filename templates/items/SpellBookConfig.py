from enum.items.SpellBookEnum import SpellBookEnum as SBkE
from classes.items.book.SpellBook import SpellBook

from enum.EffectEnum import EffectEnum as EfE



class SpellBookConfig:
    """
    This class represents the mapping of spell book items to their details.
    Each spell book is represented by a tuple of four values: item, base_price, base_weight, spell_name.
    """
    def __init__(self):
        self._index = {"item": 0, "base_price": 1, "base_weight": 2, "spell_name": 3}
        self._config = {
            SBkE.TOME_OF_FIREBALL.value: (SpellBook, 100, 1.0, "fireball", "self"),
            SBkE.TOME_OF_FROSTBITE.value: (SpellBook, 80, 1.0, "frostbite", "self"),
            SBkE.TOME_OF_LEVITATION.value: (SpellBook, 150, 1.0, "levitation", "self"),
            SBkE.TOME_OF_SUMMON_SCAMP.value: (SpellBook, 120, 1.0, "summon_scamp", "self"),
            SBkE.TOME_OF_HEALING.value: (SpellBook, 90, 1.0, "heal", "self"),
            SBkE.TOME_OF_NIGHT_EYE.value: (SpellBook, 70, 1.0, "night_eye", "self"),
            SBkE.TOME_OF_BOUND_SWORD.value: (SpellBook, 110, 1.0, "bound_sword", "self"),
            SBkE.TOME_OF_WATER_BREATHING.value: (SpellBook, 130, 1.0, "water_breathing", "self"),
            SBkE.TOME_OF_PARALYSIS.value: (SpellBook, 140, 1.0, "paralysis", "touch"),
            SBkE.TOME_OF_CHAMELEON.value: (SpellBook, 100, 1.0, "chameleon", "self"),
            SBkE.TOME_OF_BOUND_BOW.value: (SpellBook, 110, 1.0, "bound_bow", "self"),
            SBkE.TOME_OF_SUMMON_SKELETON.value: (SpellBook, 120, 1.0, "summon_skeleton", "self"),
            SBkE.TOME_OF_CURE_COMMON_DISEASE.value: (SpellBook, 90, 1.0, "cure_common_disease", "touch"),
            SBkE.TOME_OF_DETECT_CREATURE.value: (SpellBook, 70, 1.0, "detect_creature", "self"),
            SBkE.TOME_OF_DISPEL.value: (SpellBook, 80, 1.0, "dispel", "self"),
            SBkE.TOME_OF_FIRE_SHIELD.value: (SpellBook, 100, 1.0, "fire_shield", "self"),
            SBkE.TOME_OF_FROST_SHIELD.value: (SpellBook, 100, 1.0, "frost_shield", "self"),
            SBkE.TOME_OF_LIGHTNING_SHIELD.value: (SpellBook, 100, 1.0, "lightning_shield", "self"),
            SBkE.TOME_OF_MARK.value: (SpellBook, 150, 1.0, "mark", "self"),
            SBkE.TOME_OF_RECALL.value: (SpellBook, 150, 1.0, "recall", "self"),
            SBkE.TOME_OF_TELEKINESIS.value: (SpellBook, 120, 1.0, "telekinesis", "distance"),
            SBkE.TOME_OF_WATER_WALKING.value: (SpellBook, 130, 1.0, "water_walking", "self"),
            SBkE.TOME_OF_FORTIFY_ATTRIBUTE.value: (SpellBook, 140, 1.0, "fortify_attribute", "self"),
            SBkE.TOME_OF_FORTIFY_SKILL.value: (SpellBook, 100, 1.0, "fortify_skill", "self"),
        }

    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given spell book.
        The method takes one parameter: the name of the spell book.
        The item_name parameter should be a string representing the name of the spell book.
        The method returns a dictionary with keys: item, base_price, base_weight, spell_name.
        """
        if item_name not in self._config:
            raise ValueError(f"Spell book name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._index.keys(), self._config[item_name])}
