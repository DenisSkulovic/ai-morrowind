from classes.creatures.Creature import Creature


class HasSkills(Creature):
    def __init__():
        super().__init__()
    def set_skills(self, skills):
        self.skills = skills
    def get_skills(self):
        return self.skills
    def update_skill(self, skill, amount):
        # Method to update skill values
        if skill in self.skills:
            self.skills[skill] += amount
       