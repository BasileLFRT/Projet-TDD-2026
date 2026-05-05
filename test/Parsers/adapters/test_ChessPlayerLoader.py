from src.Parsers.adapters.ChessPlayerLoader import ChessPlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_chess_player_loader_returns_list_of_players():
    fake_csv = [
        {"name": "Gukesh D", "fide_id": "46616543", "birth_year": "2006", "gender": "Male", "federation": "India", "fide_title": "Grandmaster", "rating_standard": "2794", "rating_rapid": "2756", "rating_blitz": "2743"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = ChessPlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "Gukesh D"
    assert players[0].player_api_id == "46616543"