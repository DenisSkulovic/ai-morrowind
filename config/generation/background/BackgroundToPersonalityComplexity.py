class BackgroundToPersonalityComplexity:
    """
    This class represents the mapping of character backgrounds to their personality complexity.
    Each personality complexity is represented by a tuple of two values: mean and standard deviation.
    """
    def __init__(self):
        self._config = {
            "commoner": (2, 1),
            "guard": (3, 1.5),
            "mage": (5, 1),
            "necromancer": (6, 0.5),
            "telvanni_mage": (6, 0.5),
            "noble": (5, 1.5),
            "adventurer": (4, 1.5),
            "outlaw": (4, 1.5),
            "hermit": (3, 2),
            "ashlander": (4, 1.5),
            "sadrith_mora_scholar": (5, 1),
            "redoran_warrior": (4, 1.5),
            "hlaalu_trader": (4, 1.5),
            "balmora_citizen": (2, 1),
            "vivec_city_monk": (5, 1),
            "imperial_legionnaire": (3, 1.5),
            "dwemer_researcher": (6, 0.5),
            "morrowind_pilgrim": (3, 1.5),
            "ebony_mine_worker": (1, 0.5),
            "daedra_worshipper": (5, 1.5),
            "vampire_hunter": (4, 1.5),
            "buoyant_armiger": (4, 1.5),
            "silt_strider_operator": (2, 1),
            "mournhold_royalty": (6, 1),
            "fisherman": (1, 0.5),
            "alchemist": (5, 1),
            "spellwright": (5, 1),
            "smuggler": (4, 1.5),
            "khajiit_caravaneer": (3, 1.5),
            "argonian_slave": (1, 0.5)
        }
        
    def get_mean_and_std_for_background(self, background: str) -> tuple[int, int]:
        """
        This method returns the mean and standard deviation of personality complexity for a given character background.
        
        Parameters:
        background (str): The background of the character. This should be a string representing the background of the character.
        
        Returns:
        tuple[int, int]: A tuple containing two integers. The first integer is the mean personality complexity for the specified background. 
        The second integer is the standard deviation of personality complexity for the specified background.
        
        For example, for a 'mage' background, the returned tuple might look like this:
        (5, 1)
        """
        if background not in self._config:
            raise ValueError(f"Background '{background}' not found in configuration.")
        return self._config[background]
