import templates.profiles.profiles as prof


tel_fyr_pop_config = [
    {"profile": prof.telvanni_mage, "probability": 0.40},  # Divayth Fyr and any similar mages

    # Servants and assistants working in Tel Fyr
    {"profile": prof.telvanni_servant, "probability": 0.40},  

    # Inhabitants of the Corprusarium
    {"profile": prof.corprusarium_inhabitant, "probability": 0.20},

    # Ensure the total probability adds up to 1 (or 100%).
]