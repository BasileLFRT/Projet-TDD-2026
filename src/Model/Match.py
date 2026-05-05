import datetime

class Match:
    """Match entre deux équipes avec leurs scores.
 
    Parameters
    ----------
    match_id : int
        Identifiant du match.
    date : datetime.date
        Date du match.
    team1 : str
        Nom de la première équipe.
    team2 : str
        Nom de la deuxième équipe.
    score1 : int
        Score de la première équipe.
    score2 : int
        Score de la deuxième équipe.
        """
    def __init__(self, match_id: int, date:datetime, team1:str, team2:str, score1:int, score2:int):
        self.match_id = match_id
        self.date = date
        self.team1 = team1
        self.team2 = team2
        self.score1 = score1
        self.score2 = score2

    def winner(self):
        """Calcule l'équipe gagnante du match.
 
        Returns
        -------
        str or None
            Nom de l'équipe gagnante, ou None en cas d'égalité.
            """
        if self.score1 > self.score2:
            return self.team1
        elif self.score2 > self.score1:
            return self.team2
        return None

    def __str__(self):
        """Résumé du match.
 
        Returns
        -------
        str
            Format : ``date | equipe1 score1 - score2 equipe2``.
            """
        return f"{self.date} | {self.team1} {self.score1} - {self.score2} {self.team2}"

    def __repr__(self):
        """Représentation lisible du match.
 
        Returns
        -------
        str
            Représentation.
            """
        return (
            f"Match(date='{self.date}', "
            f"team1='{self.team1}', team2='{self.team2}', "
            f"score1={self.score1}, score2={self.score2}')"
        )
