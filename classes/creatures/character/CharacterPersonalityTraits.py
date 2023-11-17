from typing import List, Set


class CharacterPersonalityTraits:
    
    def __init__(self):
        morality: Set[str] = {}
        intelligence: Set[str] = {}
        courage: Set[str] = {}
        self.traits = {
            "morality": morality,
            "intelligence": intelligence,
            "courage": courage,
        }
        
    def get_morality_traits(self) -> Set[str]:
        return self.traits.morality
    def set_morality_trait(self, trait: str) -> None:
        self.traits.morality.set(trait)
        
    def get_courage_traits(self) -> Set[str]:
        return self.traits.courage
    def set_courage_trait(self, trait: str) -> None:
        self.traits.courage.set(trait)
        
    def get_intelligence_traits(self) -> Set[str]:
        return self.traits.intelligence
    def set_intelligence_trait(self, trait: str) -> None:
        self.traits.intelligence.set(trait)

    def get_all_traits_arr(self) -> List[str]:
        # TODO
        pass