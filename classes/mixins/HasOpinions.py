from classes.creatures.Creature import Creature


class HasOpinions(Creature):
    def set_opinions(self, opinions):
        self.opinions = opinions
        
    def get_opinions(self, opinions):
        self.opinions = opinions
        
    def change_opinion(self, other_character_name, change_amount):
        """
        Modify the opinion of the character about another character.
        :param other_character_name: Name of the other character.
        :param change_amount: Amount to change the opinion by (can be negative).
        """
        if other_character_name in self.opinions:
            self.opinions[other_character_name] = min(max(self.opinions[other_character_name] + change_amount, -100), 100)
        else:
            self.opinions[other_character_name] = min(max(change_amount, -100), 100)
            
    def get_opinion(self, other_character_name):
        """
        Get the opinion about another character.
        :param other_character_name: Name of the other character.
        :return: Opinion value, or None if not known.
        """
        return self.opinions.get(other_character_name)
    
    def adjust_opinion_based_on_traits(self, other_character):
        # Logic to adjust opinion based on the combination of traits between two characters
        pass
