from enum.ExperienceLevelEnum import ExperienceLevelEnum
from enum.BackgroundTypeEnum import BackgroundTypeEnum as BgE


class BackgroundToExperienceProbabilities:
    """
    This class represents the mapping of character backgrounds to their experience level probabilities.
    Each experience level probability is represented by a tuple of six values: 
    - ExperienceLevelEnum.BEGINNER: 0 to 1, higher values represent higher probability of being a beginner.
    - ExperienceLevelEnum.AMATEUR: 0 to 1, higher values represent higher probability of being an amateur.
    - ExperienceLevelEnum.ADEPT: 0 to 1, higher values represent higher probability of being an adept.
    - ExperienceLevelEnum.EXPERT: 0 to 1, higher values represent higher probability of being an expert.
    - ExperienceLevelEnum.MASTER: 0 to 1, higher values represent higher probability of being a master.
    - ExperienceLevelEnum.LEGEND: 0 to 1, higher values represent higher probability of being a legend.
    """
    def __init__(self):
        self._cols = {ExperienceLevelEnum.BEGINNER:0, ExperienceLevelEnum.AMATEUR: 1, ExperienceLevelEnum.ADEPT: 2, ExperienceLevelEnum.EXPERT: 3, ExperienceLevelEnum.MASTER: 4, ExperienceLevelEnum.LEGEND: 5}
        self._config = {
            BgE.COMMONER: (0.50, 0.40, 0.10, 0.00, 0.00, 0.00),
            BgE.GUARD: (0.00, 0.50, 0.40, 0.10, 0.00, 0.00),
            BgE.MAGE: (0.00, 0.30, 0.40, 0.30, 0.00, 0.00),
            BgE.NECROMANCER: (0.00, 0.00, 0.40, 0.50, 0.10, 0.00),
            BgE.TELVANNI_MAGE: (0.00, 0.00, 0.00, 0.40, 0.30, 0.30),
            BgE.NOBLE: (0.00, 0.40, 0.40, 0.20, 0.00, 0.00),
            BgE.ADVENTURER: (0.00, 0.00, 0.40, 0.40, 0.20, 0.00),
            BgE.OUTLAW: (0.00, 0.00, 0.50, 0.40, 0.10, 0.00),
            BgE.HERMIT: (0.40, 0.40, 0.20, 0.00, 0.00, 0.00),
            BgE.ASHLANDER: (0.00, 0.00, 0.50, 0.40, 0.10, 0.00),
            BgE.SADRITH_MORA_SCHOLAR: (0.00, 0.00, 0.30, 0.50, 0.20, 0.00),
            BgE.REDORAN_WARRIOR: (0.00, 0.00, 0.40, 0.40, 0.20, 0.00),
            BgE.HLAALU_TRADER: (0.00, 0.30, 0.50, 0.20, 0.00, 0.00),
            BgE.BALMORA_CITIZEN: (0.50, 0.40, 0.10, 0.00, 0.00, 0.00),
            BgE.VIVEC_CITY_MONK: (0.00, 0.00, 0.40, 0.40, 0.20, 0.00),
            BgE.IMPERIAL_LEGIONNAIRE: (0.00, 0.00, 0.50, 0.40, 0.10, 0.00),
            BgE.DWEMER_RESEARCHER: (0.00, 0.00, 0.00, 0.40, 0.50, 0.10),
            BgE.MORROWIND_PILGRIM: (0.00, 0.40, 0.40, 0.20, 0.00, 0.00),
            BgE.EBONY_MINE_WORKER: (0.60, 0.30, 0.10, 0.00, 0.00, 0.00),
            BgE.DAEDRA_WORSHIPPER: (0.00, 0.30, 0.40, 0.20, 0.10, 0.00),
            BgE.VAMPIRE_HUNTER: (0.00, 0.00, 0.40, 0.40, 0.20, 0.00),
            BgE.BUOYANT_ARMIGER: (0.00, 0.00, 0.00, 0.40, 0.40, 0.20),
            BgE.SILT_STRIDER_OPERATOR: (0.30, 0.50, 0.20, 0.00, 0.00, 0.00),
            BgE.MOURNHOLD_ROYALTY: (0.00, 0.30, 0.40, 0.30, 0.00, 0.00),
            BgE.FISHERMAN: (0.40, 0.40, 0.20, 0.00, 0.00, 0.00),
            BgE.ALCHEMIST: (0.00, 0.00, 0.40, 0.40, 0.20, 0.00),
            BgE.SPELLWRIGHT: (0.00, 0.00, 0.30, 0.50, 0.20, 0.00),
            BgE.SMUGGLER: (0.00, 0.40, 0.40, 0.20, 0.00, 0.00),
            BgE.KHAJIIT_CARAVANEER: (0.00, 0.40, 0.40, 0.20, 0.00, 0.00),
            BgE.ARGONIAN_SLAVE: (0.70, 0.30, 0.00, 0.00, 0.00, 0.00),
        }
        
    def get_probability(self, background: BgE, experience_level: ExperienceLevelEnum) -> float:
        """
        This method returns the probability of a given experience level for a specific background.
        
        Parameters:
        background (BgE): The background of the character. This should be an instance of BackgroundTypeEnum.
        experience_level (ExperienceLevelEnum): The experience level of interest. This should be an instance of ExperienceLevelEnum.
        
        Returns:
        float: The probability of the given experience level for the specified background. This is a float value between 0 and 1.
        """
        if background not in self._config:
            raise ValueError(f"Background '{background}' not found in configuration.")
        if experience_level not in self._cols:
            raise ValueError(f"Experience level '{experience_level}' not found in configuration.")
        index = self._cols[experience_level]
        return self._config[background][index]

    def get_background_probabilities(self, background: BgE) -> dict[ExperienceLevelEnum, float]:
        """
        This method returns a dictionary with experience levels as keys and their probabilities as values for a given background.
        The method takes one parameter: the background of the character.
        The background parameter should be an instance of BackgroundTypeEnum.
        The method returns a dictionary where keys are experience levels and values are probabilities for the character with the given background.
        The returned dictionary has the structure: {ExperienceLevelEnum.BEGINNER: probability1, ExperienceLevelEnum.AMATEUR: probability2, ...}
        For example, for a 'mage' background, the returned dictionary might look like this:
        {ExperienceLevelEnum.BEGINNER: 0.00, ExperienceLevelEnum.AMATEUR: 0.30, ExperienceLevelEnum.ADEPT: 0.40, ExperienceLevelEnum.EXPERT: 0.30, ExperienceLevelEnum.MASTER: 0.00, ExperienceLevelEnum.LEGEND: 0.00}
        """
        if background not in self._config:
            raise ValueError(f"Background '{background}' not found in configuration.")
        probabilities = self._config[background]
        return {experience_level: prob for experience_level, prob in zip(self._cols.keys(), probabilities) if prob > 0}
