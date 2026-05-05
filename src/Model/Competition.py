class Competition:
    """Compétition qui regroupe des équipes et qui a lieu au court d'une année.
 
    Parameters
    ----------
    id : int
        Identifiant de la compétition.
    nom : str
        Nom de la compétition.
    sport : str
        Sport pratiqué dans la compétition.
    annee : int
        Année de la compétition.
        """
    def __init__(self, id: int, nom: str, sport: str, annee: int):
        self.id = id
        self.nom = nom
        self.sport = sport
        self.annee = annee

    def get_classement(self) -> list:
        """Retourne le classement de la compétition.
 
        Returns
        -------
        list
            Classement des équipes.
        """
        # à implémenter
        pass

    def get_phases(self) -> list:
        """Retourne les phases de la compétition.
 
        Returns
        -------
        list
            Liste des phases. 
            """
        return []

    def get_teams(self) -> list:
        """Retourne les équipes participant à la compétition.
 
        Returns
        -------
        list
            Liste des équipes.
            """
        return []