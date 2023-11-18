from enum.ExperienceLevelEnum import ExperienceLevelEnum as ExE


experience_level_ranges = {
    ExE.BEGINNER: (0, 0.25),
    ExE.AMATEUR: (0.25, 0.5),
    ExE.ADEPT: (0.5, 0.75),
    ExE.EXPERT: (0.75, 0.9),
    ExE.MASTER: (0.9, 0.95),
    ExE.LEGEND: (0.95, 1),
}