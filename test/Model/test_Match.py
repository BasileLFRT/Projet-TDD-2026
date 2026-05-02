from src.Model.Match import Match

def test_match_constructor_is_ok_with_valid_data():
    match = Match(match_id="1", date="2024-01-01", team1="Real Madrid", team2="Barcelona", score1=2, score2=1)
    assert match.team1 == "Real Madrid"
    assert match.team2 == "Barcelona"
    assert match.score1 == 2
    assert match.score2 == 1

def test_match_str_displays_correctly():
    match = Match(match_id="1", date="2024-01-01", team1="PSG", team2="Lyon", score1=3, score2=0)
    assert str(match) == "2024-01-01 | PSG 3 - 0 Lyon"