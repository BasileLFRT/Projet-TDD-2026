from src.Parsers.adapters.CS2PlayerLoader import CS2PlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_cs2_player_loader_returns_list_of_players():
    fake_csv = [
        {"pseudo": "yuurih", "name": "Yuri Gomes dos Santos Boian", "nationality": "Brazil", "birthdate": "1999-12-22", "role": "rifler", "team": "FURIA"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = CS2PlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "Yuri Gomes dos Santos Boian"
    assert players[0].player_api_id == "yuurih"