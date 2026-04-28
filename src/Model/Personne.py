import datetime


class Personne:
    def __init__(self, nom: str, birthdate: datetime.date) -> None:
        self._nom = nom
        self._birthdate = birthdate

    @property
    def nom(self) -> str:
        return self._nom

    def __str__(self) -> str:
        return self._nom

    def __repr__(self) -> str:
        return f"Personne(nom='{self._nom}')"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Personne):
            return NotImplemented
        return self._nom == other._nom

    def __hash__(self) -> int:
        return hash(self._nom)