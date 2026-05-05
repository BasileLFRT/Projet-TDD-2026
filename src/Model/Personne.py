import datetime


class Personne:
    """Représente une personne.
 
    Parameters
    ----------
    nom : str
        Nom de la personne.
    birthdate : datetime.date
        Date de naissance de la personne.
        """


    def __init__(self, nom: str, birthdate: datetime.date) -> None:
        self._nom = nom
        self._birthdate = birthdate


    @property
    def nom(self) -> str:
        return self._nom

    def __str__(self) -> str:
        """Retourne le nom de la personne.
 
        Returns
        -------
        str
            Nom de la personne.
            """
        return self._nom

    def __repr__(self) -> str:
        """Représentation technique de la personne.
 
        Returns
        -------
        str
            Représentation.
            """
        return f"Personne(nom='{self._nom}')"

    def __eq__(self, other) -> bool:
        """Test d'égalité basé sur le nom.
 
        Parameters
        ----------
        other : Any
            Objet à comparer.
 
        Returns
        -------
        bool
            True si les deux personnes ont le même nom.
            """
        if not isinstance(other, Personne):
            return NotImplemented
        return self._nom == other._nom

    def __hash__(self) -> int:
        """Hachage basé sur le nom.
 
        Returns
        -------
        int
            Valeur de hachage.
            """
        return hash(self._nom)