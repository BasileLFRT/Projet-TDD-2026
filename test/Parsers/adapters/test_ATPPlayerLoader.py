from src.Parsers.adapters.ATPPlayerLoader import ATPPlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_atp_player_loader_returns_list_of_players():
    fake_csv = [
        {"name_first": "Alexander", "name_last": "Zverev", "player_id": "100644"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = ATPPlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "Alexander Zverev"
    assert players[0].player_api_id == "100644"