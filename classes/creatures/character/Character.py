from classes.creatures.Creature import Creature
from classes.mixins.CanHaveConversation import CanHaveConversation
from classes.mixins.HasExperience import HasExperience
from classes.mixins.HasInventory import HasInventory
from classes.mixins.HasOpinions import HasOpinions
from classes.mixins.HasPersonalityTraits import HasPersonalityTraits
from classes.mixins.HasSkills import HasSkills



class Character(
    CanHaveConversation,
    HasPersonalityTraits,
    HasInventory,
    HasOpinions,
    HasSkills,
    HasExperience,
    Creature,
):
    # add a list of known NPCs, locations, facts that the NPC can share about any quest, if any. A random NPC shouldn't have any special useful knowledge about any quest.
    # add a map for opinions about any known character. When a character encountres a new NPC, they will have a 0 opinion, but based on conversation and events the opinion must change.
    # trade must also change opinion. Opinion must influence the price
    
    def __init__(
        self,
    ):
        self.name: str = ""
        self.background: str = ""
        self.race: str = ""
        self.birthsign: str = ""
        self.character_class: str = ""
        self.mood: str = 'neutral'  # default mood
        self.talkativeness: int = None  # Scale of 1-10
        self.extraversion: int = None  # Scale of 1-10
        self.patience: int = None  # Scale of 1-10
        self.empathy: int = None  # Scale of 1-10
        self.openness: int = None  # Scale of 1-10
        self.morality: int = None
        self.intelligence: int = None
        self.courage: int = None
        self.culture: str = ""
        self.religion: str = ""
        self.faction: str = ""
        self.personality_complexity = None
        
    def set_name(self, name: str) -> None:
        self.name = name
    def get_name(self) -> str:
        return self.name

    def set_background(self, background: str) -> None:
        self.background = background
    def get_background(self) -> str:
        return self.background

    def set_race(self, race: str) -> None:
        self.race = race
    def get_race(self) -> str:
        return self.race

    def set_birthsign(self, birthsign: str) -> None:
        self.birthsign = birthsign
    def get_birthsign(self) -> str:
        return self.birthsign
        
    def set_class(self, character_class: str) -> None:
        self.character_class = character_class
    def get_class(self) -> str:
        return self.character_class
        
    def set_mood(self, mood: str) -> None:
        self.mood = mood
    def get_mood(self) -> str:
        return self.mood
        
    def set_talkativeness(self, talkativeness: int) -> None:
        self.talkativeness = talkativeness
    def get_talkativeness(self) -> int:
        return self.talkativeness
        
    def set_extraversion(self, extraversion: int) -> None:
        self.extraversion = extraversion
    def get_extraversion(self) -> int:
        return self.extraversion
        
    def set_patience(self, patience: int) -> None:
        self.patience = patience
    def get_patience(self) -> int:
        return self.patience
        
    def set_empathy(self, empathy: int) -> None:
        self.empathy = empathy
    def get_empathy(self) -> int:
        return self.empathy
        
    def set_openness(self, openness: int) -> None:
        self.openness = openness
    def get_openness(self) -> int:
        return self.openness
        
    def set_morality(self, morality: int) -> None:
        self.morality = morality
    def get_morality(self) -> int:
        return self.morality
        
    def set_intelligence(self, intelligence: int) -> None:
        self.intelligence = intelligence
    def get_intelligence(self) -> int:
        return self.intelligence
        
    def set_courage(self, courage: int) -> None:
        self.courage = courage
    def get_courage(self) -> int:
        return self.courage
        
    def set_culture(self, culture: str) -> None:
        self.culture = culture
    def get_culture(self) -> str:
        return self.culture
        
    def set_religion(self, religion: str) -> None:
        self.religion = religion
    def get_religion(self) -> str:
        return self.religion
        
    def set_faction(self, faction: str) -> None:
        self.faction = faction
    def get_faction(self) -> str:
        return self.faction
        
    def set_personality_complexity(self, personality_complexity: int) -> None:
        self.personality_complexity = personality_complexity
    def get_personality_complexity(self) -> int:
        return self.personality_complexity

    def __str__(self):
        # Method to display character information
        print(f"Name: {self.name}")
        print(f"Race: {self.race}, Class: {self.character_class}, Level: {self.experience_level}")
        print(f"Attributes: {self.attributes}")
        print(f"Skills: {self.get_skills()}")
        print(f"Inventory: {self.get_inventory().items}")
        print(f"Personality Traits: {self.personality_traits}")
        print(f"Opinion of other characters: ")
        for other_character, opinion in self.get_opinions().items():
            character_info += f" - {other_character}: {opinion}\n"
        return character_info
    

    def update_mood(self, new_mood):
        self.current_mood = new_mood
``
