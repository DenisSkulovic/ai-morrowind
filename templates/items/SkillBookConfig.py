from enum.items.SkillBookEnum import SkillBookEnum as SBkE
from classes.items.book.SkillBook import SkillBook


class SkillBookConfig:
    """
    This class represents the mapping of skill book items to their details.
    Each skill book is represented by a tuple of five values: item, base_price, base_weight, skill_improvement, improved_skill.
    If a value is not applicable, it is represented by None.
    """
    def __init__(self):
        self._cols = {"item": 0, "base_price": 1, "base_weight": 2, "skill_improvement": 3, "improved_skill": 4}
        from enum.SkillEnum import SkillEnum as SE
        self._config = {
            SBkE.DANCE_IN_FIRE_VOL1.value: (SkillBook, 60, 1.0, 5, SE.ACROBATICS.value),
            SBkE.ARMORERS_CHALLENGE.value: (SkillBook, 50, 1.0, 5, SE.ARMORER.value),
            SBkE.BLACK_ARROW_VOL2.value: (SkillBook, 70, 1.0, 5, SE.MARKSMAN.value),
            SBkE.LOCKED_ROOM.value: (SkillBook, 45, 1.0, 5, SE.SECURITY.value),
            SBkE.MYSTERY_OF_TALARA_VOL3.value: (SkillBook, 55, 1.0, 5, SE.ILLUSION.value),
            SBkE.REALITY_AND_OTHER_FALSEHOODS.value: (SkillBook, 65, 1.0, 5, SE.ALTERATION.value),
            SBkE.REFUGEES.value: (SkillBook, 40, 1.0, 5, SE.ATHLETICS.value),
            SBkE.RAINS_HAND_VOL4.value: (SkillBook, 75, 1.0, 5, SE.RESTORATION.value),
            SBkE.THE_WOLF_QUEEN_VOL1.value: (SkillBook, 80, 1.0, 5, SE.SPEECHCRAFT.value),
            SBkE.IMMORTAL_BLOOD.value: (SkillBook, 50, 1.0, 5, SE.HAND_TO_HAND.value),
            SBkE.MYSTICISM_FOR_DUMMIES.value: (SkillBook, 50, 1.0, 5, SE.MYSTICISM.value),
        }

    def get(self, item_name: str) -> dict:
        """
        This method returns the details of a given skill book.
        The method takes one parameter: the name of the skill book.
        The item_name parameter should be a string representing the name of the skill book.
        The method returns a dictionary with keys: item, base_price, base_weight, skill_improvement, improved_skill.
        If a value is not applicable, it is represented by None.

        Example of returned object:
        {
            'item': <class 'classes.items.book.SkillBook'>,
            'base_price': 60,
            'base_weight': 1.0,
            'skill_improvement': 5,
            'improved_skill': 'Acrobatics'
        }
        """
        if item_name not in self._config:
            raise ValueError(f"Skill book name '{item_name}' not found in configuration.")
        return {key: value for key, value in zip(self._cols.keys(), self._config[item_name])}
