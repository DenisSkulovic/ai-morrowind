from classes.creatures.character.Character import Character
from config.generation.background.background_to_class_map_probabilities import background_to_class_map_probabilities
from enum.class_enum import class_enum
from enum.background_type_enum import background_type_enum
import random

class CharacterClassGenerator:
    
    def __init__(self):
        pass
    
    def generate_class(self, character: Character) -> str:
        background = character.get_background()
        class_probabilities = background_to_class_map_probabilities[background]
        classes = list(class_probabilities.keys())
        probabilities = list(class_probabilities.values())
        chosen_class = random.choices(classes, probabilities)[0]
        return class_enum[chosen_class]
