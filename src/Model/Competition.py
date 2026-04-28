class Competition:
    def __init__(self, id: int, nom: str, sport: str, annee: int):
        self.id = id
        self.nom = nom
        self.sport = sport
        self.annee = annee

    def get_classement(self) -> list:
        # à implémenter
        pass

    def get_phases(self) -> list:
        return []

    def get_teams(self) -> list:
        return []