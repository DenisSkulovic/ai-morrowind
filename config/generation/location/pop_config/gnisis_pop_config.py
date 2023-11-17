import templates.profiles.profiles as prof


gnisis_pop_config = [
    {"profile": prof.commoner_redoran, "probability": 0.30},  # Dominant local Dunmer population
    {"profile": prof.imperial_legionnaire, "probability": 0.20},  # Significant Imperial Legion presence

    # Miners working in the egg mine
    {"profile": prof.kwama_egg_miner, "probability": 0.25},

    # Temple personnel and religious figures
    {"profile": prof.priest_ashlander, "probability": 0.05},
    {"profile": prof.vivec_city_monk, "probability": 0.05},

    # Other races and professions, in smaller numbers
    {"profile": prof.commoner_imperial, "probability": 0.05},
    {"profile": prof.commoner_nord, "probability": 0.03},
    {"profile": prof.commoner_breton, "probability": 0.02},
    {"profile": prof.commoner_argonian, "probability": 0.02},
    {"profile": prof.commoner_khajiit, "probability": 0.01},
    {"profile": prof.commoner_orc, "probability": 0.01},
    {"profile": prof.commoner_wood_elf, "probability": 0.01},

    # Specific roles for a town like Gnisis
    {"profile": prof.merchant_redoran, "probability": 0.01},  # Local merchants

    # Ensure the total probability adds up to 1 (or 100%).
]