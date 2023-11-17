import templates.profiles.profiles as prof


moonmoth_legion_fort_pop_config = [
    {"profile": prof.imperial_legionnaire, "probability": 0.50},  # Majority as Imperial soldiers

    # Higher ranking Imperial officers
    {"profile": prof.imperial_officer, "probability": 0.10},  

    # Non-military personnel providing essential services
    {"profile": prof.merchant_imperial, "probability": 0.10},  # Traders selling supplies to the garrison
    {"profile": prof.healer, "probability": 0.10},  # Healers and medics

    # Local civilians employed at the fort
    {"profile": prof.commoner_imperial, "probability": 0.10}, 
    {"profile": prof.commoner_hlaalu, "probability": 0.05},  # Local Dunmer working in various capacities

    # Specific roles related to a military fort
    {"profile": prof.spellwright, "probability": 0.05},  # Enchanters and magic users

    # Ensure the total probability adds up to 1 (or 100%).
]