from src.Parsers.adapters.StarcraftPlayerLoader import StarcraftPlayerLoader
from src.Model.Player import Player
import unittest.mock as mock


def test_starcraft_player_loader_returns_list_of_players():
    fake_csv = [
        {"pseudo": "Zest", "name": "Joo Sung-wook", "nationality": "South Korea",
         "birthdate": "1992-07-11", "race": "Protoss", "team": "KT Rolster"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = StarcraftPlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "Joo Sung-wook"


def test_starcraft_player_loader_returns_empty_list():
    fake_csv = []
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = StarcraftPlayerLoader().load_all_players()
    assert players == []
