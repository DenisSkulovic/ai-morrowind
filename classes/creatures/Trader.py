from classes.creatures.character.Character import Character
from classes.mixins.CanTrade import CanTrade

class Trader(Character, CanTrade):
    def __init__(self, name, race):
        super().__init__(name, race, 'Trader', 'NA', 'NA', {}, {})

    # Trader-specific methods, such as adjusting prices based on disposition
