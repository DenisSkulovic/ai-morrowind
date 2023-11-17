

from classes.creatures.Creature import Creature


class HasExperience(Creature):
    def get_experience(self):
        return self.experience_level
    def set_experience(self, experience_level):
        self.experience_level = experience_level
   