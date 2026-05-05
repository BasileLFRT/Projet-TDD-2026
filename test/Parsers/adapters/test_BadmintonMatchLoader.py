from src.Parsers.adapters.BadmintonMatchLoader import BadmintonMatchLoader
from src.Model.Match import Match
import unittest.mock as mock

def test_badminton_match_loader_returns_list_of_matches():
    fake_csv = [
        {"tournament": "Malaysia Masters", "city": "Kuala Lumpur", "country": "Malaysia", "date": "2020-01-07", "tournament_type": "Super 500", "round": "QF", "player_1": "Lyanny Mainaky", "player_2": "Xuefei Qi", "winner": "Xuefei Qi", "game_1_score": "10-21", "game_2_score": "15-21", "game_3_score": ""}
    ]
    with mock.patch("builtins.open", mock.mock_open()), \
         mock.patch("csv.DictReader", return_value=fake_csv):
        matches = BadmintonMatchLoader().load_all_matches()
    assert len(matches) == 1
    assert isinstance(matches[0], Match)
    assert matches[0].team1 == "Lyanny Mainaky"
    assert matches[0].date == "2020-01-07"