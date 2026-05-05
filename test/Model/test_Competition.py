from src.Model.Competition import Competition

def test_competition_constructor_is_ok_with_valid_data():
    comp = Competition(id=1, nom="cs2", sport="esport", annee=2024)
    assert comp.id == 1
    assert comp.nom == "cs2"
    assert comp.sport == "esport"
    assert comp.annee == 2024
 
def test_competition_get_phases_returns_empty_list():
    comp = Competition(id=1, nom="cs2", sport="esport", annee=2024)
    assert comp.get_phases() == []
 
def test_competition_get_teams_returns_empty_list():
    comp = Competition(id=1, nom="cs2", sport="esport", annee=2024)
    assert comp.get_teams() == []