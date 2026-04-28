from .Personne import Personne

class Player(Personne):
    def __init__(self, nom: str, birthdate, player_api_id=None):
        super().__init__(nom, birthdate)
        self.player_api_id = player_api_id