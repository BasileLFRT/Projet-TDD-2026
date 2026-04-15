from personne import Personne
import datetime


class Player(Personne):
    def __init__(self, nom: str, birthdate: datetime.date, team_id: str, stats: dict = None):
        super().__init__(nom, birthdate)
        self.team_id = team_id
        self.stats = stats or {}
