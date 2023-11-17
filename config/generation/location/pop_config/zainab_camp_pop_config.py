import templates.profiles.profiles as prof


zainab_camp_pop_config = [
    {"profile": prof.ashlander, "probability": 0.60},  # Majority as general Ashlanders

    # Specific roles within the Ashlander community
    {"profile": prof.hunter_ashlander, "probability": 0.15},  # Hunters of the tribe
    {"profile": prof.wise_woman_ashlander, "probability": 0.10},  # Spiritual and healing leaders
    {"profile": prof.tribal_leader_ashlander, "probability": 0.05},  # The tribal chieftain

    # Ashlander warriors and scouts
    {"profile": prof.warrior_ashlander, "probability": 0.10},

    # Ensure the total probability adds up to 1 (or 100%).
]