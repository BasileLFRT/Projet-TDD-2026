import csv
from src.Model.Team import Team

class CS2TeamLoader:
    def load_all_teams(self) -> list[Team]:
        teams_list = []
        with open('./data/counter_strike_2/team.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                team = Team(
                    id=None,
                    nom=row.get('team'),
                    abreviation=row.get('team_abbreviation'),
                    competition_id=None,
                )
                teams_list.append(team)
        return teams_list