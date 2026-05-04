from src.Parsers.adapters.BasketballPlayerLoader import BasketballPlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_basketball_player_loader_returns_list_of_players():
    fake_csv = [
        {"first_name": "Precious", "last_name": "Achiuwa", "person_id": "1630173"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = BasketballPlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "Precious Achiuwa"
    assert players[0].player_api_id == "1630173"