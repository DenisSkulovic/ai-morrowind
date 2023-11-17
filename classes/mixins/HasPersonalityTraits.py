from classes.creatures.Creature import Creature
from classes.creatures.character.CharacterPersonalityTraits import CharacterPersonalityTraits


class HasPersonalityTraits(Creature):
    def set_personality_traits(self, personality_traits: CharacterPersonalityTraits) -> None:
        self.personality_traits = personality_traits
    def get_personality_traits(self) -> CharacterPersonalityTraits:
        return self.personality_traits
