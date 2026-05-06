from src.Parsers.adapters.ChessPlayerLoader import ChessPlayerLoader
from src.Model.Player import Player
import unittest.mock as mock

def test_chess_player_loader_returns_list_of_players():
    fake_csv = [
        {"name": "Abugenda, Nagi", "fide_id": "9202544", "birth_year": "1986", "gender": "Male", "federation": "Libya", "fide_title": "Candidate Master", "rating_standard": "1972", "rating_rapid": "2020", "rating_blitz": "1989"}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        players = ChessPlayerLoader().load_all_players()
    assert len(players) == 1
    assert isinstance(players[0], Player)
    assert players[0].nom == "Nagi Abugenda"
    assert players[0].player_api_id == "9202544"