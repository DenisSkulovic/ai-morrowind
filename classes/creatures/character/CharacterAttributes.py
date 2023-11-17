class CharacterAttributes:
    
    def __init__(self):
        self.attributes = {
            "health": 0,
            "mana": 0,
            "stamina": 0,
        }
        
    def get_health(self) -> int:
        return self.attributes["health"]
    def set_health(self, val: int) -> None:
        self.attributes["health"] = val
        
    def get_mana(self) -> int:
        return self.attributes["mana"]
    def set_mana(self, val: int) -> None:
        self.attributes["mana"] = val
        
    def get_stamina(self) -> int:
        return self.attributes["stamina"]
    def set_stamina(self, val: int) -> None:
        self.attributes["stamina"] = val