import templates.profiles.profiles as prof


seyda_neen_pop_config = [
    {"profile": prof.commoner_imperial, "probability": 0.30},  # Higher Imperial presence
    {"profile": prof.commoner_hlaalu, "probability": 0.25},   # Local Dark Elf population
    {"profile": prof.commoner_redoran, "probability": 0.05},  # Some presence from other houses
    {"profile": prof.commoner_telvanni, "probability": 0.05},
    {"profile": prof.commoner_argonian, "probability": 0.10},  # Due to being a port town
    {"profile": prof.commoner_khajiit, "probability": 0.10},
    {"profile": prof.commoner_nord, "probability": 0.05},
    {"profile": prof.commoner_breton, "probability": 0.03},
    {"profile": prof.commoner_orc, "probability": 0.02},
    {"profile": prof.commoner_wood_elf, "probability": 0.02},
    {"profile": prof.commoner_high_elf, "probability": 0.01},
    {"profile": prof.guard_imperial, "probability": 0.10},    # Imperial guards due to the Census and Excise Office
    {"profile": prof.merchant_imperial, "probability": 0.02},  # Some traders and merchants
    {"profile": prof.fisherman_dark_elf, "probability": 0.03},  # Representing local fishermen
    {"profile": prof.silt_strider_operator, "probability": 0.02},  # For transport services
]