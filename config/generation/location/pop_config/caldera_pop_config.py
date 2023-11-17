import templates.profiles.profiles as prof


caldera_pop_config = [
    {"profile": prof.commoner_imperial, "probability": 0.30},  # Significant Imperial presence
    {"profile": prof.imperial_legionnaire, "probability": 0.15},  # Imperial soldiers and guards
    {"profile": prof.merchant_imperial, "probability": 0.10},  # Traders and merchants, mostly Imperial

    # Local Dunmer population, some working in mines or local businesses
    {"profile": prof.commoner_hlaalu, "probability": 0.15},
    {"profile": prof.ebony_mine_worker_hlaalu, "probability": 0.10},  # Workers in the ebony mine

    # Other races present due to the mining operation and trade
    {"profile": prof.commoner_nord, "probability": 0.05},
    {"profile": prof.commoner_redguard, "probability": 0.05},
    {"profile": prof.commoner_breton, "probability": 0.03},
    {"profile": prof.commoner_orc, "probability": 0.02},
    {"profile": prof.commoner_argonian, "probability": 0.02},
    {"profile": prof.commoner_khajiit, "probability": 0.01},
    {"profile": prof.commoner_wood_elf, "probability": 0.01},
    {"profile": prof.commoner_high_elf, "probability": 0.01},

    # Specific roles related to the town's characteristics
    {"profile": prof.smuggler_argonian, "probability": 0.02},  # Considering the illegal activities around mining
    # More profiles as needed...

    # Ensure the total probability adds up to 1 (or 100%).
]