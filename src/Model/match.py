from datetime import date
from team import Equipe

class Match:
    """
    Classe définissant un match entre deux équipes à une date donnée
    """
    def __init__(self, id: int, date:datetime.date, equipe_1: Equipe, equipe_2: Equipe, stats: dict) -> None:
            self._id = id
            self._date = date
            self._equipe_1 = equipe_1
            self._equipe_2 = equipe_2
            self._stats = stats