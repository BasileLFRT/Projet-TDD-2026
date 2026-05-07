import csv

from src.Model.Team import Team


class LoLTeamLoader:
    """Classe pour charger les équipes de League of Legends à partir d'un fichier CSV.
    
    Utilise les colonnes 'team' et 'team_abbreviation' du fichier CSV
    """
    def load_all_teams(self) -> list[Team]:
        """Charge toutes les équipes de League of Legends à partir du fichier CSV et les retourne sous forme de liste d'instances de la classe Team.
        
        Returns:
            list[Team]: Une liste d'instances de la classe Team représentant les équipes de League of Legends.
        
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvé.
            KeyError: Si les colonnes 'team' ou 'team_ab
        """
        teams_list = []
        with open('./data/league_of_legends/team.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                team = Team(
                    id=i,
                    nom=row['team'],
                    abreviation=row['team_abbreviation'],
                    competition_id=None,
                )
                teams_list.append(team)
        return teams_list
