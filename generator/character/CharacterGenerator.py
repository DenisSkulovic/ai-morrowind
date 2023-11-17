import random
from classes.Inventory import Inventory
from classes.creatures.character.Character import Character
from classes.creatures.character.CharacterAttributes import CharacterAttributes
from classes.creatures.character.CharacterPersonalityTraits import CharacterPersonalityTraits
from classes.creatures.character.CharacterProfile import CharacterProfile
from classes.creatures.character.CharacterSkills import CharacterSkills
from config.generation.attributes import attributes_base_config, attributes_class_modifiers_config, attributes_experience_level_modifiers
from config.generation.background import background_to_characteristics_probabilities
from config.generation.location.pop_config import FINISH_________ME
from enum.birthsign_enum import birthsign_enum
from generator.character.CharacterClassGenerator import CharacterClassGenerator
from generator.character.CharacterInventoryGenerator import CharacterInventoryGenerator
from generator.character.CharacterPersonalityTraitGenerator import CharacterPersonalityTraitGenerator
from generator.character.CharacterSkillGenerator import CharacterSkillGenerator
from generator.character.CharacterTopicGenerator import CharacterTopicGenerator




class CharacterGeneratorOptions:
    def __init__(
        self,
        profile: CharacterProfile,
        personality_complexity: int = 6,
        biography_facts = None,
        experience_level = None,
        character_class = None,
        morality = None,
        intelligence = None,
        courage = None,
        birthsign = None,
    ):
        self.profile = profile
        self.personality_complexity = personality_complexity
        self.morality = morality
        self.intelligence = intelligence
        self.courage = courage
        self.character_class = character_class
        self.experience_level = experience_level
        self.biography_facts = biography_facts
        self.birthsign = birthsign


class CharacterGenerator:
    def __init__(
        self,
        options: CharacterGeneratorOptions,
        specialization_bonus = 15,
        inventory_generator = CharacterInventoryGenerator(),
        trait_generator = CharacterPersonalityTraitGenerator(),
        skill_generator = CharacterSkillGenerator(),
        class_generator = CharacterClassGenerator(),
        topic_generator = CharacterTopicGenerator(),
    ):
        self._options = options
        self._specialization_bonus = specialization_bonus
        self._inventory_generator = inventory_generator
        self._trait_generator = trait_generator
        self._skill_generator = skill_generator
        self._class_generator = class_generator
        self._topic_generator = topic_generator
    
    def set_options(self, options: CharacterGeneratorOptions) -> None:
        self._options = options
    def get_options(self) -> CharacterGeneratorOptions:
        return self._options

    def generate_character(self):
        character = Character()
        
        # USE DATA FROM PROFILE
        character.set_background(self._options.profile.background)
        character.set_race(self._options.profile.race)
        character.set_culture(self._options.profile.culture)
        character.set_religion(self._options.profile.religion)
        character.set_faction(self._options.profile.faction)
        
        # CHARACTERISTICS
        characteristics = self._generate_characteristics(character)
        character.set_morality(characteristics["morality"])
        character.set_intelligence(characteristics["intelligence"])
        character.set_courage(characteristics["courage"])
        character.set_talkativeness(characteristics["talkativeness"])
        character.set_extraversion(characteristics["extraversion"])
        character.set_patience(characteristics["patience"])
        character.set_empathy(characteristics["empathy"])
        character.set_openness(characteristics["openness"])

        # EXPERIENCE
        experience: str = self._generate_experience(character)
        character.set_experience(experience)

        # BIRTHSIGN
        birthsign: str = self._generate_birthsign(character)
        character.set_birthsign(birthsign)

        # CLASS
        character_class: str = self._class_generator.generate_class(character)
        character.set_class(character_class)

        # SKILLS
        skills: CharacterSkills = self._skill_generator.generate_skills(character)
        character.set_skills(skills)

        # INVENTORY
        inventory: Inventory = self._inventory_generator.generate_inventory(character)
        character.set_inventory(inventory)

        # TRAITS
        traits: CharacterPersonalityTraits = self._trait_generator.generate_personality_traits(character)
        character.set_personality_traits(traits)


        # KNOWLEDGE
        knowledge = self._determine_knowledge_of_world(character)
        character.set_knowledge(knowledge)
        
        # TOPICS
        topics = self._topic_generator.generate_character_topics(character)
        character.set_topics(topics)

        # ATTRIBUTES
        attributes: CharacterAttributes = self._generate_attributes(character)
        character.set_attributes(attributes)
        
        return character

    def _generate_birthsign(self) -> str:
        if self._options.birthsign:
            return self._options.birthsign
        else:
            return random.sample(birthsign_enum.keys(), 1)

    def _generate_characteristics(self, character: Character) -> dict[str, int]:
        # Generate characteristics based on character's background
        background = character.get_background()
        probabilities = background_to_characteristics_probabilities[background]

        characteristics = {}
        for characteristic in probabilities:
            characteristics[characteristic] = max(1, min(10, round(random.gauss(probabilities[characteristic]["mean"], probabilities[characteristic]["std"]))))

        return characteristics

    def _generate_attributes(self, character: Character) -> CharacterAttributes:
        attributes = CharacterAttributes()

        base_attributes = attributes_base_config[character.get_race()].copy()

        class_modifiers = attributes_class_modifiers_config[character.get_character_class()]
        experience_modifiers = attributes_experience_level_modifiers.get(self.get_experience(), {"health": 0, "mana": 0, "stamina": 0})

        # Calculate final attributes
        health: int = base_attributes["health"] + class_modifiers["health"] + experience_modifiers["health"],
        mana: int = base_attributes["mana"] + class_modifiers["mana"] + experience_modifiers["mana"],
        stamina: int = base_attributes["stamina"] + class_modifiers["stamina"] + experience_modifiers["stamina"]
        
        attributes.set_health(health)
        attributes.set_mana(mana)
        attributes.set_stamina(stamina)

        return attributes
    
    def _determine_knowledge_of_world(self, character: Character):
        # TODO: Implement the logic to determine the character's knowledge of the world
        pass
