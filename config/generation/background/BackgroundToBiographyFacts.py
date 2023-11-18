from enum.BiographyFactEnum import BiographyFactEnum as BF


class BackgroundToBiographyFacts:
    def __init__(self):
        self._config = {
            "commoner": [
                (BF.POVERTY_STRICKEN_CHILDHOOD, 0.30),
                (BF.SKILLED_ARTISAN, 0.20),
                (BF.STREETWISE_URCHIN, 0.20),
                (BF.LOST_FAMILY, 0.10),
                (BF.MYSTICAL_ENCOUNTER, 0.05),
                (BF.SECRETIVE_PAST, 0.05),
                (BF.ROGUEISH_CHARM, 0.05),
                (BF.NATURAL_BORN_LEADER, 0.05),
            ],
            "guard": [
                (BF.FORMER_MERCENARY, 0.30),
                (BF.VETERAN_OF_BATTLES, 0.25),
                (BF.NATURAL_BORN_LEADER, 0.15),
                (BF.AFFLUENT_UPBRINGING, 0.10),
                (BF.FARMHAND_TURNED_WARRIOR, 0.10),
                (BF.SECRET_LINEAGE, 0.05),
                (BF.MYSTICAL_ENCOUNTER, 0.05),
            ],
            "mage": [
                (BF.GIFTED_APPRENTICE, 0.30),
                (BF.RECLUSIVE_SCHOLAR, 0.25),
                (BF.MYSTICAL_ENCOUNTER, 0.20),
                (BF.FAILED_MAGE, 0.10),
                (BF.BOTCHED_ALCHEMY, 0.05),
                (BF.WHISPERED_PROPHECIES, 0.05),
                (BF.SECRETIVE_PAST, 0.05),
            ],
            "necromancer": [
                (BF.CURSED_BY_BIRTH, 0.30),
                (BF.RECLUSIVE_SCHOLAR, 0.25),
                (BF.SECRETIVE_PAST, 0.20),
                (BF.CULT_ESCAPEE, 0.15),
                (BF.DISGRACED_NOBLE, 0.05),
                (BF.MYSTICAL_ENCOUNTER, 0.05),
            ],
            "telvanni_mage": [
                (BF.GIFTED_APPRENTICE, 0.30),
                (BF.RECLUSIVE_SCHOLAR, 0.25),
                (BF.SECRETIVE_PAST, 0.20),
                (BF.MYSTICAL_ENCOUNTER, 0.10),
                (BF.WHISPERED_PROPHECIES, 0.05),
                (BF.AFFLUENT_UPBRINGING, 0.05),
                (BF.BOTCHED_ALCHEMY, 0.05),
            ],
            "noble": [
                (BF.AFFLUENT_UPBRINGING, 0.40),
                (BF.DISGRACED_NOBLE, 0.20),
                (BF.MYSTERIOUS_BENEFACTOR, 0.15),
                (BF.SECRET_LINEAGE, 0.10),
                (BF.CHARISMATIC_DIPLOMAT, 0.10),
                (BF.FORGOTTEN_ROYALTY, 0.05),
            ],
            "adventurer": [
                (BF.LONE_WANDERER, 0.25),
                (BF.DARING_EXPLORER, 0.20),
                (BF.SHIPWRECK_SURVIVOR, 0.15),
                (BF.ESCAPED_CAPTIVITY, 0.10),
                (BF.WANDERING_MINSTREL, 0.10),
                (BF.NATURAL_BORN_LEADER, 0.10),
                (BF.ILLICIT_TREASURE_HUNTER, 0.10),
            ],
            "outlaw": [
                (BF.STREETWISE_URCHIN, 0.25),
                (BF.ESCAPED_CAPTIVITY, 0.20),
                (BF.ROGUEISH_CHARM, 0.15),
                (BF.ILLICIT_TREASURE_HUNTER, 0.15),
                (BF.EXILED_TRAITOR, 0.10),
                (BF.BOUNTY_HUNTER, 0.10),
                (BF.SECRETIVE_PAST, 0.05),
            ],
            "hermit": [
                (BF.HERMITIC_LIFESTYLE, 0.40),
                (BF.RECLUSIVE_SCHOLAR, 0.20),
                (BF.SECRETIVE_PAST, 0.15),
                (BF.MYSTICAL_ENCOUNTER, 0.10),
                (BF.LOST_FAMILY, 0.10),
                (BF.CURSED_BY_BIRTH, 0.05),
            ],
            "ashlander": [
                (BF.ORPHANED_AT_BIRTH, 0.25),
                (BF.LONE_WANDERER, 0.20),
                (BF.NATURAL_BORN_LEADER, 0.15),
                (BF.LOST_FAMILY, 0.15),
                (BF.MYSTICAL_ENCOUNTER, 0.10),
                (BF.CULT_ESCAPEE, 0.10),
                (BF.HERMITIC_LIFESTYLE, 0.05),
            ],
            "sadrith_mora_scholar": [
                (BF.RECLUSIVE_SCHOLAR, 0.30),
                (BF.GIFTED_APPRENTICE, 0.25),
                (BF.MYSTERIOUS_BENEFACTOR, 0.15),
                (BF.FAILED_MAGE, 0.10),
                (BF.SECRETIVE_PAST, 0.10),
                (BF.WHISPERED_PROPHECIES, 0.10),
            ],
            "redoran_warrior": [
                (BF.FARMHAND_TURNED_WARRIOR, 0.30),
                (BF.VETERAN_OF_BATTLES, 0.25),
                (BF.NATURAL_BORN_LEADER, 0.15),
                (BF.LOST_FAMILY, 0.15),
                (BF.AFFLUENT_UPBRINGING, 0.10),
                (BF.FAMED_DUELIST, 0.05),
            ],
            "hlaalu_trader": [
                (BF.STREETWISE_URCHIN, 0.25),
                (BF.SKILLED_ARTISAN, 0.20),
                (BF.CHARISMATIC_DIPLOMAT, 0.15),
                (BF.ROGUEISH_CHARM, 0.15),
                (BF.POVERTY_STRICKEN_CHILDHOOD, 0.10),
                (BF.SECRETIVE_PAST, 0.10),
                (BF.MYSTERIOUS_BENEFACTOR, 0.05),
            ],
            "balmora_citizen": [
                (BF.POVERTY_STRICKEN_CHILDHOOD, 0.30),
                (BF.SKILLED_ARTISAN, 0.25),
                (BF.STREETWISE_URCHIN, 0.20),
                (BF.LOST_FAMILY, 0.10),
                (BF.MYSTICAL_ENCOUNTER, 0.10),
                (BF.SECRETIVE_PAST, 0.05),
            ],
            "vivec_city_monk": [
                (BF.RELIGIOUS_UPBRINGING, 0.30),
                (BF.MYSTICAL_ENCOUNTER, 0.25),
                (BF.GIFTED_APPRENTICE, 0.15),
                (BF.ORPHANED_AT_BIRTH, 0.10),
                (BF.LOST_FAMILY, 0.10),
                (BF.WHISPERED_PROPHECIES, 0.10),
            ],
            "imperial_legionnaire": [
                (BF.VETERAN_OF_BATTLES, 0.30),
                (BF.FARMHAND_TURNED_WARRIOR, 0.20),
                (BF.NATURAL_BORN_LEADER, 0.15),
                (BF.ESCAPED_CAPTIVITY, 0.15),
                (BF.AFFLUENT_UPBRINGING, 0.10),
                (BF.FAMED_DUELIST, 0.10),
            ],
            "dwemer_researcher": [
                (BF.RECLUSIVE_SCHOLAR, 0.35),
                (BF.MYSTERIOUS_BENEFACTOR, 0.20),
                (BF.GIFTED_APPRENTICE, 0.15),
                (BF.SECRETIVE_PAST, 0.10),
                (BF.LOST_FAMILY, 0.10),
                (BF.INVENTOR_OF_GADGETS, 0.10),
            ],
            "morrowind_pilgrim": [
                (BF.RELIGIOUS_UPBRINGING, 0.30),
                (BF.ORPHANED_AT_BIRTH, 0.20),
                (BF.MYSTICAL_ENCOUNTER, 0.20),
                (BF.LOST_FAMILY, 0.15),
                (BF.NATURAL_BORN_LEADER, 0.10),
                (BF.WHISPERED_PROPHECIES, 0.05),
            ],
            "ebony_mine_worker": [
                (BF.POVERTY_STRICKEN_CHILDHOOD, 0.40),
                (BF.SKILLED_ARTISAN, 0.25),
                (BF.ESCAPED_CAPTIVITY, 0.15),
                (BF.STREETWISE_URCHIN, 0.10),
                (BF.FARMHAND_TURNED_WARRIOR, 0.10),
            ],
            "daedra_worshipper": [
                (BF.CURSED_BY_BIRTH, 0.30),
                (BF.MYSTICAL_ENCOUNTER, 0.25),
                (BF.CULT_ESCAPEE, 0.20),
                (BF.SECRETIVE_PAST, 0.15),
                (BF.ORPHANED_AT_BIRTH, 0.10),
            ],
            "vampire_hunter": [
                (BF.ESCAPED_CAPTIVITY, 0.25),
                (BF.LOST_FAMILY, 0.20),
                (BF.MYSTICAL_ENCOUNTER, 0.20),
                (BF.FORMER_MERCENARY, 0.15),
                (BF.BOUNTY_HUNTER, 0.10),
                (BF.CURSED_BY_BIRTH, 0.10),
            ],
            "buoyant_armiger": [
                (BF.VETERAN_OF_BATTLES, 0.30),
                (BF.NATURAL_BORN_LEADER, 0.25),
                (BF.AFFLUENT_UPBRINGING, 0.15),
                (BF.FAMED_DUELIST, 0.15),
                (BF.RELIGIOUS_UPBRINGING, 0.10),
                (BF.SECRET_LINEAGE, 0.05),
            ],
            "silt_strider_operator": [
                (BF.POVERTY_STRICKEN_CHILDHOOD, 0.35),
                (BF.STREETWISE_URCHIN, 0.25),
                (BF.LONE_WANDERER, 0.15),
                (BF.ROGUEISH_CHARM, 0.15),
                (BF.ESCAPED_CAPTIVITY, 0.10),
            ],
            "mournhold_royalty": [
                (BF.AFFLUENT_UPBRINGING, 0.40),
                (BF.FORGOTTEN_ROYALTY, 0.25),
                (BF.CHARISMATIC_DIPLOMAT, 0.15),
                (BF.SECRET_LINEAGE, 0.10),
                (BF.DISGRACED_NOBLE, 0.10),
            ],
            "fisherman": [
                (BF.POVERTY_STRICKEN_CHILDHOOD, 0.30),
                (BF.LONE_WANDERER, 0.20),
                (BF.SHIPWRECK_SURVIVOR, 0.20),
                (BF.ORPHANED_AT_BIRTH, 0.15),
                (BF.STREETWISE_URCHIN, 0.10),
                (BF.NATURAL_BORN_LEADER, 0.05),
            ],
            "alchemist": [
                (BF.GIFTED_APPRENTICE, 0.30),
                (BF.BOTCHED_ALCHEMY, 0.25),
                (BF.RECLUSIVE_SCHOLAR, 0.20),
                (BF.MYSTERIOUS_BENEFACTOR, 0.15),
                (BF.SECRETIVE_PAST, 0.10),
            ],
            "spellwright": [
                (BF.GIFTED_APPRENTICE, 0.35),
                (BF.FAILED_MAGE, 0.25),
                (BF.MYSTICAL_ENCOUNTER, 0.20),
                (BF.RECLUSIVE_SCHOLAR, 0.10),
                (BF.SECRETIVE_PAST, 0.10),
            ],
            "smuggler": [
                (BF.STREETWISE_URCHIN, 0.30),
                (BF.ILLICIT_TREASURE_HUNTER, 0.25),
                (BF.ROGUEISH_CHARM, 0.20),
                (BF.ESCAPED_CAPTIVITY, 0.15),
                (BF.EXILED_TRAITOR, 0.10),
            ],
            "khajiit_caravaneer": [
                (BF.WANDERING_MINSTREL, 0.30),
                (BF.LONE_WANDERER, 0.25),
                (BF.STREETWISE_URCHIN, 0.20),
                (BF.ROGUEISH_CHARM, 0.15),
                (BF.MYSTICAL_ENCOUNTER, 0.10),
            ],
            "argonian_slave": [
                (BF.ESCAPED_CAPTIVITY, 0.40),
                (BF.POVERTY_STRICKEN_CHILDHOOD, 0.30),
                (BF.CURSED_BY_BIRTH, 0.15),
                (BF.ORPHANED_AT_BIRTH, 0.10),
                (BF.STREETWISE_URCHIN, 0.05),
            ],
        }

    def get_probability(self, background: str, biography_fact: BF) -> float:
        """
        This method returns the probability of a given biography fact for a specific background.
        
        Parameters:
        background (str): The background of the character. This should be a string representing the background of the character.
        biography_fact (BF): The biography fact of interest. This should be an instance of BiographyFactEnum.
        
        Returns:
        float: The probability of the given biography fact for the specified background. This is a float value between 0 and 1.
        """
        if background not in self._config:
            raise ValueError(f"Background '{background}' not found in configuration.")
        for fact, prob in self._config[background]:
            if fact == biography_fact:
                return prob
        return 0.0

    def get_background_biography_facts(self, background: str) -> dict[BF, float]:
        """
        This method returns a dictionary with biography facts as keys and their probabilities as values for a given background.
        The method takes one parameter: the background of the character.
        The background parameter should be a string representing the background of the character.
        The method returns a dictionary where keys are biography facts and values are probabilities for the character with the given background.
        The returned dictionary has the structure: {BiographyFactEnum.FACT: probability1, BiographyFactEnum.FACT2: probability2, ...}
        For example, for a 'mage' background, the returned dictionary might look like this:
        {BiographyFactEnum.GIFTED_APPRENTICE: 0.30, BiographyFactEnum.BOTCHED_ALCHEMY: 0.25, BiographyFactEnum.RECLUSIVE_SCHOLAR: 0.20, BiographyFactEnum.MYSTERIOUS_BENEFACTOR: 0.15, BiographyFactEnum.SECRETIVE_PAST: 0.10}
        """
        if background not in self._config:
            raise ValueError(f"Background '{background}' not found in configuration.")
        return {fact: prob for fact, prob in self._config[background]}
