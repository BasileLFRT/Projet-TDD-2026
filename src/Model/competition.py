from datetime import date
from reglescore import RegleScore

class Competition:
    """
    Classe définissant une compétition représentée par son nom, sa date de début et sa date de fin

    Parameters
    ---------
    nom:str
        Le nom de la compétition
    start_date:datetime.date
        La date de début de la compétition
    end_date:datetime.date
        La date de fin de la compétition
    """
    def __init__(self, id: int, nom: str, sport: str, annee: int, regle: RegleScore) -> None:
            self._id = id
            self._nom = nom
            self._sport = sport
            self._annee = annee
            self._regle = regle