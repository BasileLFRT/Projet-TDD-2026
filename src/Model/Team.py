class Team:
    """Équipe qui participe à une compétition
 
    Parameters
    ----------
    id : int
        Identifiant de l'équipe.
    nom : str
        Nom de l'équipe.
    abreviation : str
        Abréviation du nom de l'équipe.
    competition_id : int
        Identifiant de la compétition à laquelle l'équipe participe.
        """
    def __init__(self, id: int, nom: str, abreviation: str, competition_id: int):
        self.id = id
        self.nom = nom
        self.abreviation = abreviation
        self.competition_id = competition_id
        self.players = []
        self.stats = {}

    def get_players(self):
        """Retourne la liste des joueurs de l'équipe.
 
        Returns
        -------
        list
            Liste des joueurs.
        """
        return self.players

    def update_stats(self, match):
        """Met à jour les statistiques de l'équipe à partir d'un match.
 
        Parameters
        ----------
        match : Match
            Match joué par l'équipe.
            """
        # à implémenter selon les résultats
        pass

    def __str__(self):
        """Retourne le nom de l'équipe.
 
        Returns
        -------
        str
            Nom de l'équipe.
            """
        return self.nom
