class Team:
    def __init__(self, id: int, nom: str, abreviation: str, competition_id: int):
        self.id = id
        self.nom = nom
        self.abreviation = abreviation
        self.competition_id = competition_id
        self.players = []
        self.stats = {}

    def get_players(self):
        return self.players

    def update_stats(self, match):
        # à implémenter selon les résultats
        pass

    def __str__(self):
        return self.nom
