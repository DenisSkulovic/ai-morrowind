# TODO instead of strings for items, use templates

class WeaponArmorKit:
    def __init__(self):
        self.items = { }
    
    def get_kit_based_on_culture_and_experience(self, culture, experience_level):
        kit = {}
        for item_type, items in self.items.items():
            culture_items = culture_item_mapping[culture][item_type]
            experience_range = experience_level_ranges[experience_level]
            filtered_items = self.filter_items_by_experience(culture_items, experience_range)
            kit[item_type] = random.choice(filtered_items)
        return kit

    @staticmethod
    def filter_items_by_experience(items, experience_range):
        # Implement logic to filter items based on experience level
        pass
    
class SwordHeavyKit(WeaponArmorKit):
    """
    This kit is designed for a warrior class character. It includes a long sword, a heavy shield, and a full set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["long_sword"],
            "shield": ["shield_heavy"],
            "armor": ["cuirass_heavy", "helmet_heavy", "greaves_heavy", "gauntlets_heavy", "boots_heavy", "pauldrons_heavy"]
        }
class WarAxeHeavyKit(WeaponArmorKit):
    """
    This kit is designed for a warrior class character. It includes a war axe, a heavy shield, and a full set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["war_axe"],
            "shield": ["shield_heavy"],
            "armor": ["cuirass_heavy", "helmet_heavy", "greaves_heavy", "gauntlets_heavy", "boots_heavy", "pauldrons_heavy"]
        }
class BattleAxeHeavyKit(WeaponArmorKit):
    """
    This kit is designed for a warrior class character. It includes a battle axe, a heavy shield, and a full set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["battle_axe"],
            "shield": ["shield_heavy"],
            "armor": ["cuirass_heavy", "helmet_heavy", "greaves_heavy", "gauntlets_heavy", "boots_heavy", "pauldrons_heavy"]
        }
class WarhammerHeavyKit(WeaponArmorKit):
    """
    This kit is designed for a warrior class character. It includes a warhammer and a full set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["warhammer"],
            "armor": ["cuirass_heavy", "helmet_heavy", "greaves_heavy", "gauntlets_heavy", "boots_heavy", "pauldrons_heavy"]
        }
class BowHeavyKit(WeaponArmorKit):
    """
    This kit is designed for a warrior class character. It includes a bow, a short sword, arrows, and a set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["bow", "short_sword"],
            "misc": ["arrow"],
            "armor": ["cuirass_heavy", "helmet_heavy", "boots_heavy"]
        }
class BowMediumKit(WeaponArmorKit):
    """
    This kit is designed for a scout class character. It includes a bow, a short sword, arrows, and a set of medium armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["bow", "short_sword"],
            "misc": ["arrow"],
            "armor": ["cuirass_medium", "helmet_medium", "boots_medium"]
        }
class BowLightKit(WeaponArmorKit):
    """
    This kit is designed for a scout class character. It includes a bow, a short sword, arrows, and a set of light armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["bow", "short_sword"],
            "misc": ["arrow"],
            "armor": ["cuirass_light", "helmet_light", "boots_light"]
        }
class PilgrimKit(WeaponArmorKit):
    """
    This kit is designed for a pilgrim class character. It includes a staff and a religious symbol.
    """
    def __init__(self):
        self.items = {
            "weapon": ["staff"],
            "misc": ["religious_symbol"]
        }
class ScoutKit(WeaponArmorKit):
    """
    This kit is designed for a scout class character. It includes a dagger, a set of light armor, and a lockpick.
    """
    def __init__(self):
        self.items = {
                "weapon": ["dagger"],
                "armor": ["cuirass_light", "boots_light"],
                "misc": ["lockpick"]
        }
class SorcererKit(WeaponArmorKit):
    """
    This kit is designed for a sorcerer class character. It includes a spell book with two spells and a sorcerer's robe.
    """
    def __init__(self):
        self.items = {
            "spell_book": ["tome_of_summoning", "tome_of_mystic_shield"],
            "robe": ["sorcerer_robe"]
        }
class SpellswordLongSwordKit(WeaponArmorKit):
    """
    This kit is designed for a spellsword class character. It includes a long sword, a spell book with two spells, and a set of medium armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["long_sword"],
            "spell_book": ["tome_of_flame_aura", "tome_of_healing"],
            "armor": ["cuirass_medium", "helmet_medium", "boots_medium"]
        }
