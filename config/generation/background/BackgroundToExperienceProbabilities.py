class BackgroundToExperienceProbabilities:
    """
    This class represents the mapping of character backgrounds to their experience level probabilities.
    Each experience level probability is represented by a tuple of six values: 
    - beginner: 0 to 1, higher values represent higher probability of being a beginner.
    - amateur: 0 to 1, higher values represent higher probability of being an amateur.
    - adept: 0 to 1, higher values represent higher probability of being an adept.
    - expert: 0 to 1, higher values represent higher probability of being an expert.
    - master: 0 to 1, higher values represent higher probability of being a master.
    - legend: 0 to 1, higher values represent higher probability of being a legend.
    """
    def __init__(self):
        self._index = {"beginner":0, "amateur": 1, "adept": 2, "expert": 3, "master": 4, "legend": 5}
        self._config = {
            "commoner": (0.50, 0.40, 0.10, 0.00, 0.00, 0.00),
            "guard": (0.00, 0.50, 0.40, 0.10, 0.00, 0.00),
            "mage": (0.00, 0.30, 0.40, 0.30, 0.00, 0.00),
            "necromancer": (0.00, 0.00, 0.40, 0.50, 0.10, 0.00),
            "telvanni_mage": (0.00, 0.00, 0.00, 0.40, 0.30, 0.30),
            "noble": (0.00, 0.40, 0.40, 0.20, 0.00, 0.00),
            "adventurer": (0.00, 0.00, 0.40, 0.40, 0.20, 0.00),
            "outlaw": (0.00, 0.00, 0.50, 0.40, 0.10, 0.00),
            "hermit": (0.40, 0.40, 0.20, 0.00, 0.00, 0.00),
            "ashlander": (0.00, 0.00, 0.50, 0.40, 0.10, 0.00),
            "sadrith_mora_scholar": (0.00, 0.00, 0.30, 0.50, 0.20, 0.00),
            "redoran_warrior": (0.00, 0.00, 0.40, 0.40, 0.20, 0.00),
            "hlaalu_trader": (0.00, 0.30, 0.50, 0.20, 0.00, 0.00),
            "balmora_citizen": (0.50, 0.40, 0.10, 0.00, 0.00, 0.00),
            "vivec_city_monk": (0.00, 0.00, 0.40, 0.40, 0.20, 0.00),
            "imperial_legionnaire": (0.00, 0.00, 0.50, 0.40, 0.10, 0.00),
            "dwemer_researcher": (0.00, 0.00, 0.00, 0.40, 0.50, 0.10),
            "morrowind_pilgrim": (0.00, 0.40, 0.40, 0.20, 0.00, 0.00),
            "ebony_mine_worker": (0.60, 0.30, 0.10, 0.00, 0.00, 0.00),
            "daedra_worshipper": (0.00, 0.30, 0.40, 0.20, 0.10, 0.00),
            "vampire_hunter": (0.00, 0.00, 0.40, 0.40, 0.20, 0.00),
            "buoyant_armiger": (0.00, 0.00, 0.00, 0.40, 0.40, 0.20),
            "silt_strider_operator": (0.30, 0.50, 0.20, 0.00, 0.00, 0.00),
            "mournhold_royalty": (0.00, 0.30, 0.40, 0.30, 0.00, 0.00),
            "fisherman": (0.40, 0.40, 0.20, 0.00, 0.00, 0.00),
            "alchemist": (0.00, 0.00, 0.40, 0.40, 0.20, 0.00),
            "spellwright": (0.00, 0.00, 0.30, 0.50, 0.20, 0.00),
            "smuggler": (0.00, 0.40, 0.40, 0.20, 0.00, 0.00),
            "khajiit_caravaneer": (0.00, 0.40, 0.40, 0.20, 0.00, 0.00),
            "argonian_slave": (0.70, 0.30, 0.00, 0.00, 0.00, 0.00),
        }
        
    def get_probability(self, background: str, experience_level: str) -> float:
        """
        This method returns the probability of a given experience level for a specific background.
        
        Parameters:
        background (str): The background of the character. This should be a string representing the background of the character.
        experience_level (str): The experience level of interest. This should be a string representing the experience level of interest.
        
        Returns:
        float: The probability of the given experience level for the specified background. This is a float value between 0 and 1.
        """
        if background not in self._config:
            raise ValueError(f"Background '{background}' not found in configuration.")
        if experience_level not in self._index:
            raise ValueError(f"Experience level '{experience_level}' not found in configuration.")
        index = self._index[experience_level]
        return self._config[background][index]

    def get_background_probabilities(self, background: str) -> dict[str, float]:
        """
        This method returns a dictionary with experience levels as keys and their probabilities as values for a given background.
        The method takes one parameter: the background of the character.
        The background parameter should be a string representing the background of the character.
        The method returns a dictionary where keys are experience levels and values are probabilities for the character with the given background.
        The returned dictionary has the structure: {'beginner': probability1, 'amateur': probability2, ...}
        For example, for a 'mage' background, the returned dictionary might look like this:
        {'beginner': 0.00, 'amateur': 0.30, 'adept': 0.40, 'expert': 0.30, 'master': 0.00, 'legend': 0.00}
        """
        if background not in self._config:
            raise ValueError(f"Background '{background}' not found in configuration.")
        probabilities = self._config[background]
        return {experience_level: prob for experience_level, prob in zip(self._index.keys(), probabilities) if prob > 0}
