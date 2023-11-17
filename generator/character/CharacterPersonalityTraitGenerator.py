import random
from classes.creatures.character.Character import Character
from classes.creatures.character.CharacterPersonalityTraits import CharacterPersonalityTraits
from enum.traits import courage_neutral_traits, courage_traits, cowardice_traits, immorality_traits, intelligence_neutral_traits, intelligence_traits, morality_neutral_traits, morality_traits, unintelligence_traits

class CharacterPersonalityTraitGenerator:
    
    def generate_personality_traits(self, character: Character, threshold=5) -> CharacterPersonalityTraits:
        """
        Generate personality traits for a character based on their morality, intelligence, and courage.
        The threshold parameter (default 5) is the middle ground for morality, intelligence, and courage, which range from 0 to 10.
        The function first determines the dominant category for each dimension (morality, intelligence, courage) based on whether the character's score is above the threshold.
        It then samples traits from the dominant category. If the number of dominant traits is less than the required traits per dimension, it fills the rest with neutral traits.
        The resulting traits are a combination of moral, intelligent, and courageous traits.
        """
        traits = CharacterPersonalityTraits()

        # Calculate the number of traits per dimension
        traits_per_dimension = character.personality_complexity // 3

        # Determine the dominant category for each dimension
        moral_dominant = character.morality > threshold
        intelligent_dominant = character.intelligence > threshold
        courageous_dominant = character.courage > threshold

        # Sample dominant and non-dominant traits
        moral_traits: list[str] = random.sample(morality_traits if moral_dominant else immorality_traits, traits_per_dimension)
        intelligent_traits: list[str] = random.sample(intelligence_traits if intelligent_dominant else unintelligence_traits, traits_per_dimension)
        courageous_traits: list[str] = random.sample(courage_traits if courageous_dominant else cowardice_traits, traits_per_dimension)

        # Fill with neutral traits if dominant traits are not enough
        if len(moral_traits) < traits_per_dimension:
            morality_neutral_traits_sample: list[str] = random.sample(morality_neutral_traits, traits_per_dimension - len(moral_traits))
            for trait in morality_neutral_traits_sample:
                traits.set_morality_trait(trait)
        
        if len(intelligent_traits) < traits_per_dimension:
            intelligence_neutral_traits_sample: list[str] = random.sample(intelligence_neutral_traits, traits_per_dimension - len(intelligent_traits))
            intelligent_traits += intelligence_neutral_traits_sample

        if len(courageous_traits) < traits_per_dimension:
            courage_neutral_traits_sample: list[str] = random.sample(courage_neutral_traits, traits_per_dimension - len(courageous_traits))
            courageous_traits += courage_neutral_traits_sample

        # Combine all traits
        traits = moral_traits + intelligent_traits + courageous_traits

        return traits