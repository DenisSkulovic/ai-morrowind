from enum.EffectEnum import EffectEnum as EfE
from enum.SpellEnum import SpellEnum as SpellE

class SpellConfig:
    """
    This class represents the mapping of spell details.
    Each spell is represented by a tuple of three values: effect, magnitude, type.
    """
    def __init__(self):
        self._cols = {"effect": 0, "magnitude": 1, "type": 2}
        self._config = {
            SpellE.FIREBALL.value: (EfE.FIRE_DAMAGE.value, 30, "distance"),
            SpellE.FROSTBITE.value: (EfE.FROST_DAMAGE.value, 25, "touch"),
            SpellE.LEVITATION.value: (EfE.LEVITATE.value, 10, "self"),
            SpellE.SUMMON_SCAMP.value: (EfE.SUMMON_CREATURE.value, 15, "self"),
            SpellE.HEAL.value: (EfE.RESTORE_HEALTH.value, 20, "self"),
            SpellE.NIGHT_EYE.value: (EfE.NIGHT_EYE.value, 10, "self"),
            SpellE.BOUND_SWORD.value: (EfE.BOUND_ITEM.value, 15, "self"),
            SpellE.WATER_BREATHING.value: (EfE.WATER_BREATHING.value, 10, "self"),
            SpellE.PARALYSIS.value: (EfE.PARALYSIS.value, 20, "touch"),
            SpellE.CHAMELEON.value: (EfE.CHAMELEON.value, 10, "self"),
            SpellE.BOUND_BOW.value: (EfE.BOUND_ITEM.value, 15, "self"),
            SpellE.SUMMON_SKELETON.value: (EfE.SUMMON_CREATURE.value, 15, "self"),
            SpellE.CURE_COMMON_DISEASE.value: (EfE.CURE_COMMON_DISEASE.value, 20, "touch"),
            SpellE.DETECT_CREATURE.value: (EfE.DETECT_CREATURE.value, 10, "self"),
            SpellE.DISPEL.value: (EfE.DISPEL.value, 15, "self"),
            SpellE.FIRE_SHIELD.value: (EfE.SHIELD.value, 20, "self"),
            SpellE.FROST_SHIELD.value: (EfE.SHIELD.value, 20, "self"),
            SpellE.LIGHTNING_SHIELD.value: (EfE.SHIELD.value, 20, "self"),
            SpellE.MARK.value: (EfE.MARK.value, 10, "self"),
            SpellE.RECALL.value: (EfE.RECALL.value, 10, "self"),
            SpellE.TELEKINESIS.value: (EfE.TELEKINESIS.value, 15, "self"),
            SpellE.WATER_WALKING.value: (EfE.WATER_WALKING.value, 10, "self"),
            SpellE.FORTIFY_STRENGTH.value: (EfE.FORTIFY_STRENGTH.value, 20, "self"),
            SpellE.FORTIFY_INTELLIGENCE.value: (EfE.FORTIFY_INTELLIGENCE.value, 20, "self"),
            SpellE.FORTIFY_WILLPOWER.value: (EfE.FORTIFY_WILLPOWER.value, 20, "self"),
            SpellE.FORTIFY_AGILITY.value: (EfE.FORTIFY_AGILITY.value, 20, "self"),
            SpellE.FORTIFY_SPEED.value: (EfE.FORTIFY_SPEED.value, 20, "self"),
            SpellE.FORTIFY_ENDURANCE.value: (EfE.FORTIFY_ENDURANCE.value, 20, "self"),
            SpellE.FORTIFY_PERSONALITY.value: (EfE.FORTIFY_PERSONALITY.value, 20, "self"),
            SpellE.FORTIFY_LUCK.value: (EfE.FORTIFY_LUCK.value, 20, "self"),
            SpellE.FORTIFY_LONG_BLADE.value: (EfE.FORTIFY_LONG_BLADE.value, 20, "self"),
            SpellE.FORTIFY_SHORT_BLADE.value: (EfE.FORTIFY_SHORT_BLADE.value, 20, "self"),
            SpellE.FORTIFY_LIGHT_ARMOR.value: (EfE.FORTIFY_LIGHT_ARMOR.value, 20, "self"),
            SpellE.FORTIFY_HEAVY_ARMOR.value: (EfE.FORTIFY_HEAVY_ARMOR.value, 20, "self"),
            SpellE.FORTIFY_BLOCK.value: (EfE.FORTIFY_BLOCK.value, 20, "self"),
            SpellE.FORTIFY_AXE.value: (EfE.FORTIFY_AXE.value, 20, "self"),
            SpellE.FORTIFY_BOW.value: (EfE.FORTIFY_BOW.value, 20, "self"),
            SpellE.FORTIFY_SPEAR.value: (EfE.FORTIFY_SPEAR.value, 20, "self"),
            SpellE.FORTIFY_ARMORER.value: (EfE.FORTIFY_ARMORER.value, 20, "self"),
            SpellE.FORTIFY_DESTRUCTION.value: (EfE.FORTIFY_DESTRUCTION.value, 20, "self"),
            SpellE.FORTIFY_ALTERATION.value: (EfE.FORTIFY_ALTERATION.value, 20, "self"),
            SpellE.FORTIFY_ILLUSION.value: (EfE.FORTIFY_ILLUSION.value, 20, "self"),
            SpellE.FORTIFY_CONJURATION.value: (EfE.FORTIFY_CONJURATION.value, 20, "self"),
            SpellE.FORTIFY_MYSTICISM.value: (EfE.FORTIFY_MYSTICISM.value, 20, "self"),
            SpellE.FORTIFY_ENCHANT.value: (EfE.FORTIFY_ENCHANT.value, 20, "self"),
            SpellE.FORTIFY_RESTORATION.value: (EfE.FORTIFY_RESTORATION.value, 20, "self"),
            SpellE.FORTIFY_ALCHEMY.value: (EfE.FORTIFY_ALCHEMY.value, 20, "self"),
            SpellE.FORTIFY_UNARMORED.value: (EfE.FORTIFY_UNARMORED.value, 20, "self"),
            SpellE.FORTIFY_SECURITY.value: (EfE.FORTIFY_SECURITY.value, 20, "self"),
            SpellE.FORTIFY_SNEAK.value: (EfE.FORTIFY_SNEAK.value, 20, "self"),
            SpellE.FORTIFY_ACROBATICS.value: (EfE.FORTIFY_ACROBATICS.value, 20, "self"),
        }

    def get(self, spell_name: str) -> dict:
        """
        This method returns the details of a given spell.
        The method takes one parameter: the name of the spell.
        The spell_name parameter should be a string representing the name of the spell.
        The method returns a dictionary with keys: effect, magnitude, type.
        """
        if spell_name not in self._config:
            raise ValueError(f"Spell name '{spell_name}' not found in configuration.")
        return {key: value for key, value in zip(self._cols.keys(), self._config[spell_name])}
