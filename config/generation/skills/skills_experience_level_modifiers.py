from enum.ExperienceLevelEnum import ExperienceLevelEnum


skills_experience_level_modifiers = {
    ExperienceLevelEnum.BEGINNER: 0,  # No additional bonus to skills for beginners
    ExperienceLevelEnum.AMATEUR: 5,  # Small bonus for amateurs
    ExperienceLevelEnum.ADEPT: 10,  # Moderate bonus for adepts
    ExperienceLevelEnum.EXPERT: 15,  # Significant bonus for experts
    ExperienceLevelEnum.MASTER: 20,  # High bonus for masters
    ExperienceLevelEnum.LEGEND: 25,  # Maximum bonus for legends
}