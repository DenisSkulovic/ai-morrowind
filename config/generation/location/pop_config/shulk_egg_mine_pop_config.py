import templates.profiles.profiles as prof


shulk_egg_mine_pop_config = [
    {"profile": prof.kwama_egg_miner, "probability": 0.70},  # Majority as kwama egg miners

    # Miners from various races, reflecting some diversity in the workforce
    {"profile": prof.commoner_hlaalu, "probability": 0.10},  # Local Hlaalu Dunmer miners
    {"profile": prof.commoner_redoran, "probability": 0.05},
    {"profile": prof.commoner_imperial, "probability": 0.05},
    {"profile": prof.commoner_nord, "probability": 0.03},
    {"profile": prof.commoner_breton, "probability": 0.02},
    {"profile": prof.commoner_argonian, "probability": 0.02},
    {"profile": prof.commoner_khajiit, "probability": 0.01},
    {"profile": prof.commoner_orc, "probability": 0.01},
    {"profile": prof.commoner_wood_elf, "probability": 0.01},

    # Specific roles associated with a mining operation
    {"profile": prof.merchant_hlaalu, "probability": 0.01},  # Merchant selling mining supplies

    # Ensure the total probability adds up to 1 (or 100%).
]