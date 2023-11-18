class SwordHeavyKit:
    """
    This kit is designed for a warrior class character. It includes a long sword, a heavy shield, and a full set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["long_sword"],
            "shield": ["shield_heavy"],
            "armor": ["cuirass_heavy", "helmet_heavy", "greaves_heavy", "gauntlets_heavy", "boots_heavy", "pauldrons_heavy"]
        }
class WarAxeHeavyKit:
    """
    This kit is designed for a warrior class character. It includes a war axe, a heavy shield, and a full set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["war_axe"],
            "shield": ["shield_heavy"],
            "armor": ["cuirass_heavy", "helmet_heavy", "greaves_heavy", "gauntlets_heavy", "boots_heavy", "pauldrons_heavy"]
        }
class BattleAxeHeavyKit:
    """
    This kit is designed for a warrior class character. It includes a battle axe, a heavy shield, and a full set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["battle_axe"],
            "shield": ["shield_heavy"],
            "armor": ["cuirass_heavy", "helmet_heavy", "greaves_heavy", "gauntlets_heavy", "boots_heavy", "pauldrons_heavy"]
        }

class WarhammerHeavyKit:
    """
    This kit is designed for a warrior class character. It includes a warhammer and a full set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["warhammer"],
            "armor": ["cuirass_heavy", "helmet_heavy", "greaves_heavy", "gauntlets_heavy", "boots_heavy", "pauldrons_heavy"]
        }

class BowHeavyKit:
    """
    This kit is designed for a warrior class character. It includes a bow, a short sword, arrows, and a set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["bow", "short_sword"],
            "misc": ["arrow"],
            "armor": ["cuirass_heavy", "helmet_heavy", "boots_heavy"]
        }
class BowMediumKit:
    """
    This kit is designed for a scout class character. It includes a bow, a short sword, arrows, and a set of medium armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["bow", "short_sword"],
            "misc": ["arrow"],
            "armor": ["cuirass_medium", "helmet_medium", "boots_medium"]
        }
class BowLightKit:
    """
    This kit is designed for a scout class character. It includes a bow, a short sword, arrows, and a set of light armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["bow", "short_sword"],
            "misc": ["arrow"],
            "armor": ["cuirass_light", "helmet_light", "boots_light"]
        }
class PilgrimKit:
    """
    This kit is designed for a pilgrim class character. It includes a staff and a religious symbol.
    """
        def __init__(self):
            self.items = {
                "weapon": ["staff"],
                "misc": ["religious_symbol"]
            }
class ScoutKit:
    """
    This kit is designed for a scout class character. It includes a dagger, a set of light armor, and a lockpick.
    """
    def __init__(self):
        self.items = {
                "weapon": ["dagger"],
                "armor": ["cuirass_light", "boots_light"],
                "misc": ["lockpick"]
        }
class SorcererKit:
    """
    This kit is designed for a sorcerer class character. It includes a spell book with two spells and a sorcerer's robe.
    """
    def __init__(self):
        self.items = {
            "spell_book": ["tome_of_summoning", "tome_of_mystic_shield"],
            "robe": ["sorcerer_robe"]
        }
class SpellswordLongSwordKit:
    """
    This kit is designed for a spellsword class character. It includes a long sword, a spell book with two spells, and a set of medium armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["long_sword"],
            "spell_book": ["tome_of_flame_aura", "tome_of_healing"],
            "armor": ["cuirass_medium", "helmet_medium", "boots_medium"]
        }
class SpellswordMaceKit:
    """
    This kit is designed for a spellsword class character. It includes a mace, a spell book with a levitation spell, and a set of medium armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["mace"],
            "spell_book": ["tome_of_levitation"],
            "armor": ["cuirass_medium", "helmet_medium", "boots_medium"]
        }
class MonkKit:
    """
    This kit is designed for a monk class character. It includes a staff and a monk's robe.
    """
    def __init__(self):
        self.items = {
            "weapon": ["staff"],
            "robe": ["monk_robe"]
        }

class AssassinKit:
    """
    This kit is designed for an assassin class character. It includes a dagger, a short sword, a set of light armor, and a lockpick.
    """
    def __init__(self):
        self.items = {
            "weapon": ["dagger", "short_sword"],
            "armor": ["cuirass_light", "helmet_light", "boots_light"],
            "misc": ["lockpick"]
        }

class BardMediumKit:
    """
    This kit is designed for a bard class character. It includes a lute, a flute, a short sword, and a set of medium armor.
    """
    def __init__(self):
        self.items = {
            "instrument": ["lute", "flute"],
            "weapon": ["short_sword"],
            "armor": ["cuirass_medium", "boots_medium"]
        }
class BardLightKit:
    """
    This kit is designed for a bard class character. It includes a lute, a flute, a dagger, and a set of light armor.
    """
    def __init__(self):
        self.items = {
            "instrument": ["lute", "flute"],
            "weapon": ["dagger"],
            "armor": ["cuirass_light", "boots_light"]
        }

class BattleMageMediumKit:
    """
    This kit is designed for a battlemage class character. It includes a staff, a long sword, a spell book with two spells, and a set of medium armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["staff", "long_sword"],
            "spell_book": ["tome_of_lightning_bolt", "tome_of_frostbite"],
            "armor": ["cuirass_medium", "helmet_medium", "boots_medium"]
        }
