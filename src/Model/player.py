import datetime
from .personne import Personne

class Player:
    def __init__(id : int, nom : str, birthdate : datetime.date, team_id : int, stats : dict[str, list[float]]) -> None:
        self.id = id
        self.nom = nom
        self.birthdate = birthdate
        self.team_id = team_id
        self.stats = stats
