from src.Model.Team import Team

def test_team_constructor_is_ok_with_valid_data():
    team = Team(id=1, nom="FURIA", abreviation="FUR", competition_id=10)
    assert team.id == 1
    assert team.nom == "FURIA"
    assert team.abreviation == "FUR"
    assert team.competition_id == 10
 
def test_team_players_is_empty_on_init():
    team = Team(id=1, nom="FURIA", abreviation="FUR", competition_id=10)
    assert team.get_players() == []
 
def test_team_str_displays_name():
    team = Team(id=1, nom="FURIA", abreviation="FUR", competition_id=10)
    assert str(team) == "FURIA"