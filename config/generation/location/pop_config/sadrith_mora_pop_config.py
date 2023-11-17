import templates.profiles.profiles as prof


sadrith_mora_pop_config = [
    {"profile": prof.commoner_telvanni, "probability": 0.35},  # Dominant Telvanni population
    {"profile": prof.telvanni_mage, "probability": 0.20},     # High concentration of mages
    {"profile": prof.sadrith_mora_scholar, "probability": 0.10}, # Scholars and researchers

    # Other Dunmer populations, including non-Telvanni
    {"profile": prof.commoner_redoran, "probability": 0.05},
    {"profile": prof.commoner_hlaalu, "probability": 0.05},

    # Non-Dunmer, mainly those who serve or trade with the Telvanni
    {"profile": prof.commoner_imperial, "probability": 0.05},
    {"profile": prof.commoner_argonian, "probability": 0.03},
    {"profile": prof.commoner_khajiit, "probability": 0.03},
    {"profile": prof.commoner_nord, "probability": 0.02},
    {"profile": prof.commoner_breton, "probability": 0.02},
    {"profile": prof.commoner_orc, "probability": 0.01},
    {"profile": prof.commoner_wood_elf, "probability": 0.01},
    {"profile": prof.commoner_high_elf, "probability": 0.01},

    # Specific roles relevant to Sadrith Mora
    {"profile": prof.dwemer_researcher, "probability": 0.02},  # Given the Telvanni's interest in ancient knowledge
    {"profile": prof.alchemist, "probability": 0.03},          # Alchemists and potion makers
    {"profile": prof.spellwright, "probability": 0.03},        # Creators of magical items and enchantments
    # More profiles as needed...

    # Ensure the total probability adds up to 1 (or 100%).
]