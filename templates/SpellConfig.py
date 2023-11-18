from enum.EffectEnum import EffectEnum as EfE
from enum.SpellEnum import SpellEnum as SpellE

class SpellConfig:
    """
    This class represents the mapping of spell details.
    Each spell is represented by a tuple of three values: effect, magnitude, type.
    """
    def __init__(self):
        self._index = {"effect": 0, "magnitude": 1, "type": 2}
        self._config = {
            SpellE.FIREBALL.value: (EfE.FIRE_DAMAGE.value, 30, "self"),
            SpellE.FROSTBITE.value: (EfE.FROST_DAMAGE.value, 25, "self"),
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
            SpellE.TELEKINESIS.value: (EfE.TELEKINESIS.value, 15, "distance"),
            SpellE.WATER_WALKING.value: (EfE.WATER_WALKING.value, 10, "self"),
            SpellE.FORTIFY_ATTRIBUTE.value: (EfE.FORTIFY_ATTRIBUTE.value, 20, "self"),
            SpellE.FORTIFY_SKILL.value: (EfE.FORTIFY_SKILL.value, 20, "self"),
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
        return {key: value for key, value in zip(self._index.keys(), self._config[spell_name])}
