import templates.profiles.profiles as prof


khuul_pop_config = [
    {"profile": prof.commoner_hlaalu, "probability": 0.30},  # Majority as local Hlaalu Dunmer
    {"profile": prof.fisherman_dark_elf, "probability": 0.25},  # Significant number of fishermen

    # Smugglers, reflecting the village's reputation
    {"profile": prof.smuggler_dark_elf, "probability": 0.20}, 
    {"profile": prof.smuggler_argonian, "probability": 0.05},

    # Other races present in smaller numbers
    {"profile": prof.commoner_nord, "probability": 0.05},
    {"profile": prof.commoner_redguard, "probability": 0.05},
    {"profile": prof.commoner_breton, "probability": 0.03},
    {"profile": prof.commoner_argonian, "probability": 0.02},
    {"profile": prof.commoner_orc, "probability": 0.01},
    {"profile": prof.commoner_khajiit, "probability": 0.01},
    {"profile": prof.commoner_wood_elf, "probability": 0.01},
    {"profile": prof.commoner_high_elf, "probability": 0.01},
    
    # More specific roles relevant to a fishing village
    {"profile": prof.silt_strider_operator, "probability": 0.01},  # For transport services

    # Ensure the total probability adds up to 1 (or 100%).
]