from src.Parsers.adapters.BadmintonPlayerLoader import BadmintonPlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_badminton_player_loader_returns_list_of_players():
    fake_csv = [
        {"name": "Akane Yamaguchi", "country": "Japan", "continent": "Asia"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = BadmintonPlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "Akane Yamaguchi"