from enum.travel_difficulty_enum import travel_difficulty_enum
from enum.travel_danger_enum import travel_danger_enum

# TODO use travel time as base, but it can be modified by some skill or potion, or maybe even horse
# TODO base_danger should be modified for player's skill for silent moving, potion, trait. Maybe it's better to make it into 0-100
# TODO maybe instead of travel time use distance, so that time becomes flexible

vvardenfell_connections = {
    "Balmora <-> Seyda Neen": {
        "base_travel_time": "4 hours",
        "base_difficulty": travel_difficulty_enum.easy,
        "base_danger": travel_danger_enum.low_risk
    },
    "Balmora <-> Vivec City": {
        "base_travel_time": "6 hours",
        "base_difficulty": travel_difficulty_enum.moderate,
        "base_danger": travel_danger_enum.moderate_risk
    },
    "Balmora <-> Ald'ruhn": {
        "base_travel_time": "8 hours",
        "base_difficulty": travel_difficulty_enum.moderate,
        "base_danger": travel_danger_enum.moderate_risk
    },
    "Balmora <-> Caldera": {
        "base_travel_time": "3 hours",
        "base_difficulty": travel_difficulty_enum.easy,
        "base_danger": travel_danger_enum.low_risk
    },
    "Balmora <-> Pelagiad": {
        "base_travel_time": "5 hours",
        "base_difficulty": travel_difficulty_enum.easy,
        "base_danger": travel_danger_enum.low_risk
    },
    "Seyda Neen <-> Vivec City": {
        "base_travel_time": "2 hours",
        "base_difficulty": travel_difficulty_enum.easy,
        "base_danger": travel_danger_enum.safe
    },
    "Seyda Neen <-> Ebonheart": {
        "base_travel_time": "3 hours",
        "base_difficulty": travel_difficulty_enum.moderate,
        "base_danger": travel_danger_enum.low_risk
    },
    "Vivec City <-> Ebonheart": {
        "base_travel_time": "1 hour",
        "base_difficulty": travel_difficulty_enum.easy,
        "base_danger": travel_danger_enum.safe
    },
    "Vivec City <-> Molag Mar": {
        "base_travel_time": "10 hours",
        "base_difficulty": travel_difficulty_enum.hard,
        "base_danger": travel_danger_enum.high_risk
    },
    "Ald'ruhn <-> Caldera": {
        "base_travel_time": "7 hours",
        "base_difficulty": travel_difficulty_enum.moderate,
        "base_danger": travel_danger_enum.moderate_risk
    },
    "Ald'ruhn <-> Gnisis": {
        "base_travel_time": "6 hours",
        "base_difficulty": travel_difficulty_enum.hard,
        "base_danger": travel_danger_enum.high_risk
    },
    "Caldera <-> Pelagiad": {
        "base_travel_time": "4 hours",
        "base_difficulty": travel_difficulty_enum.easy,
        "base_danger": travel_danger_enum.low_risk
    },
    "Pelagiad <-> Ebonheart": {
        "base_travel_time": "6 hours",
        "base_difficulty": travel_difficulty_enum.moderate,
        "base_danger": travel_danger_enum.moderate_risk
    },
    "Sadrith Mora <-> Tel Fyr": {
        "base_travel_time": "3 hours",
        "base_difficulty": travel_difficulty_enum.hard,
        "base_danger": travel_danger_enum.high_risk
    },
    "Sadrith Mora <-> Molag Mar": {
        "base_travel_time": "5 hours",
        "base_difficulty": travel_difficulty_enum.moderate,
        "base_danger": travel_danger_enum.moderate_risk
    },
    "Gnisis <-> Khuul": {
        "base_travel_time": "4 hours",
        "base_difficulty": travel_difficulty_enum.moderate,
        "base_danger": travel_danger_enum.moderate_risk
    },
    "Gnisis <-> Urshilaku Camp": {
        "base_travel_time": "6 hours",
        "base_difficulty": travel_difficulty_enum.hard,
        "base_danger": travel_danger_enum.high_risk
    },
    "Khuul <-> Urshilaku Camp": {
        "base_travel_time": "6 hours",
        "base_difficulty": travel_difficulty_enum.hard,
        "base_danger": travel_danger_enum.high_risk
    },
    "Tel Fyr <-> Azura's Coast": {
        "base_travel_time": "4 hours",
        "base_difficulty": travel_difficulty_enum.treacherous,
        "base_danger": travel_danger_enum.extremely_dangerous
    },
    "Azura's Coast <-> Sadrith Mora": {
        "base_travel_time": "7 hours",
        "base_difficulty": travel_difficulty_enum.hard,
        "base_danger": travel_danger_enum.high_risk
    },
    "Ghostgate <-> Ald'ruhn": {
        "base_travel_time": "5 hours",
        "base_difficulty": travel_difficulty_enum.hard,
        "base_danger": travel_danger_enum.high_risk
    },
    "Ghostgate <-> Berandas Stronghold": {
        "base_travel_time": "7 hours",
        "base_difficulty": travel_difficulty_enum.treacherous,
        "base_danger": travel_danger_enum.extremely_dangerous
    },
    "Berandas Stronghold <-> Ald'ruhn": {
        "base_travel_time": "6 hours",
        "base_difficulty": travel_difficulty_enum.hard,
        "base_danger": travel_danger_enum.high_risk
    },
    "Kogoruhn <-> Ald'ruhn": {
        "base_travel_time": "8 hours",
        "base_difficulty": travel_difficulty_enum.treacherous,
        "base_danger": travel_danger_enum.extremely_dangerous
    },
    "Dushariran Shrine <-> Ald'ruhn": {
        "base_travel_time": "4 hours",
        "base_difficulty": travel_difficulty_enum.moderate,
        "base_danger": travel_danger_enum.moderate_risk
    },
    "Dushariran Shrine <-> Gnisis": {
        "base_travel_time": "6 hours",
        "base_difficulty": travel_difficulty_enum.hard,
        "base_danger": travel_danger_enum.high_risk
    },
    "Arkngthand <-> Balmora": {
        "base_travel_time": "5 hours",
        "base_difficulty": travel_difficulty_enum.moderate,
        "base_danger": travel_danger_enum.moderate_risk
    },
    "Arkngthand <-> Moonmoth Legion Fort": {
        "base_travel_time": "4 hours",
        "base_difficulty": travel_difficulty_enum.easy,
        "base_danger": travel_danger_enum.low_risk
    },
    "Moonmoth Legion Fort <-> Balmora": {
        "base_travel_time": "2 hours",
        "base_difficulty": travel_difficulty_enum.easy,
        "base_danger": travel_danger_enum.low_risk
    },
    "Shulk Egg Mine <-> Balmora": {
        "base_travel_time": "1 hour",
        "base_difficulty": travel_difficulty_enum.easy,
        "base_danger": travel_danger_enum.safe
    },
    "Assu Cave <-> Sadrith Mora": {
        "base_travel_time": "6 hours",
        "base_difficulty": travel_difficulty_enum.moderate,
        "base_danger": travel_danger_enum.moderate_risk
    },
    "Assu Cave <-> Tel Fyr": {
        "base_travel_time": "3 hours",
        "base_difficulty": travel_difficulty_enum.hard,
        "base_danger": travel_danger_enum.high_risk
    },
    "Zainab Camp <-> Sadrith Mora": {
        "base_travel_time": "9 hours",
        "base_difficulty": travel_difficulty_enum.hard,
        "base_danger": travel_danger_enum.high_risk
    },
    "Falensarano Stronghold <-> Sadrith Mora": {
        "base_travel_time": "5 hours",
        "base_difficulty": travel_difficulty_enum.moderate,
        "base_danger": travel_danger_enum.moderate_risk}
}