class SpellswordMaceKit(WeaponArmorKit):
    """
    This kit is designed for a spellsword class character. It includes a mace, a spell book with a levitation spell, and a set of medium armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["mace"],
            "spell_book": ["tome_of_levitation"],
            "armor": ["cuirass_medium", "helmet_medium", "boots_medium"]
        }
class MonkKit(WeaponArmorKit):
    """
    This kit is designed for a monk class character. It includes a staff and a monk's robe.
    """
    def __init__(self):
        self.items = {
            "weapon": ["staff"],
            "robe": ["monk_robe"]
        }

class AssassinKit(WeaponArmorKit):
    """
    This kit is designed for an assassin class character. It includes a dagger, a short sword, a set of light armor, and a lockpick.
    """
    def __init__(self):
        self.items = {
            "weapon": ["dagger", "short_sword"],
            "armor": ["cuirass_light", "helmet_light", "boots_light"],
            "misc": ["lockpick"]
        }

class BardMediumKit(WeaponArmorKit):
    """
    This kit is designed for a bard class character. It includes a lute, a flute, a short sword, and a set of medium armor.
    """
    def __init__(self):
        self.items = {
            "instrument": ["lute", "flute"],
            "weapon": ["short_sword"],
            "armor": ["cuirass_medium", "boots_medium"]
        }
class BardLightKit(WeaponArmorKit):
    """
    This kit is designed for a bard class character. It includes a lute, a flute, a dagger, and a set of light armor.
    """
    def __init__(self):
        self.items = {
            "instrument": ["lute", "flute"],
            "weapon": ["dagger"],
            "armor": ["cuirass_light", "boots_light"]
        }
class BattleMageMediumKit(WeaponArmorKit):
    """
    This kit is designed for a battlemage class character. It includes a staff, a long sword, a spell book with two spells, and a set of medium armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["staff", "long_sword"],
            "spell_book": ["tome_of_lightning_bolt", "tome_of_frostbite"],
            "armor": ["cuirass_medium", "helmet_medium", "boots_medium"]
        }
class BattleMageHeavyKit(WeaponArmorKit):
    """
    This kit is designed for a battlemage class character. It includes a mace, a spell book with a fireball spell, and a set of heavy armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["mace"],
            "spell_book": ["tome_of_fireball"],
            "armor": ["cuirass_heavy", "helmet_heavy", "greaves_heavy"]
        }
class AgentKit(WeaponArmorKit):
    """
    This kit is designed for an agent class character. It includes a dagger, a set of light armor, and a lockpick.
    """
    def __init__(self):
        self.items = {
            "weapon": ["dagger"],
            "armor": ["cuirass_light", "boots_light"],
            "misc": ["lockpick"]
        }
class ArcherKit(WeaponArmorKit):
    """
    This kit is designed for an archer class character. It includes a bow, arrows, and a set of light armor.
    """
    def __init__(self):
        self.items = {
            "weapon": ["bow"],
            "misc": ["arrow"],
            "armor": ["cuirass_light", "boots_light"]
        }
class HealerKit(WeaponArmorKit):
    """
    This kit is designed for a healer class character. It includes a spell book with two healing spells and healing potions.
    """
    def __init__(self):
        self.items = {
            "spell_book": ["tome_of_healing", "tome_of_purification"],
            "misc": ["healing_potions"]
        }
class RogueKit(WeaponArmorKit):
    """
    This kit is designed for a rogue class character. It includes a short sword, a dagger, a set of light armor, a lockpick, and a poison vial.
    """
    def __init__(self):
        self.items = {
            "weapon": ["short_sword", "dagger"],
            "armor": ["cuirass_light"],
            "misc": ["lockpick", "poison_vial"]
        }
class MageSpellBookKit(WeaponArmorKit):
    """
    This kit is designed for a mage class character. It includes a spell book with two spells and a mage's robe.
    """
    def __init__(self):
        self.items = {
            "spell_book": ["tome_of_fireball", "tome_of_levitation"],
            "robe": ["mage_robe"]
        }
class MageStaffKit(WeaponArmorKit):
    """
    This kit is designed for a mage class character. It includes a staff and a mage's robe.
    """
    def __init__(self):
        self.items = {
            "weapon": ["staff"],
            "robe": ["mage_robe"]
        }
class ThiefKit(WeaponArmorKit):
    """
    This kit is designed for a thief class character. It includes a dagger, a short sword, a set of light armor, and a lockpick.
    """
    def __init__(self):
        self.items = {
            "weapon": ["dagger", "short_sword"],
            "armor": ["cuirass_light", "helmet_light", "boots_light"],
            "misc": ["lockpick"]
        }
class WitchhunterMediumKit(WeaponArmorKit):
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
class WitchhunterLightKit(WeaponArmorKit):
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