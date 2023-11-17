class StoryTeller:
    current_step = 1
    current_game_stage = game_stage_enum.introdunction
    current_mode = mode_enum.story
    
    # this needs to have an object for the current scene, like a description of the location, collection of involved characters and enemies
    # this needs functionality to take two characters and enter in combat, conversation, etc. This should be the main tool to use for storytelling.
    # Each step or any action should trigger a review of the scene or replace it completely.
    # Maybe add layers, like immediate surrounding, at a distance, on the horizon, and some characters and items on each layer. For example, conversation or close combat is nly possible on close layer, arrows and spells can reach at a distance.
    
    def commence_with_the_story():
        current_mode = mode_enum.story
    def take_next_step():
        current_step = current_step + 1
    def enter_purchasing():
        current_mode = mode_enum.purchasing
    def enter_selling():
        current_mode = mode_enum.selling
    def enter_combat():
        current_mode = mode_enum.combat
    def next_game_stage():
        # TODO replace the stage with the next one in sequence
        pass
        
    def engage_in_conversation(player, npc):
        # this should generate dialogue based on character knowledge, opinion, traits
        # this should return a set of topics that this NPC can be spoken to about, and some opinion, mood modifiers, to generate good dialogue based on it.
        # conversation can lead to 
        pass

    def simulate_trade(player, trader, item, base_price, is_buying):
        # TODO add the impact of opinion between trader and player
        
        # Player and Trader Skills
        player_mercantile = player['skills'].get('Mercantile', 0)
        player_charisma = player['attributes'].get('Charisma', 0)
        trader_mercantile = trader['skills'].get('Mercantile', 0)
        trader_disposition = trader['disposition']

        # Base Price Adjustment
        if is_buying:
            price_modifier = (trader_mercantile + trader_disposition) / (player_mercantile + player_charisma)
        else:  # Selling
            price_modifier = (player_mercantile + player_charisma) / (trader_mercantile + trader_disposition)

        # Initial Price Calculation
        initial_price = round(base_price * price_modifier)

        # Additional Factors
        item_rarity = item.get('rarity', 1)  # Default rarity value is 1
        market_demand = item.get('demand', 1)  # Default market demand value is 1
        special_circumstances = item.get('special_circumstances', 1)  # Default special circumstances modifier is 1

        # Adjusting Price based on Additional Factors
        adjusted_price = initial_price * item_rarity * market_demand * special_circumstances

        # Final Price Calculation
        final_price = round(adjusted_price)

        return final_price

    def simulate_combat(player, enemy):
        # Random Factor - Dice Roll
        dice_roll = random.randint(1, 20)

        # Player's Attack and Defense Calculation
        player_attack_skill = player['skills'].get('weapon_skill', 0)  # e.g., 'Short Sword', 'Marksman'
        player_weapon_value = player['inventory']['Weapon'].get('attack_value', 0)
        player_attack = dice_roll + (player_attack_skill * 0.1) + player_weapon_value

        player_defense_skill = player['skills'].get('armor_skill', 0)  # e.g., 'Heavy Armor', 'Light Armor'
        player_armor_value = player['inventory']['Armor'].get('defense_value', 0)
        player_defense = (player_defense_skill * 0.1) + player_armor_value

        # Enemy's Attack and Defense Calculation
        enemy_attack_skill = enemy['skills'].get('weapon_skill', 0)
        enemy_weapon_value = enemy['inventory']['Weapon'].get('attack_value', 0)
        enemy_attack = (enemy_attack_skill * 0.1) + enemy_weapon_value

        enemy_defense_skill = enemy['skills'].get('armor_skill', 0)
        enemy_armor_value = enemy['inventory']['Armor'].get('defense_value', 0)
        enemy_defense = (enemy_defense_skill * 0.1) + enemy_armor_value

        # Special Abilities or Spells
        # Add any effects from spells or abilities that may modify attack/defense

        # Net Damage Calculation
        player_damage = max(0, player_attack - enemy_defense)
        enemy_damage = max(0, enemy_attack - player_defense)

        return player_damage, enemy_damage
