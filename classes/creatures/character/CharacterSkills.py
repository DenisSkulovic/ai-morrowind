class CharacterSkills:
    
    def __init__(self):
        self.skills = {}
        pass
    
    def get_skill(self, skill: str) -> int:
        return self.skills[skill]
    
    def set_skill(self, skill: str, val: int) -> None:
        self.skills[skill] = val
