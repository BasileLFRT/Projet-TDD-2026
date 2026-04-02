"""Implémentation de la classe _Personne."""
import datetime

class Personne:
    """
    Classe définissant une personne représentée par son nom ou son pseudo et sa date de naissance

    Parameters
    ---------
    nom:str
        Le nom de la personne
    birthdate:datetime.date
        La date de naissance de la personne
    """
    def __init__(self, nom: str, pseudo: str, birthdate: datetime.date) -> None:
            self._nom = nom
            self._pseudo = pseudo
            self._birthdate = birthdate
        
    @property
    def nom(self) -> str:
        if self.nom is not None:
            return self._nom
        else:
            raise ValueError("On ne connaît pas le nom du joueur")

    @property
    def pseudo(self) -> str:
        if self._pseudo is not None:
            return self._pseudo
        else:
            raise ValueError("La personne n'utilise pas de pseudo")


    def __eq__(self, other) -> bool:
        """Permet de comparer deux personnes selon leur pseudo"""
        if not isinstance(other, Personne):
            return NotImplemented
        else:
            return self.nom == other.nom

    def __str__(self) -> str:
        """Affiche le pseudonyme utilisé"""
        return self._nom
    
    def __repr__(self) -> str:
        """Retourner une représentation précise de l'objet """
        return f"Personne(nom='{self._nom}')"

    def __hash__(self) -> int:
        """Associer un entier à un nom pour l'identifier"""
        return hash(self._nom)