from enum import Enum

class EffectEnum(Enum):
    FIRE_DAMAGE = "Fire Damage"
    FROST_DAMAGE = "Frost Damage"
    SHOCK_DAMAGE = "Shock Damage"
    POISON_DAMAGE = "Poison Damage"
    MAGICKA_DAMAGE = "Magicka Damage"
    FATIGUE_DAMAGE = "Fatigue Damage"
    HEALTH_DAMAGE = "Health Damage"
    ABSORB_HEALTH = "Absorb Health"
    ABSORB_MAGICKA = "Absorb Magicka"
    ABSORB_FATIGUE = "Absorb Fatigue"
    RESTORE_HEALTH = "Restore Health"
    RESTORE_MAGICKA = "Restore Magicka"
    RESTORE_FATIGUE = "Restore Fatigue"
    REGENERATE_HEALTH = "Regenerate Health"
    REGENERATE_MAGICKA = "Regenerate Magicka"
    REGENERATE_FATIGUE = "Regenerate Fatigue"
    FORTIFY_ATTRIBUTE = "Fortify Attribute"
    FORTIFY_SKILL = "Fortify Skill"
    RESIST_FIRE = "Resist Fire"
    RESIST_FROST = "Resist Frost"
    RESIST_SHOCK = "Resist Shock"
    RESIST_MAGICKA = "Resist Magicka"
    RESIST_POISON = "Resist Poison"
    RESIST_COMMON_DISEASE = "Resist Common Disease"
    RESIST_BLIGHT_DISEASE = "Resist Blight Disease"
    RESIST_PARALYSIS = "Resist Paralysis"
    RESIST_CORPRUS = "Resist Corprus"
    CURE_COMMON_DISEASE = "Cure Common Disease"
    CURE_BLIGHT_DISEASE = "Cure Blight Disease"
    CURE_POISON = "Cure Poison"
    LEVITATE = "Levitate"
    WATER_WALKING = "Water Walking"
    WATER_BREATHING = "Water Breathing"
    INVISIBILITY = "Invisibility"
    CHAMELEON = "Chameleon"
    REFLECT = "Reflect"
    TELEKINESIS = "Telekinesis"
    NIGHT_EYE = "Night Eye"
    PARALYSIS = "Paralysis"
    SILENCE = "Silence"
    BLIND = "Blind"
    SOUND = "Sound"
    CALM_CREATURE = "Calm Creature"
    CALM_HUMANOID = "Calm Humanoid"
    FRENZY_CREATURE = "Frenzy Creature"
    FRENZY_HUMANOID = "Frenzy Humanoid"
    DEMORALIZE_CREATURE = "Demoralize Creature"
    DEMORALIZE_HUMANOID = "Demoralize Humanoid"
    RALLY_CREATURE = "Rally Creature"
    RALLY_HUMANOID = "Rally Humanoid"
    CHARM = "Charm"
    SUMMON_CREATURE = "Summon Creature"
    TURN_UNDEAD = "Turn Undead"
    BOUND_ITEM = "Bound Item"
    LIGHT = "Light"
    LOCK = "Lock"
    OPEN = "Open"
    DISPEL = "Dispel"
    ALMSIVI_INTERVENTION = "Almsivi Intervention"
    DIVINE_INTERVENTION = "Divine Intervention"
    MARK = "Mark"
    RECALL = "Recall"
    SLOWFALL = "Slowfall"
    SHIELD = "Shield"
    SPIRIT_KNIFE = "Spirit Knife"
    DETECT_KEY = "Detect Key"
    DETECT_ENCHANTMENT = "Detect Enchantment"
    DETECT_ANIMAL = "Detect Animal"
    DETECT_DEAD = "Detect Dead"
    DETECT_HUMANOID = "Detect Humanoid"
    DETECT_CREATURE = "Detect Creature"
    DETECT_DAEDRA = "Detect Daedra"
    DETECT_UNDEAD = "Detect Undead"
    DETECT_DOOR = "Detect Door"
    DETECT_TRAP = "Detect Trap"
    TELEPORTATION = "Teleportation"
    SOULTRAP = "Soultrap"
    FORTIFY_MAXIMUM_MAGICKA = "Fortify Maximum Magicka"
    FORTIFY_ATTACK = "Fortify Attack"
    FORTIFY_ARMOR_RATING = "Fortify Armor Rating"
    FORTIFY_BARTER = "Fortify Barter"
    FORTIFY_BLOCK = "Fortify Block"
    FORTIFY_CASTING = "Fortify Casting"
    FORTIFY_DESTRUCTION = "Fortify Destruction"
    FORTIFY_ENCHANT = "Fortify Enchant"
    FORTIFY_FATIGUE = "Fortify Fatigue"
    FORTIFY_HEALTH = "Fortify Health"
    FORTIFY_HEAVY_ARMOR = "Fortify Heavy Armor"
    FORTIFY_ILLUSION = "Fortify Illusion"
    FORTIFY_LIGHT_ARMOR = "Fortify Light Armor"
    FORTIFY_LOCKPICKING = "Fortify Lockpicking"
    FORTIFY_LONG_BLADE = "Fortify Long Blade"
    FORTIFY_MAGICKA = "Fortify Magicka"
    FORTIFY_MARKSMAN = "Fortify Marksman"
    FORTIFY_MYSTICISM = "Fortify Mysticism"
    FORTIFY_ONE_HANDED = "Fortify One Handed"
    FORTIFY_PICKPOCKET = "Fortify Pickpocket"
    FORTIFY_RESTORATION = "Fortify Restoration"
    FORTIFY_SHORT_BLADE = "Fortify Short Blade"
    FORTIFY_SNEAK = "Fortify Sneak"
    FORTIFY_SPEECHCRAFT = "Fortify Speechcraft"
    FORTIFY_TWO_HANDED = "Fortify Two Handed"
    FORTIFY_UNARMED = "Fortify Unarmed"
    FORTIFY_ALCHEMY = "Fortify Alchemy"
    FORTIFY_ALTERATION = "Fortify Alteration"
    FORTIFY_ATHLETICS = "Fortify Athletics"
    FORTIFY_AXE = "Fortify Axe"
    FORTIFY_BLUNT_WEAPON = "Fortify Blunt Weapon"
    FORTIFY_CONJURATION = "Fortify Conjuration"
    FORTIFY_CROSSBOW = "Fortify Crossbow"
    FORTIFY_HAND_TO_HAND = "Fortify Hand to Hand"
    FORTIFY_MEDIUM_ARMOR = "Fortify Medium Armor"
    FORTIFY_MERCANTILE = "Fortify Mercantile"
    FORTIFY_PERSUASION = "Fortify Persuasion"
    FORTIFY_SPEAR = "Fortify Spear"
    FORTIFY_UNARMORED = "Fortify Unarmored"
    FORTIFY_ACROBATICS = "Fortify Acrobatics"
    FORTIFY_ARMORER = "Fortify Armorer"
    FORTIFY_BOW = "Fortify Bow"
    FORTIFY_DAGGER = "Fortify Dagger"
    FORTIFY_MACE = "Fortify Mace"
    FORTIFY_SWORD = "Fortify Sword"
    FORTIFY_WARHAMMER = "Fortify Warhammer"
    FORTIFY_WILLPOWER = "Fortify Willpower"
    FORTIFY_AGILITY = "Fortify Agility"
    FORTIFY_ENDURANCE = "Fortify Endurance"
    FORTIFY_INTELLIGENCE = "Fortify Intelligence"
    FORTIFY_LUCK = "Fortify Luck"
    FORTIFY_PERSONALITY = "Fortify Personality"
    FORTIFY_SPEED = "Fortify Speed"
    FORTIFY_STRENGTH = "Fortify Strength"
    FORTIFY_BLADE = "Fortify Blade"
    FORTIFY_BLUNT = "Fortify Blunt"