class BattleMageHeavyKit:
    """
    This kit is designed for a battlemage class character. It includes a mace, a spell book with a fireball spell, and a set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["mace"],
            "spell_book": ["tome_of_fireball"],
            "armor": ["cuirass_heavy", "helmet_heavy", "greaves_heavy"]
        }
class AgentKit:
    """
    This kit is designed for an agent class character. It includes a dagger, a set of light armor, and a lockpick.
    """
    def __init__(self):
        self.items = {
            "weapon": ["dagger"],
            "armor": ["cuirass_light", "boots_light"],
            "misc": ["lockpick"]
        }

class ArcherKit:
    """
    This kit is designed for an archer class character. It includes a bow, arrows, and a set of light armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["bow"],
            "misc": ["arrow"],
            "armor": ["cuirass_light", "boots_light"]
        }

class HealerKit:
    """
    This kit is designed for a healer class character. It includes a spell book with two healing spells and healing potions.
    """
    def __init__(self):
        self.items = {
            "spell_book": ["tome_of_healing", "tome_of_purification"],
            "misc": ["healing_potions"]
        }

class RogueKit:
    """
    This kit is designed for a rogue class character. It includes a short sword, a dagger, a set of light armor, a lockpick, and a poison vial.
    """
    def __init__(self):
        self.items = {
            "weapon": ["short_sword", "dagger"],
            "armor": ["cuirass_light"],
            "misc": ["lockpick", "poison_vial"]
        }

class MageSpellBookKit:
    """
    This kit is designed for a mage class character. It includes a spell book with two spells and a mage's robe.
    """
    def __init__(self):
        self.items = {
            "spell_book": ["tome_of_fireball", "tome_of_levitation"],
            "robe": ["mage_robe"]
        }
class MageStaffKit:
    """
    This kit is designed for a mage class character. It includes a staff and a mage's robe.
    """
    def __init__(self):
        self.items = {
            "weapon": ["staff"],
            "robe": ["mage_robe"]
        }

class ThiefKit:
    """
    This kit is designed for a thief class character. It includes a dagger, a short sword, a set of light armor, and a lockpick.
    """
    def __init__(self):
        self.items = {
            "weapon": ["dagger", "short_sword"],
            "armor": ["cuirass_light", "helmet_light", "boots_light"],
            "misc": ["lockpick"]
        }

class WitchhunterMediumKit:
    """
    This kit is designed for a witchhunter class character. It includes a crossbow, a dagger, a spell book with two spells, a set of medium armor, and bolts.
    """
    def __init__(self):
        self.items = {
            "weapon": ["crossbow", "dagger"],
            "spell_book": ["tome_of_banishment", "tome_of_spirit_trap"],
            "armor": ["cuirass_medium", "boots_medium"],
            "misc": ["bolts"]
        }
class WitchhunterLightKit:
    """
    This kit is designed for a witchhunter class character. It includes a crossbow, a dagger, a spell book with two spells, a set of light armor, and bolts.
    """
    def __init__(self):
        self.items = {
            "weapon": ["crossbow", "dagger"],
            "spell_book": ["tome_of_banishment", "tome_of_spirit_trap"],
            "armor": ["cuirass_light", "boots_light"],
            "misc": ["bolts"]
        }

class InventoryClassMandatoryItems:
    """
    This class represents the mapping of character classes to their mandatory inventory items.
    Each class is represented by a list of tuples. Each tuple contains a kit and its probability.
    These kits are used to generate the initial inventory for characters of the corresponding class in the game.
    """
    def __init__(self):
        self._config = {
            "warrior": [
                (SwordHeavyKit, 0.2),
                (WarAxeHeavyKit, 0.4),
                (BattleAxeHeavyKit, 0.4),
                (WarhammerHeavyKit, 0.3),
                (BowHeavyKit, 0.3),
            ],
            "monk": [
                (MonkKit, 1.0),
            ],
            "assassin": [
                (AssassinKit, 1.0),
            ],
            "bard": [
                (BardMediumKit, 0.5),
                (BardLightKit, 0.5),
            ],
            "battlemage": [
                (BattleMageHeavyKit, 0.4),
                (BattleMageMediumKit, 0.6),
            ],
            "crusader": [
                (SwordHeavyKit, 0.4),
                (WarAxeHeavyKit, 0.3),
                (BattleAxeHeavyKit, 0.3),
            ],
            "knight": [
                (SwordHeavyKit, 1.0),
            ],
            "pilgrim": [
                (PilgrimKit, 1.0),
            ],
            "scout": [
                (BowLightKit, 0.5),
                (ScoutKit, 0.5),
            ],
            "sorcerer": [
                (SorcererKit, 1.0),
            ],
            "spellsword": [
                (SpellswordLongSwordKit, 0.6),
                (SpellswordMaceKit, 0.4),
            ],
            "agent": [
                (AgentKit, 1.0),
            ],
            "archer": [
                (ArcherKit, 1.0),
            ],
            "healer": [
                (HealerKit, 1.0),
            ],
            "rogue": [
                (RogueKit, 1.0),
            ],
            "mage": [
                (MageSpellBookKit, 0.7),
                (MageStaffKit, 0.3),
            ],
            "thief": [
                (ThiefKit, 0.6),
                (ArcherKit, 0.4),
            ],
            "witchhunter": [
                (WitchhunterMediumKit, 0.6),
                (WitchhunterLightKit, 0.4),
            ]
        }

    def get_kits_and_probabilities(self, character_class: str) -> list[tuple[object, float]]:
        """
        This method returns the list of kits and their probabilities for a specific character class.
        The method takes one parameter: the class of the character.
        The character_class parameter should be a string representing the class of the character.
        The method returns a list of tuples: each tuple contains a kit and its probability.
        """
        if character_class not in self._config:
            raise ValueError(f"Character class '{character_class}' not found in configuration.")
        return self._config[character_class]

