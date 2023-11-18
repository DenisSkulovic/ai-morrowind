from classes.creatures.character.CharacterProfile import CharacterProfile as CP
from enum.culture_enum import CultureEnum as C
from enum.race_enum import RaceEnum as Ra
from enum.religion_enum import ReligionEnum as Re
from enum.faction_enum import FactionEnum as F
from enum.background_type_enum import BackgroundTypeEnum as B


# common citizens of the empire, mostly cosmopolitan and worship nine divines, but dark elves are more rooted with vvardenfell - carry the local culture and worship the tribunal
commoner_hlaalu = CP(B.COMMONER, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.INDEP)
commoner_redoran = CP(B.COMMONER, Ra.DARK_ELF, C.REDORAN, Re.TRIBUNAL_T, F.INDEP)
commoner_telvanni = CP(B.COMMONER, Ra.DARK_ELF, C.TELVANNI, Re.TRIBUNAL_T, F.INDEP)
commoner_imperial = CP(B.COMMONER, Ra.IMPERIAL, C.COSMOP, Re.NINE_D, F.INDEP)
commoner_argonian = CP(B.COMMONER, Ra.ARGONIAN, C.COSMOP, Re.NINE_D, F.INDEP)
commoner_khajiit = CP(B.COMMONER, Ra.KHAJIIT, C.COSMOP, Re.NINE_D, F.INDEP)
commoner_nord = CP(B.COMMONER, Ra.NORD, C.COSMOP, Re.NINE_D, F.INDEP)
commoner_breton = CP(B.COMMONER, Ra.BRETON, C.COSMOP, Re.NINE_D, F.INDEP)
commoner_orc = CP(B.COMMONER, Ra.ORC, C.COSMOP, Re.NINE_D, F.INDEP)
commoner_redguard = CP(B.COMMONER, Ra.REDGUARD, C.COSMOP, Re.NINE_D, F.INDEP)
commoner_wood_elf = CP(B.COMMONER, Ra.WOOD_ELF, C.COSMOP, Re.NINE_D, F.INDEP)
commoner_high_elf = CP(B.COMMONER,Ra.HIGH_ELF, C.COSMOP, Re.NINE_D, F.INDEP)

# guards representing various ruling powers
guard_hlaalu = CP(B.GUARD, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.HLAALU)
guard_redoran = CP(B.GUARD, Ra.DARK_ELF, C.REDORAN, Re.TRIBUNAL_T, F.REDORAN)
guard_telvanni = CP(B.GUARD, Ra.DARK_ELF, C.TELVANNI, Re.TRIBUNAL_T, F.TELVANNI)
guard_imperial = CP(B.GUARD, Ra.IMPERIAL, C.IMPERIAL_CYR, Re.NINE_D, F.IMPERIAL_LEG)

# mages of the mages guild
mage_breton = CP(B.MAGE, Ra.BRETON, C.BRETON, Re.NINE_D, F.MAGES_G)
mage_high_elf = CP(B.MAGE,Ra.HIGH_ELF, C.ALDMERI, Re.NINE_D, F.MAGES_G)

#necromancers
necromancer_breton = CP(B.NECROMANCER, Ra.BRETON, C.COSMOP, Re.MOLAG_BAL, F.INDEP)
necromancer_high_elf = CP(B.NECROMANCER,Ra.HIGH_ELF, C.COSMOP, Re.MOLAG_BAL, F.INDEP)

# telvanni mages
telvanni_mage = CP(B.TELVANNI_MAGE, Ra.DARK_ELF, C.TELVANNI, Re.TRIBUNAL_T, F.TELVANNI)

# servants of telvanni mages
telvanni_servant = CP(B.TELVANNI_SERVANT, Ra.DARK_ELF, C.TELVANNI, Re.TRIBUNAL_T, F.TELVANNI)

# nobles
noble_imperial = CP(B.NOBLE, Ra.IMPERIAL, C.IMPERIAL_CYR, Re.NINE_D, F.IMPERIAL_LEG)
noble_redoran = CP(B.NOBLE, Ra.DARK_ELF, C.REDORAN, Re.TRIBUNAL_T, F.REDORAN)
noble_hlaalu = CP(B.NOBLE, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.HLAALU)
noble_high_elf = CP(B.NOBLE,Ra.HIGH_ELF, C.ALDMERI, Re.ALDMERI_P, F.IMPERIAL_LEG)

