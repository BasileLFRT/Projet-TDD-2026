from src.Analysis.homemade.GoatFinder import find_the_goat
from src.Model.Player import Player
import unittest.mock as mock

def test_find_the_goat():
    player1 = Player(nom="Player 1", birthdate=None, player_api_id="100")
    player2 = Player(nom="Player 2", birthdate=None, player_api_id="200")
    player3 = Player(nom="Spieler 3", birthdate=None, player_api_id="300")
    players_list = [player1, player2, player3]

    fake_csv = [
        {"home_team_goal": "2", "away_team_goal": "0",
         "home_player_1": "300", "home_player_2": "", "home_player_3": "", "home_player_4": "", "home_player_5": "", "home_player_6": "", "home_player_7": "", "home_player_8": "", "home_player_9": "", "home_player_10": "", "home_player_11": "",
         "away_player_1": "100", "away_player_2": "", "away_player_3": "", "away_player_4": "", "away_player_5": "", "away_player_6": "", "away_player_7": "", "away_player_8": "", "away_player_9": "", "away_player_10": "", "away_player_11": ""},
        {"home_team_goal": "1", "away_team_goal": "0",
         "home_player_1": "300", "home_player_2": "", "home_player_3": "", "home_player_4": "", "home_player_5": "", "home_player_6": "", "home_player_7": "", "home_player_8": "", "home_player_9": "", "home_player_10": "", "home_player_11": "",
         "away_player_1": "200", "away_player_2": "", "away_player_3": "", "away_player_4": "", "away_player_5": "", "away_player_6": "", "away_player_7": "", "away_player_8": "", "away_player_9": "", "away_player_10": "", "away_player_11": ""},
    ]

    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        goat = find_the_goat(players_list)

    assert goat.nom == "Spieler 3"