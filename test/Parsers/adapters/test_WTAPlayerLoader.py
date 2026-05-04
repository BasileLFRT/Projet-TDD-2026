from src.Parsers.adapters.WTAPlayerLoader import WTAPlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_wta_player_loader_returns_list_of_players():
    fake_csv = [
        {"name_first": "Iga", "name_last": "Swiatek", "player_id": "216347"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = WTAPlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "Iga Swiatek"
    assert players[0].player_api_id == "216347"