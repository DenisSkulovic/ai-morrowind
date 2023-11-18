class BackgroundCharacteristics:
    """
    This class represents the mapping of character backgrounds to their characteristic probabilities.
    Each characteristic is represented by a tuple of two values: mean and standard deviation.
    These characteristics are used to generate personality traits and influence character behavior in the game.
    The characteristics are:
    - morality: 0 to 10, higher values represent higher morality.
    - intelligence: 0 to 10, higher values represent higher intelligence.
    - courage: 0 to 10, higher values represent higher courage.
    - talkativeness: 0 to 10, higher values represent higher talkativeness. Influences the length of conversation and its responses.
    - extraversion: 0 to 10, higher values represent higher extraversion. Reflects if a character is more reflective of oneself or outward oriented.
    - patience: 0 to 10, higher values represent higher patience.
    - empathy: 0 to 10, higher values represent higher empathy. Reflects a character's ability to read other people, in the context of this game - to detect personality traits of other characters.
    - openness: 0 to 10, higher values represent higher openness. Reflects a character's readiness to share facts.
    """
    def __init__(self):
        self._index = {"morality": 0, "intelligence": 1, "courage": 2, "talkativeness": 3, "extraversion": 4, "patience": 5, "empathy": 6, "openness": 7}
        self._config = {
            "commoner": ((5, 2),(4, 2), (4, 2), (4, 2), (4, 2), (3, 2), (4, 2), (4, 2),),
            "guard": ((7, 2),(5, 2), (7, 2), (3, 2), (3, 2), (6, 2), (3, 2), (3, 2),),
            "mage": ((7, 2),(10, 2), (5, 2), (3, 2), (3, 2), (5, 2), (4, 2), (3, 2),),
            "necromancer": ((2, 2),(10, 2), (5, 2), (2, 2), (2, 2), (4, 2), (2, 2), (2, 2),),
            "telvanni_mage": ((3, 2),(10, 2), (5, 2), (2, 2), (2, 2), (4, 2), (2, 2), (4, 2),),
            "noble": ((5, 2),(7, 2), (5, 2), (4, 2), (5, 2), (4, 2), (4, 2), (4, 2),),
            "adventurer": ((5, 2),(5, 2), (8, 2), (5, 2), (5, 2), (3, 2), (4, 2), (5, 2),),
            "outlaw": ((3, 2),(5, 2), (7, 2), (4, 2), (4, 2), (2, 2), (2, 2), (3, 2),),
            "hermit": ((7, 2),(7, 2), (5, 2), (1, 1), (1, 1), (5, 2), (2, 1), (1, 1),),
            "ashlander": ((5, 2),(5, 2), (7, 2), (2, 1), (2, 1), (4, 2), (3, 1), (2, 1),),
            "sadrith_mora_scholar": ((7, 2),(8, 2), (3, 2), (4, 2), (2, 1), (5, 2), (4, 2), (4, 2),),
            "redoran_warrior": ((7, 2),(5, 2), (8, 2), (3, 1), (4, 2), (4, 2), (3, 1), (3, 1),),
            "hlaalu_trader": ((5, 2),(7, 2), (5, 2), (5, 2), (5, 2), (4, 2), (4, 2), (5, 2),),
            "balmora_citizen": ((5, 2),(3, 2), (3, 2), (4, 2), (4, 2), (4, 2), (4, 2), (4, 2),),
            "vivec_city_monk": ((8, 2),(7, 2), (5, 2), (2, 1), (2, 1), (5, 2), (5, 2), (2, 1),),
            "imperial_legionnaire": ((5, 2),(5, 2), (7, 2), (5, 2), (5, 2), (4, 2), (4, 2), (5, 2),),
            "dwemer_researcher": ((5, 2),(7, 2), (4, 2), (2, 1), (2, 1), (5, 2), (5, 2), (2, 1),),
            "morrowind_pilgrim": ((6, 2),(5, 2), (5, 2), (4, 2), (4, 2), (5, 2), (4, 2), (4, 2),),
            "ebony_mine_worker": ((5, 2),(4, 2), (6, 2), (2, 2), (2, 2), (4, 2), (2, 2), (2, 2),),
            "daedra_worshipper": ((3, 2),(5, 2), (6, 2), (5, 2), (5, 2), (2, 2), (2, 2), (5, 2),),
            "vampire_hunter": ((5, 2),(6, 2), (7, 2), (3, 2), (3, 2), (4, 2), (4, 2), (4, 2),),
            "buoyant_armiger": ((7, 2),(7, 2), (8, 2), (4, 2), (4, 2), (3, 2), (3, 2), (4, 2),),
            "silt_strider_operator": ((5, 2),(4, 2), (5, 2), (3, 2), (3, 2), (5, 2), (2, 2), (3, 2),),
            "mournhold_royalty": ((7, 2),(7, 2), (5, 2), (5, 2), (5, 2), (2, 2), (2, 2), (5, 2),),
            "fisherman": ((5, 2),(4, 2), (5, 2), (2, 2), (2, 2), (5, 2), (3, 2), (2, 2),),
            "alchemist": ((5, 2),(7, 2), (4, 2), (4, 2), (2, 2), (6, 2), (5, 2), (4, 2),),
            "spellwright": ((5, 2),(7, 2), (5, 2), (5, 2), (4, 2), (4, 2), (4, 2), (5, 2),),
            "smuggler": ((4, 2),(5, 2), (6, 2), (6, 2), (5, 2), (2, 2), (2, 2), (1, 2),),
            "khajiit_caravaneer": ((5, 2),(5, 2), (5, 2), (7, 2), (6, 2), (4, 2), (4, 2), (5, 2),),
            "argonian_slave": ((6, 2),(4, 2), (4, 2), (3, 2), (3, 2), (5, 2), (5, 2), (3, 2),),
        }
        
    def get_mean_and_std(self, background: str, characteristic: str) -> tuple[int, int]:
        """
        This method returns the mean and standard deviation of a given characteristic for a specific background.
        The method takes two parameters: the background of the character and the characteristic of interest.
        The background parameter should be a string representing the background of the character.
        The characteristic parameter should be a string representing the characteristic of interest.
        The method returns a tuple of two integers: the first integer is the mean and the second integer is the standard deviation of the characteristic for the given background.
        """
        if background not in self._config:
            raise ValueError(f"Background '{background}' not found in configuration.")
        if characteristic not in self._index:
            raise ValueError(f"Characteristic '{characteristic}' not found in configuration.")
        index = self._index[characteristic]
        return self._config[background][index]

