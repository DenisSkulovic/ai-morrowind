from enum.SpellEnum import SpellEnum
from enum.items.SpellBookEnum import SpellBookEnum as SBkE
from classes.items.book.SpellBook import SpellBook


class SpellBookConfig:
    """
    This class represents the mapping of spell book items to their details.
    Each spell book is represented by a tuple of four values: item, base_price, base_weight, spell_name.
    """
    def __init__(self):
        self._cols = {"item": 0, "base_price": 1, "base_weight": 2, "spell_name": 3}
        self._config = {
            SBkE.TOME_OF_FIREBALL.value: (SpellBook, 100, 1.0, SpellEnum.FIREBALL.value),
            SBkE.TOME_OF_FROSTBITE.value: (SpellBook, 80, 1.0, SpellEnum.FROSTBITE.value),
            SBkE.TOME_OF_LEVITATION.value: (SpellBook, 150, 1.0, SpellEnum.LEVITATION.value),
            SBkE.TOME_OF_SUMMON_SCAMP.value: (SpellBook, 120, 1.0, SpellEnum.SUMMON_SCAMP.value),
            SBkE.TOME_OF_HEAL.value: (SpellBook, 90, 1.0, SpellEnum.HEAL.value),
            SBkE.TOME_OF_NIGHT_EYE.value: (SpellBook, 70, 1.0, SpellEnum.NIGHT_EYE.value),
            SBkE.TOME_OF_BOUND_SWORD.value: (SpellBook, 110, 1.0, SpellEnum.BOUND_SWORD.value),
            SBkE.TOME_OF_WATER_BREATHING.value: (SpellBook, 130, 1.0, SpellEnum.WATER_BREATHING.value),
            SBkE.TOME_OF_PARALYSIS.value: (SpellBook, 140, 1.0, SpellEnum.PARALYSIS.value),
            SBkE.TOME_OF_CHAMELEON.value: (SpellBook, 100, 1.0, SpellEnum.CHAMELEON.value),
            SBkE.TOME_OF_BOUND_BOW.value: (SpellBook, 110, 1.0, SpellEnum.BOUND_BOW.value),
            SBkE.TOME_OF_SUMMON_SKELETON.value: (SpellBook, 120, 1.0, SpellEnum.SUMMON_SKELETON.value),
            SBkE.TOME_OF_CURE_COMMON_DISEASE.value: (SpellBook, 90, 1.0, SpellEnum.CURE_COMMON_DISEASE.value),
            SBkE.TOME_OF_DETECT_CREATURE.value: (SpellBook, 70, 1.0, SpellEnum.DETECT_CREATURE.value),
            SBkE.TOME_OF_DISPEL.value: (SpellBook, 80, 1.0, SpellEnum.DISPEL.value),
            SBkE.TOME_OF_FIRE_SHIELD.value: (SpellBook, 100, 1.0, SpellEnum.FIRE_SHIELD.value),
            SBkE.TOME_OF_FROST_SHIELD.value: (SpellBook, 100, 1.0, SpellEnum.FROST_SHIELD.value),
            SBkE.TOME_OF_LIGHTNING_SHIELD.value: (SpellBook, 100, 1.0, SpellEnum.LIGHTNING_SHIELD.value),
            SBkE.TOME_OF_MARK.value: (SpellBook, 150, 1.0, SpellEnum.MARK.value),
            SBkE.TOME_OF_RECALL.value: (SpellBook, 150, 1.0, SpellEnum.RECALL.value),
            SBkE.TOME_OF_TELEKINESIS.value: (SpellBook, 120, 1.0, SpellEnum.TELEKINESIS.value),
            SBkE.TOME_OF_WATER_WALKING.value: (SpellBook, 130, 1.0, SpellEnum.WATER_WALKING.value),
            SBkE.TOME_OF_FORTIFY_STRENGTH.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_STRENGTH.value),
            SBkE.TOME_OF_FORTIFY_INTELLIGENCE.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_INTELLIGENCE.value),
            SBkE.TOME_OF_FORTIFY_WILLPOWER.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_WILLPOWER.value),
            SBkE.TOME_OF_FORTIFY_AGILITY.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_AGILITY.value),
            SBkE.TOME_OF_FORTIFY_SPEED.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_SPEED.value),
            SBkE.TOME_OF_FORTIFY_ENDURANCE.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_ENDURANCE.value),
            SBkE.TOME_OF_FORTIFY_PERSONALITY.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_PERSONALITY.value),
            SBkE.TOME_OF_FORTIFY_LUCK.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_LUCK.value),
            SBkE.TOME_OF_FORTIFY_LONG_BLADE.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_LONG_BLADE.value),
            SBkE.TOME_OF_FORTIFY_SHORT_BLADE.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_SHORT_BLADE.value),
            SBkE.TOME_OF_FORTIFY_LIGHT_ARMOR.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_LIGHT_ARMOR.value),
            SBkE.TOME_OF_FORTIFY_HEAVY_ARMOR.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_HEAVY_ARMOR.value),
            SBkE.TOME_OF_FORTIFY_BLOCK.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_BLOCK.value),
            SBkE.TOME_OF_FORTIFY_AXE.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_AXE.value),
            SBkE.TOME_OF_FORTIFY_BOW.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_BOW.value),
            SBkE.TOME_OF_FORTIFY_SPEAR.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_SPEAR.value),
            SBkE.TOME_OF_FORTIFY_ARMORER.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_ARMORER.value),
            SBkE.TOME_OF_FORTIFY_DESTRUCTION.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_DESTRUCTION.value),
            SBkE.TOME_OF_FORTIFY_ALTERATION.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_ALTERATION.value),
            SBkE.TOME_OF_FORTIFY_ILLUSION.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_ILLUSION.value),
            SBkE.TOME_OF_FORTIFY_CONJURATION.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_CONJURATION.value),
            SBkE.TOME_OF_FORTIFY_MYSTICISM.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_MYSTICISM.value),
            SBkE.TOME_OF_FORTIFY_ENCHANT.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_ENCHANT.value),
            SBkE.TOME_OF_FORTIFY_RESTORATION.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_RESTORATION.value),
            SBkE.TOME_OF_FORTIFY_ALCHEMY.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_ALCHEMY.value),
            SBkE.TOME_OF_FORTIFY_UNARMORED.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_UNARMORED.value),
            SBkE.TOME_OF_FORTIFY_SECURITY.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_SECURITY.value),
            SBkE.TOME_OF_FORTIFY_SNEAK.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_SNEAK.value),
            SBkE.TOME_OF_FORTIFY_ACROBATICS.value: (SpellBook, 100, 1.0, SpellEnum.FORTIFY_ACROBATICS.value),
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
        return {key: value for key, value in zip(self._cols.keys(), self._config[item_name])}