# adventurers of various backgrounds
adventurer_imperial = CP(B.ADVENTURER, Ra.IMPERIAL, C.COSMOP, Re.NINE_D, F.INDEP)
adventurer_high_elf = CP(B.ADVENTURER,Ra.HIGH_ELF, C.COSMOP, Re.NINE_D, F.INDEP)
adventurer_breton = CP(B.ADVENTURER, Ra.BRETON, C.COSMOP, Re.NINE_D, F.INDEP)
adventurer_orc = CP(B.ADVENTURER, Ra.ORC, C.COSMOP, Re.NINE_D, F.INDEP)
adventurer_wood_elf = CP(B.ADVENTURER, Ra.WOOD_ELF, C.COSMOP, Re.NINE_D, F.INDEP)
adventurer_nord = CP(B.ADVENTURER, Ra.NORD, C.COSMOP, Re.NINE_D, F.INDEP)

# outlaws and bandits
outlaw_dark_elf_hlaalu = CP(B.OUTLAW, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.INDEP)
outlaw_dark_elf_redoran = CP(B.OUTLAW, Ra.DARK_ELF, C.REDORAN, Re.TRIBUNAL_T, F.INDEP)
outlaw_nord = CP(B.OUTLAW, Ra.NORD, C.COSMOP, Re.NINE_D, F.INDEP)
outlaw_argonian = CP(B.OUTLAW, Ra.ARGONIAN, C.COSMOP, Re.NINE_D, F.INDEP)

# a hermit is someone living outside of cities - hiding away, daedra worshipers, loners, scholars and researchers
hermit_dark_elf_hlaalu = CP(B.HERMIT, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.INDEP)
hermit_dark_elf_redoran = CP(B.HERMIT, Ra.DARK_ELF, C.REDORAN, Re.TRIBUNAL_T, F.INDEP)

# ashlander tribesmen
ashlander = CP(B.ASHLANDER, Ra.DARK_ELF, C.ASHLANDER, Re.ASHLANDER, F.ASHLANDERS)

sadrith_mora_scholar = CP(B.SADRITH_MORA_SCHOLAR, Ra.DARK_ELF, C.TELVANNI, Re.TRIBUNAL_T, F.TELVANNI)

redoran_warrior = CP(B.REDORAN_WARRIOR, Ra.DARK_ELF, C.REDORAN, Re.TRIBUNAL_T, F.REDORAN)

hlaalu_trader = CP(B.HLAALU_TRADER, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.HLAALU)

balmora_citizen = CP(B.BALMORA_CITIZEN, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.INDEP)

vivec_city_monk = CP(B.VIVEC_CITY_MONK, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.TRIBUNAL_T)

imperial_legionnaire = CP(B.IMPERIAL_LEGIONNAIRE, Ra.IMPERIAL, C.IMPERIAL_CYR, Re.NINE_D, F.IMPERIAL_LEG)
imperial_officer = CP(B.IMPERIAL_OFFICER, Ra.IMPERIAL, C.IMPERIAL_CYR, Re.NINE_D, F.IMPERIAL_LEG)

dwemer_researcher = CP(B.DWEMER_RESEARCHER, Ra.HIGH_ELF, C.ALDMERI, Re.NINE_D, F.MAGES_G)

morrowind_pilgrim_hlaalu = CP(B.PILGRIM, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.TRIBUNAL_T)
morrowind_pilgrim_redoran = CP(B.PILGRIM, Ra.DARK_ELF, C.REDORAN, Re.TRIBUNAL_T, F.TRIBUNAL_T)

ebony_mine_worker_hlaalu = CP(B.MINER, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.INDEP)
ebony_mine_worker_redoran = CP(B.MINER, Ra.DARK_ELF, C.REDORAN, Re.TRIBUNAL_T, F.INDEP)

