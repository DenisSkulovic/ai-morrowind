class BackgroundToClassMapProbabilities:
    """
    This class represents the mapping of character backgrounds to their class probabilities.
    Each class is represented by a tuple of 18 values: each value represents a probability of a background to have a class.
    """
    def __init__(self):
        self._cols = {"warrior": 0, "mage": 1, "thief": 2, "monk": 3, "assassin": 4, "barbarian": 5, "bard": 6, "crusader": 7, "knight": 8, "rogue": 9, "scout": 10, "sorcerer": 11, "spellsword": 12, "witchhunter": 13, "battlemage": 14, "healer": 15, "nightblade": 16, "archer": 17}
        self._config = {
            "commoner": (0, 0, 0.25, 0, 0, 0, 0.20, 0, 0, 0, 0.15, 0, 0, 0, 0, 0, 0, 0),
            "guard": (0.15, 0, 0, 0, 0, 0, 0, 0.25, 0.35, 0, 0, 0, 0, 0, 0, 0, 0, 0.20),
            "mage": (0, 0.45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.10, 0.15, 0.05, 0, 0, 0, 0),
            "necromancer": (0, 0.20, 0, 0, 0.10, 0, 0, 0, 0, 0, 0, 0, 0, 0.30, 0, 0, 0.40, 0),
            "noble": (0, 0, 0, 0, 0, 0, 0.20, 0.25, 0.30, 0, 0, 0, 0, 0, 0, 0.10, 0, 0.15),
            "adventurer": (0.20, 0, 0.20, 0, 0, 0, 0.10, 0, 0, 0, 0.15, 0.10, 0, 0, 0, 0, 0, 0.25),
            "outlaw": (0, 0, 0.35, 0, 0.20, 0, 0.10, 0, 0, 0, 0.10, 0, 0, 0, 0, 0, 0, 0.25),
            "hermit": (0, 0.25, 0, 0.30, 0, 0, 0, 0, 0, 0.20, 0.10, 0, 0, 0, 0, 0, 0, 0),
            "ashlander": (0.20, 0, 0.15, 0, 0, 0, 0, 0, 0, 0, 0.10, 0, 0, 0, 0, 0, 0, 0.25),
            "sadrith_mora_scholar": (0, 0.40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.20, 0.10, 0.05, 0, 0, 0, 0.25),
            "redoran_warrior": (0.20, 0, 0, 0, 0, 0, 0, 0, 0.40, 0, 0.05, 0, 0, 0, 0, 0, 0, 0.35),
            "hlaalu_trader": (0, 0, 0.15, 0, 0, 0, 0.30, 0, 0, 0.35, 0, 0, 0, 0, 0, 0, 0, 0.20),
            "balmora_citizen": (0, 0, 0.10, 0, 0, 0.20, 0.20, 0, 0, 0.25, 0.30, 0, 0, 0, 0, 0, 0, 0.15),
            "vivec_city_monk": (0, 0, 0, 0.50, 0, 0, 0, 0, 0, 0.10, 0, 0, 0, 0, 0, 0.25, 0, 0.15),
            "imperial_legionnaire": (0.05, 0, 0, 0, 0, 0, 0, 0, 0.40, 0.05, 0, 0, 0, 0, 0, 0, 0, 0.50),
            "dwemer_researcher": (0, 0.35, 0.10, 0, 0, 0, 0, 0, 0, 0, 0, 0.10, 0.25, 0, 0, 0.20, 0, 0),
            "morrowind_pilgrim": (0, 0, 0, 0.40, 0, 0.10, 0.10, 0, 0, 0.05, 0, 0, 0, 0, 0, 0.20, 0.15, 0),
            "ebony_mine_worker": (0.20, 0, 0.20, 0, 0, 0.10, 0, 0, 0.30, 0.15, 0, 0, 0, 0, 0, 0, 0, 0.15),
            "daedra_worshipper": (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.30, 0, 0.15, 0.20, 0.35),
            "vampire_hunter": (0, 0, 0.05, 0, 0, 0, 0, 0, 0.20, 0, 0, 0, 0, 0.35, 0, 0, 0, 0.40),
            "buoyant_armiger": (0, 0, 0, 0, 0, 0, 0, 0, 0.20, 0.05, 0, 0, 0, 0, 0, 0, 0, 0.75),
            "silt_strider_operator": (0, 0, 0.10, 0, 0, 0, 0.10, 0, 0, 0.25, 0.40, 0, 0, 0, 0, 0, 0, 0.15),
            "mournhold_royalty": (0, 0.20, 0, 0, 0, 0.30, 0.10, 0.15, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0),
            "fisherman": (0.20, 0, 0.25, 0, 0, 0, 0.10, 0, 0, 0.15, 0.30, 0, 0, 0, 0, 0, 0, 0),
            "alchemist": (0, 0.40, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.30, 0, 0.30),
            "spellwright": (0, 0.35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0.25, 0.05, 0, 0.20, 0, 0),
            "smuggler": (0, 0, 0.05, 0, 0.20, 0, 0.10, 0, 0, 0.30, 0.10, 0, 0, 0, 0, 0, 0.25, 0),
            "khajiit_caravaneer": (0, 0, 0.05, 0, 0, 0, 0.10, 0, 0, 0.30, 0.35, 0, 0, 0, 0, 0, 0, 0.20),
            "argonian_slave": (0, 0, 0.10, 0, 0, 0, 0.10, 0, 0, 0.30, 0.25, 0, 0, 0, 0, 0, 0, 0.25),
        }
        
    def get_probability(self, background: str, character_class: str) -> float:
        """
        This method returns the probability of a character with a given background to have a certain class.
        The method takes two parameters: the background of the character and the class of the character.
        The background parameter should be a string representing the background of the character.
        The character_class parameter should be a string representing the class of the character.
        The method returns a float representing the probability of the character with the given background to have the given class.
        """
        if background not in self._config:
            raise ValueError(f"Background '{background}' not found in configuration.")
        if character_class not in self._cols:
            raise ValueError(f"Class '{character_class}' not found in configuration.")
        index = self._cols[character_class]
        return self._config[background][index]
        
    def get_class_probabilities(self, background: str) -> dict[str, float]:
        """
        This method returns a dictionary with classes as keys and their probabilities as values for a given background.
        The method takes one parameter: the background of the character.
        The background parameter should be a string representing the background of the character.
        The method returns a dictionary where keys are classes and values are probabilities for the character with the given background.
        The returned dictionary has the structure: {'class1': probability1, 'class2': probability2, ...}
        For example, for a 'mage' background, the returned dictionary might look like this:
        {'mage': 0.45, 'sorcerer': 0.10, 'spellsword': 0.15, 'witchhunter': 0.05}
        """
        if background not in self._config:
            raise ValueError(f"Background '{background}' not found in configuration.")
        probabilities = self._config[background]
        return {class_: prob for class_, prob in zip(self._cols.keys(), probabilities) if prob > 0}