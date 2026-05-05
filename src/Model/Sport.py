class Sport:
    """Sport reconnu par l'application : seulement les sports listés dans ``SPORTS_AUTORISES``..
 
    Parameters
    ----------
    nom : str
        Nom du sport.
 
    Raises
    ------
    ValueError
        Si le nom ne figure pas dans ``SPORTS_AUTORISES``.
        """
    SPORTS_AUTORISES = ["football", "basketball", "tennis", "volleyball", "chess", "badminton", "lol", "cs2"]

    def __init__(self, nom: str):
        if nom not in self.SPORTS_AUTORISES:
            raise ValueError(f"Sport non autorisé. Choisir parmi : {self.SPORTS_AUTORISES}")
        self.nom = nom