# worshipers of various daedra princes
daedra_worshiper_vaermina = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.VAERMINA, F.INDEP)
daedra_worshiper_sheogorath = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.SHEOGORATH, F.INDEP)
daedra_worshiper_sanguine = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.SANGUINE, F.INDEP)
daedra_worshiper_peryite = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.PERYITE, F.INDEP)
daedra_worshiper_nocturnal = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.NOCTURNAL, F.INDEP)
daedra_worshiper_namira = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.NAMIRA, F.INDEP)
daedra_worshiper_molag_bal = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.MOLAG_BAL, F.INDEP)
daedra_worshiper_meridia = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.MERIDIA, F.INDEP)
daedra_worshiper_mehrunes_dagon = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.MEHRUNES_DAGON, F.INDEP)
daedra_worshiper_malacath = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.MALACATH, F.INDEP)
daedra_worshiper_hircine = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.HIRCINE, F.INDEP)
daedra_worshiper_hermeus_mora = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.HERMAEUS_MORA, F.INDEP)
daedra_worshiper_clavicus_vile = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.CLAVICUS_VILE, F.INDEP)
daedra_worshiper_boethiah = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.BOETHIAH, F.INDEP)
daedra_worshiper_azura = CP(B.DAEDRA_WORSHIPER, Ra.DARK_ELF, C.COSMOP, Re.AZURA, F.INDEP)

vampire_hunter = CP(B.VAMPIRE_HUNTER, Ra.NORD, C.NORD, Re.NINE_D, F.FIGHTERS_G)

buoyant_armiger = CP(B.BUOYANT_ARMIGER, Ra.DARK_ELF, C.BOUYANT_ARMIGER, Re.TRIBUNAL_T, F.TRIBUNAL_T)

silt_strider_operator = CP(B.SILT_STRIDER_OPERATOR, Ra.DARK_ELF, C.COSMOP, Re.DARK_ELF, F.INDEP)

mournhold_royalty = CP(B.MOURNHOLD_ROYALTY, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.HLAALU)

fisherman_dark_elf = CP(B.FISHERMAN, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.INDEP)

alchemist = CP(B.ALCHEMIST, Ra.HIGH_ELF, C.COSMOP, Re.NINE_D, F.MAGES_G)

spellwright = CP(B.SPELLWRIGHT, Ra.HIGH_ELF, C.ALDMERI, Re.NINE_D, F.MAGES_G)

smuggler_dark_elf = CP(B.SMUGGLER, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.INDEP)
smuggler_argonian = CP(B.SMUGGLER, Ra.DARK_ELF, C.COSMOP, Re.NINE_D, F.INDEP)

khajiit_caravaneer = CP(B.CARAVANEER, Ra.KHAJIIT, C.COSMOP, Re.NINE_D, F.INDEP)

slave_argonian = CP(B.ARGONIAN_SLAVE, Ra.ARGONIAN, C.ARGONIAN_TRIBAL, Re.HIST, F.INDEP)

merchant_imperial = CP(B.MERCHANT, Ra.IMPERIAL, C.COSMOP, Re.NINE_D, F.INDEP)
merchant_hlaalu = CP(B.MERCHANT, Ra.DARK_ELF, C.HLAALU, Re.NINE_D, F.INDEP)
merchant_redoran = CP(B.MERCHANT, Ra.DARK_ELF, C.REDORAN, Re.NINE_D, F.INDEP)
merchant_wood_elf = CP(B.MERCHANT, Ra.WOOD_ELF, C.COSMOP, Re.NINE_D, F.INDEP)
merchant_redguard = CP(B.MERCHANT, Ra.REDGUARD, C.COSMOP, Re.NINE_D, F.INDEP)
merchant_khajiit = CP(B.MERCHANT, Ra.KHAJIIT, C.COSMOP, Re.NINE_D, F.INDEP)

priest_ashlander = CP(B.PRIEST, Ra.DARK_ELF, C.ASHLANDER, Re.ASHLANDER, F.ASHLANDERS)
priest_imperial_cyrodiil = CP(B.PRIEST, Ra.IMPERIAL, C.IMPERIAL_CYR, Re.NINE_D, F.IMPERIAL_CULT)
priest_imperial_breton = CP(B.PRIEST, Ra.BRETON, C.BRETON, Re.NINE_D, F.IMPERIAL_CULT)

kwama_egg_miner = CP(B.MINER, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.INDEP)

farmer_redoran = CP(B.FARMER, Ra.DARK_ELF, C.REDORAN, Re.TRIBUNAL_T, F.INDEP)
farmer_hlaalu = CP(B.FARMER, Ra.DARK_ELF, C.HLAALU, Re.TRIBUNAL_T, F.INDEP)
farmer_imperial = CP(B.FARMER, Ra.IMPERIAL, C.IMPERIAL_COL, Re.NINE_D, F.INDEP)