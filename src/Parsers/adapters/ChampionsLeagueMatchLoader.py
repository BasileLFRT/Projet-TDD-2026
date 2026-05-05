import csv
from src.Model.Match import Match

class ChampionsLeagueMatchLoader:
    """Classe permettant de charger des matchs de la Ligue des Champions(Foot) depuis un fichier CSV.
    
    Lit les données du fichier match.csv lié au football et en crée des instances de Match
    avec les colonnes: date, team_home, team_away, score_team_home, score_team_away.
    Le champ match_id est laissé à None au chargement et doit être assigné manuellement
    """
    def load_all_matches(self) -> list[Match]:
        """Lit le fichier CSV et retourne la liste de tous les matchs.
        
        Chaque ligne est convertie en objet Match.
        Le champ match_id est initialisé à None
        Il doit être renseigné manuellement.

        Returns:
            list[Match]: Liste des matchs chargés.
                        Vide si le fichier ne contient aucune ligne de données.
        
        Raises:
            FileNotFoundError: Si le fichier CSV est introuvable
            KeyError: Si une colonne obligatoire est absente du CSV.
        """
        liste_matchs = []
        with open('./data/football_champions_league/match.csv', newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                match = Match(
                    match_id=None,
                    date=row.get("date"),
                    team1=row.get("team_home"),
                    team2=row.get("team_away"),
                    score1=int(row.get("score_team_home") or 0),
                    score2=int(row.get("score_team_away") or 0),
                )
                liste_matchs.append(match)
        return liste_matchs