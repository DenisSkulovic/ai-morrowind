import random
from classes.creatures.character.Character import Character
from classes.creatures.character.CharacterSkills import CharacterSkills
from config.generation.skills import skills_base_config, skills_experience_level_modifiers, skills_specialized_config, skills_race_bonus_config


class CharacterSkillGenerator:
    def __init__(self):
        pass
        
    def _generate_skills(self, character: Character) -> None:
        skills: CharacterSkills = CharacterSkills()

        # Generate base skills
        for skill, skill_range in skills_base_config.items():
            skills.set_skill(skill, random.randint(*skill_range))

        # Add specialized skills for the class
        for skill, bonus in skills_specialized_config.get(character.character_class, {}).items():
            skills.set_skill(skill, min(skills.get_skill(skill) + bonus, 100)) # Ensure skill doesn't exceed 100

        # Add race-based skills
        for skill, bonus in skills_race_bonus_config.get(character.race, {}).items():
            skills.set_skill(skill, min(skills.get_skill(skill) + bonus, 100)) # Ensure skill doesn't exceed 100

        # Apply experience level modifiers
        experience_bonus = skills_experience_level_modifiers.get(character.experience_level, 0)
        for skill in skills:
            skills.set_skill(skill, min(skills.get_skill(skill) + experience_bonus, 100)) # Ensure skill doesn't exceed 100

        character.skills = skills
