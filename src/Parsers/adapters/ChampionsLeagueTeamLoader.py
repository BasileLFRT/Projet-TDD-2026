import csv
from src.Model.Team import Team

class ChampionsLeagueTeamLoader:
    def load_all_teams(self) -> list[Team]:
        teams_list = []
        with open('./data/football_champions_league/team.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team = Team(
                    id=None,
                    nom=row.get('full_name'),
                    abreviation=row.get('short_name'),
                    competition_id=None,
                )
                teams_list.append(team)
        return teams_list