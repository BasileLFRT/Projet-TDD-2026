from .Personne import Personne

class Player(Personne):
    """Joueur, extension de Personne.
 
    Parameters
    ----------
    nom : str
        Nom du joueur.
    birthdate : datetime.date
        Date de naissance du joueur.
    player_api_id : str, optional
        Identifiant optionnel du joueur dans la source de données externe (pseudo,
        identifiant numérique, etc.)
        """
    def __init__(self, nom: str, birthdate, player_api_id=None):
        super().__init__(nom, birthdate)
        self.player_api_id = player_api_id