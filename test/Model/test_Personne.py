import datetime
from src.Model.Personne import Personne

def test_personne_constructor_is_ok_with_valid_data():
    p = Personne(nom="Alice", birthdate=datetime.date(1990, 1, 15))
    assert p.nom == "Alice"
 
def test_personne_str_displays_name():
    p = Personne(nom="Alice", birthdate=datetime.date(1990, 1, 15))
    assert str(p) == "Alice"
 
def test_personne_eq_with_same_name():
    p1 = Personne(nom="Alice", birthdate=datetime.date(1990, 1, 15))
    p2 = Personne(nom="Alice", birthdate=datetime.date(2000, 3, 3))
    assert p1 == p2
 
def test_personne_eq_with_different_name():
    p1 = Personne(nom="Alice", birthdate=datetime.date(1990, 1, 15))
    p2 = Personne(nom="Bob",   birthdate=datetime.date(1990, 1, 15))
    assert p1 != p2