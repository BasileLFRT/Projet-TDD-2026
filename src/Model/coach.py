from .personne import Personne
import datetime


class Coach(Personne):
    def __init__(self, nom: str, birthdate: datetime.date, team_id: str, fonction: str):
        super().__init__(nom, birthdate)
        self.team_id = team_id
        self.fonction = fonction
