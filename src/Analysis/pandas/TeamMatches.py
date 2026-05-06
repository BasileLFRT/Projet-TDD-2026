import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport
from src.Analysis.TeamSearch import TeamSearch
from src.Parsers.TeamLoader import TeamLoader

def show_team_matches(matches_df: pd.DataFrame, sport: Sport, competition: Competition = None, choix_recherche: str = None):
    if sport.nom in ["chess", "badminton", "starcraft_2", "tennis"]:
        raise ValueError("Fonctionnalité non disponible car c'est un sport individuel")

    def get_team_name(teams_df, name_col):
        if choix_recherche == "1":
            from src.Analysis.TeamSearch import TeamSearch
            search_string = input("Nom de l'équipe : ")
            results = [row[name_col] for _, row in teams_df.iterrows() if search_string.lower() in str(row[name_col]).lower()]
            if len(results) == 0:
                raise ValueError(f"Aucune équipe trouvée avec le nom '{search_string}'")
            if len(results) == 1:
                return results[0]
            for i, t in enumerate(results):
                print(f"{i} - {t}")
            return results[int(input("Ton choix : "))]
        else:
            for i, row in teams_df.iterrows():
                print(f"{i} - {row[name_col]}")
            return teams_df.iloc[int(input("Sélectionne une équipe (numéro) : "))][name_col]

    if competition and competition.nom == "european_leagues":
        teams_df = pd.read_csv("./data/football_european_leagues/team.csv")
        team_name = get_team_name(teams_df, "team_long_name")
        team_id = teams_df[teams_df["team_long_name"] == team_name].iloc[0]["team_api_id"]
        team_matches = matches_df[(matches_df["home_team_api_id"] == team_id) | (matches_df["away_team_api_id"] == team_id)]
        for _, match in team_matches.iterrows():
            print(f"{match['date']} | {match['home_team_api_id']} {int(match['home_team_goal'])} - {int(match['away_team_goal'])} {match['away_team_api_id']}")

    elif competition and competition.nom == "champions_league":
        teams = sorted(set(matches_df["team_home"].tolist() + matches_df["team_away"].tolist()))
        if choix_recherche == "1":
            search_string = input("Nom de l'équipe : ")
            results = [t for t in teams if search_string.lower() in t.lower()]
            if len(results) == 0:
                raise ValueError(f"Aucune équipe trouvée avec le nom '{search_string}'")
            team = results[0] if len(results) == 1 else results[int(input("Ton choix : "))]
        else:
            for i, team in enumerate(teams):
                print(f"{i} - {team}")
            team = teams[int(input("Sélectionne une équipe (numéro) : "))]
        team_matches = matches_df[(matches_df["team_home"] == team) | (matches_df["team_away"] == team)]
        for _, match in team_matches.iterrows():
            print(f"{match['date']} | {match['team_home']} {int(match['score_team_home'])} - {int(match['score_team_away'])} {match['team_away']}")

    elif sport.nom == "volleyball":
        if competition.nom == "volleyball_men":
            team1_col, team2_col = "country_code_1", "country_code_2"
        else:
            team1_col, team2_col = "country_1", "country_2"
        teams = sorted(set(matches_df[team1_col].tolist() + matches_df[team2_col].tolist()))
        if choix_recherche == "1":
            search_string = input("Nom de l'équipe : ")
            results = [t for t in teams if search_string.lower() in t.lower()]
            if len(results) == 0:
                raise ValueError(f"Aucune équipe trouvée avec le nom '{search_string}'")
            team = results[0] if len(results) == 1 else results[int(input("Ton choix : "))]
        else:
            for i, team in enumerate(teams):
                print(f"{i} - {team}")
            team = teams[int(input("Sélectionne une équipe (numéro) : "))]

        team_matches = matches_df[(matches_df[team1_col] == team) | (matches_df[team2_col] == team)]
        for _, match in team_matches.iterrows():
            print(f"{match['date']} | {match[team1_col]} {int(match['set_country_1'])} - {int(match['set_country_2'])} {match[team2_col]}")
        return 

    else:  # basketball
        teams_df = pd.read_csv("./data/basketball/team.csv")
        team_name = get_team_name(teams_df, "full_name")
        team_id = teams_df[teams_df["full_name"] == team_name].iloc[0]["id"]
        team_matches = matches_df[(matches_df["team_id_home"] == team_id) | (matches_df["team_id_away"] == team_id)]
        for _, match in team_matches.iterrows():
            print(f"{match['game_date']} | {match['team_id_home']} {int(match['pts_home'])} - {int(match['pts_away'])} {match['team_id_away']}")