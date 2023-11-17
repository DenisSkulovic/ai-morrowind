import templates.profiles.profiles as prof


ald_ruhn_pop_config = [
    {"profile": prof.commoner_redoran, "probability": 0.35},  # Majority as Redoran Dunmer
    {"profile": prof.redoran_warrior, "probability": 0.20},   # Significant warrior presence
    {"profile": prof.guard_redoran, "probability": 0.10},     # Redoran guards
    {"profile": prof.merchant_redoran, "probability": 0.05},  # Local merchants

    # Other Dunmer populations, including non-Redoran
    {"profile": prof.commoner_hlaalu, "probability": 0.05},
    {"profile": prof.commoner_telvanni, "probability": 0.05},

    # Non-Dunmer populations reflecting trade and travel
    {"profile": prof.commoner_imperial, "probability": 0.05},
    {"profile": prof.commoner_argonian, "probability": 0.03},
    {"profile": prof.commoner_khajiit, "probability": 0.03},
    {"profile": prof.commoner_nord, "probability": 0.03},
    {"profile": prof.commoner_breton, "probability": 0.02},
    {"profile": prof.commoner_orc, "probability": 0.01},
    {"profile": prof.commoner_wood_elf, "probability": 0.01},
    {"profile": prof.commoner_high_elf, "probability": 0.01},

    # Specific roles and professions
    {"profile": prof.farmer_redoran, "probability": 0.03},  # Local farmers
    {"profile": prof.smuggler_dark_elf, "probability": 0.01},  # Some illegal activities
    {"profile": prof.kwama_egg_miner, "probability": 0.02},  # Local miners
    # More profiles as needed...

    # Ensure the total probability adds up to 1 (or 100%).
]