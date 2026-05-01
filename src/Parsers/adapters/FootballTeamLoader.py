import csv

from src.Model.Team import Team


class FootballTeamLoader:
    def load_all_teams(self) -> list[Team]:
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