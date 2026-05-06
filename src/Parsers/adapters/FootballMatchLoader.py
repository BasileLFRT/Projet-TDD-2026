import csv
from src.Model.Match import Match

class FootballMatchLoader:
    """
    Charge les matchs de football depuis match.csv issu du Football européen
    avec les colonnes match_api_id, date, home_team_api_id, away_team_api_id, home_team_goal et away_team_goal
    """

    @staticmethod
    def load_all_matches() -> list[Match]:
        """
        Lit le fichier CSV et retourne la liste de tous les matchs.

        Chaque ligne est convertie en instance de Match.
        Les scores sont lus dans le CSV et valent 0 si ils sont nuls dans le fichier

        Returns:
            list[Match]: Liste des matchs chargés, vide si le fichier l'est

        Raises:
            FileNotFoundError: Si le fichier CSV est introuvable
            ValueError: Si les colonnes de score contiennent une valeur non convertible en entier.
            KeyError: Si une colonne obligatoire est absente du CSV.
        """
        liste_matchs = []
        with open('./data/football_european_leagues/match.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                match = Match(
                    match_id=row.get("match_api_id"),
                    date=row.get("date"),
                    team1=row.get("home_team_api_id"),
                    team2=row.get("away_team_api_id"),
                    score1=int(row.get("home_team_goal") or 0),
                    score2=int(row.get("away_team_goal") or 0),
                )
                liste_matchs.append(match)
        return liste_matchs