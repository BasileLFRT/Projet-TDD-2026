import csv

from src.Model.Team import Team


class FootballTeamLoader:
    """Charge les équipes de football depuis team.csv issu du Football européen
    avec les colonnes team_api_id, team_long_name et team_short_name
    """
    def load_all_teams(self) -> list[Team]:
        """Lit le fichier CSV et retourne la liste de toutes les équipes.

        Returns:
            list[Team]: Liste de toutes les équipes de football.
        Raises:
            FileNotFoundError: Si le fichier CSV n'est pas trouvable
            Exception: Pour toute autre erreur lors de la lecture du fichier.
        """
        teams_list = []
        with open('./data/football_european_leagues/team.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team = Team(
                    id=row.get('team_api_id'),
                    nom=row.get('team_long_name'),
                    abreviation=row.get('team_short_name'),
                    competition_id=None,
                )
                teams_list.append(team)
        return teams_list