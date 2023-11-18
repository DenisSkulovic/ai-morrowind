import templates.kits.kits as k


class InventoryClassMandatoryItems:
    """
    This class represents the mapping of character classes to their mandatory inventory items.
    Each class is represented by a list of tuples. Each tuple contains a kit and its probability.
    These kits are used to generate the initial inventory for characters of the corresponding class in the game.
    """
    def __init__(self):
        self._config = {
            "warrior": [
                (k.SwordHeavyKit, 0.2),
                (k.WarAxeHeavyKit, 0.4),
                (k.BattleAxeHeavyKit, 0.4),
                (k.WarhammerHeavyKit, 0.3),
                (k.BowHeavyKit, 0.3),
            ],
            "monk": [
                (k.MonkKit, 1.0),
            ],
            "assassin": [
                (k.AssassinKit, 1.0),
            ],
            "bard": [
                (k.BardMediumKit, 0.5),
                (k.BardLightKit, 0.5),
            ],
            "battlemage": [
                (k.BattleMageHeavyKit, 0.4),
                (k.BattleMageMediumKit, 0.6),
            ],
            "crusader": [
                (k.SwordHeavyKit, 0.4),
                (k.WarAxeHeavyKit, 0.3),
                (k.BattleAxeHeavyKit, 0.3),
            ],
            "knight": [
                (k.SwordHeavyKit, 1.0),
            ],
            "pilgrim": [
                (k.PilgrimKit, 1.0),
            ],
            "scout": [
                (k.BowLightKit, 0.5),
                (k.ScoutKit, 0.5),
            ],
            "sorcerer": [
                (k.SorcererKit, 1.0),
            ],
            "spellsword": [
                (k.SpellswordLongSwordKit, 0.6),
                (k.SpellswordMaceKit, 0.4),
            ],
            "agent": [
                (k.AgentKit, 1.0),
            ],
            "archer": [
                (k.ArcherKit, 1.0),
            ],
            "healer": [
                (k.HealerKit, 1.0),
            ],
            "rogue": [
                (k.RogueKit, 1.0),
            ],
            "mage": [
                (k.MageSpellBookKit, 0.7),
                (k.MageStaffKit, 0.3),
            ],
            "thief": [
                (k.ThiefKit, 0.6),
                (k.ArcherKit, 0.4),
            ],
            "witchhunter": [
                (k.WitchhunterMediumKit, 0.6),
                (k.WitchhunterLightKit, 0.4),
            ]
        }

    def get_kits_and_probabilities(self, character_class: str) -> list[tuple[object, float]]:
        """
        This method returns the list of kits and their probabilities for a specific character class.
        The method takes one parameter: the class of the character.
        The character_class parameter should be a string representing the class of the character.
        The method returns a list of tuples: each tuple contains a kit and its probability.

        Example:
        If the character class is 'mage', the method might return:
        [(k.MageSpellBookKit, 0.7), (k.MageStaffKit, 0.3)]
        """
        if character_class not in self._config:
            raise ValueError(f"Character class '{character_class}' not found in configuration.")
        return self._config[character_class]

