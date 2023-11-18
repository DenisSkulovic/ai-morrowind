from templates.items.ItemConfig import ItemConfig as ItCon
from enum.items.PotionEnum import PotionEnum as PotE
from enum.items.RingEnum import RingEnum as RingE
from enum.items.ScrollEnum import ScrollEnum as ScrE

class InventoryClassOptionalItems:
    """
    This class represents the mapping of character classes to their optional inventory items.
    Each item is represented by a tuple of two values: item details and probability.
    The item details are represented by a tuple of five values: item, quantity, standard deviation, effect, spell.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._index = {"item": 0, "quantity": 1, "std_dev": 2, "probability": 3}
        self._config = {
            "warrior": [
                (ItCon().get("potion", PotE.RESTORE_HEALTH.value), 1, 0.50, 0.50),
                (ItCon().get("potion", PotE.FORTIFY_STRENGTH.value), 1, 0.30, 0),
                (ItCon().get("tool", "RepairTool"), 1, 0.40, 0)
            ],
            "mage": [
                (ItCon().get("potion", PotE.RESTORE_MAGICKA.value), 1, 0.60, 0),
                (ItCon().get("scroll", ScrE.FIREBALL.value), 1, 0.30, 0),
                (ItCon().get("scroll", ScrE.LEVITATION.value), 1, 0.25, 0)
            ],
            "thief": [
                (ItCon().get("tool", "Lockpick"), 1, 0.70, 0),
                (ItCon().get("tool", "Probe"), 1, 0.50, 0),
                (ItCon().get("potion", PotE.INVISIBILITY.value), 1, 0.40, 0)
            ],
            "monk": [
                (ItCon().get("potion", PotE.RESTORE_HEALTH.value), 1, 0.40, 0),
                (ItCon().get("potion", PotE.FORTIFY_UNARMORED.value), 1, 0.30, 0)
            ],
            "assassin": [
                (ItCon().get("potion", PotE.POISON.value), 1, 0.60, 0),
                (ItCon().get("potion", PotE.SWIFT_SWIM.value), 1, 0.40, 0),
            ],
            "bard": [
                (ItCon().get("potion", PotE.FORTIFY_PERSONALITY.value), 1, 0.40, 0)
            ],
            "battlemage": [
                (ItCon().get("potion", PotE.RESTORE_MAGICKA.value), 1, 0.60, 0),
                (ItCon().get("scroll", ScrE.FIREBALL.value), 1, 0.35, 0),
                (ItCon().get("scroll", ScrE.FROSTBITE.value), 1, 0.35, 0)
            ],
            "crusader": [
                (ItCon().get("potion", PotE.RESTORE_HEALTH.value), 1, 0.55, 0),
                (ItCon().get("potion", PotE.FORTIFY_ATTACK.value), 1, 0.40, 0)
            ],
            "knight": [
                (ItCon().get("potion", PotE.RESTORE_HEALTH.value), 1, 0.60, 0)
            ],
            "pilgrim": [
                (ItCon().get("item", "religious_icon"), 1, 0.50, 0),
                (ItCon().get("potion", PotE.FORTIFY_ENDURANCE.value), 1, 0.30, 0)
            ],
            "scout": [
                (ItCon().get("tool", "Lockpick"), 1, 0.60, 0),
                (ItCon().get("item", "LocalMap"), 1, 0.50, 0),
                (ItCon().get("potion", PotE.RESTORE_FATIGUE.value), 1, 0.40, 0)
            ],
            "sorcerer": [
                (ItCon().get("scroll", ScrE.SUMMON_SKELETON.value), 1, 0.45, 0),
                (ItCon().get("scroll", ScrE.COMMAND_CREATURE.value), 1, 0.30, 0),
                (ItCon().get("potion", PotE.RESTORE_MAGICKA.value), 1, 0.55, 0)
            ],
            "spellsword": [
                (ItCon().get("potion", PotE.RESTORE_MAGICKA.value), 1, 0.50, 0),
                (ItCon().get("potion", PotE.RESTORE_HEALTH.value), 1, 0.45, 0),
                (ItCon().get("scroll", ScrE.SHIELD.value), 1, 0.35, 0)
            ],
            "agent": [
                (ItCon().get("tool", "Lockpick"), 1, 0.60, 0),
                (ItCon().get("potion", PotE.INVISIBILITY.value), 1, 0.50, 0),
                (ItCon().get("ring", RingE.CHAMELEON.value), 1, 0.40, 0)
            ],
            "archer": [
                (ItCon().get("potion", PotE.FORTIFY_AGILITY.value), 1, 0.35, 0)
            ],
            "healer": [
                (ItCon().get("potion", PotE.RESTORE_HEALTH.value), 1, 0.70, 0),
                (ItCon().get("potion", PotE.CURE_COMMON_DISEASE.value), 1, 0.40, 0),
                (ItCon().get("scroll", ScrE.HEAL.value), 1, 0.50, 0)
            ],
            "rogue": [
                (ItCon().get("tool", "Lockpick"), 1, 0.65, 0),
                (ItCon().get("potion", PotE.INVISIBILITY.value), 1, 0.50, 0),
                (ItCon().get("ring", RingE.CHAMELEON.value), 1, 0.40, 0)
            ],
            "witchhunter": [
                (ItCon().get("potion", "holy_water"), 1, 0.55, 0),
                (ItCon().get("potion", PotE.RESTORE_MAGICKA.value), 1, 0.45, 0),
                (ItCon().get("scroll", ScrE.ABSORB_HEALTH.value), 1, 0.40, 0)
            ]
        }

    def get_item_and_properties(self, character_class: str, property: str) -> tuple[object, int, int, str, str]:
        """
        This method returns the item and its properties for a specific character class and property.
        The method takes two parameters: the class of the character and the property of interest.
        The character_class parameter should be a string representing the class of the character.
        The property parameter should be a string representing the property of interest.
        The method returns a tuple of five values: item, quantity, standard deviation, effect, spell.
        If a value is not applicable, it is represented by None.
        """
        if character_class not in self._config:
            raise ValueError(f"Character class '{character_class}' not found in configuration.")
        if property not in self._index:
            raise ValueError(f"Property '{property}' not found in configuration.")
        index = self._index[property]
        return self._config[character_class][index][0]

