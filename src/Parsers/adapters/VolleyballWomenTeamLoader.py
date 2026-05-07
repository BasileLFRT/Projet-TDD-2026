import csv
from src.Model.Team import Team

class VolleyballWomenTeamLoader:
    """Classe pour charger les sélections de volley féminin à partir d'un fichier CSV.
    
    Utilise les colonnes 'country_1' et 'country_2' du fichier CSV pour extraire les équipes.
    """
    def load_all_teams(self) -> list[Team]:
        """Charge toutes les sélections de volley féminin à partir du fichier CSV et les retourne sous forme de liste d'instances de la classe Team.
        
        Returns:
            list[Team]: Une liste d'instances de la classe Team représentant les équipes de volleyball
            
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvé.
            KeyError: Si les colonnes 'country_1' ou 'country_2' manquent
        """
        teams_set = set()
        with open('./data/volleyball/match_women.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                teams_set.add(row['country_1'])
                teams_set.add(row['country_2'])
        return [Team(id=None, nom=t, abreviation=t, competition_id=None) for t in sorted(teams_set)]