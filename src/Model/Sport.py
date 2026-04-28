class Sport:
    SPORTS_AUTORISES = ["football"]

    def __init__(self, nom: str):
        if nom not in self.SPORTS_AUTORISES:
            raise ValueError(f"Sport non autorisé. Choisir parmi : {self.SPORTS_AUTORISES}")
        self.nom = nom