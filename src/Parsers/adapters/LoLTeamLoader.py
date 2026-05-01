import csv

from src.Model.Team import Team


class LoLTeamLoader:
    def load_all_teams(self) -> list[Team]:
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
