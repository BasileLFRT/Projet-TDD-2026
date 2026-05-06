import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport

def show_player_profile(players_df, sport: Sport, competition: Competition = None):
    if sport.nom == "tennis":
        players_df["full_name"] = players_df["name_first"] + " " + players_df["name_last"]
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['full_name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        p = players_df.loc[index]
        player_id = str(p["player_id"])
        matches_df = pd.read_csv(f"./data/tennis/{competition.nom}_matches_2024.csv")
        played = matches_df[(matches_df["winner_id"].astype(str) == player_id) | (matches_df["loser_id"].astype(str) == player_id)]
        wins = matches_df[matches_df["winner_id"].astype(str) == player_id]
        print(f"\n--- {p['name_first']} {p['name_last']} ---")
        print("\nInfos personnelles :")
        print(f"  Date de naissance : {p['dob']}")
        print(f"  Nationalité : {p['ioc']}")
        print(f"  Taille : {p['height']} cm")
        print(f"  Main dominante : {p['hand']}")
        print("\nStats :")
        print(f"  Matchs joués : {len(played)}")
        print(f"  Matchs gagnés : {len(wins)}")

    elif competition and competition.nom == "european_leagues":
        teams_df = pd.read_csv("./data/football_european_leagues/team.csv")
        matches_df = pd.read_csv("./data/football_european_leagues/match.csv")
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['player_name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        p = players_df.loc[index]
        player_id = p["player_api_id"]
        home_cols = [f"home_player_{i}" for i in range(1, 12)]
        away_cols = [f"away_player_{i}" for i in range(1, 12)]
        home_matches = matches_df[matches_df[home_cols].isin([player_id]).any(axis=1)]
        away_matches = matches_df[matches_df[away_cols].isin([player_id]).any(axis=1)]
        home_wins = home_matches[home_matches["home_team_goal"] > home_matches["away_team_goal"]]
        away_wins = away_matches[away_matches["away_team_goal"] > away_matches["home_team_goal"]]
        total_matches = len(home_matches) + len(away_matches)
        total_wins = len(home_wins) + len(away_wins)
        team_id = None
        if len(home_matches) > 0:
            team_id = home_matches.iloc[-1]["home_team_api_id"]
        elif len(away_matches) > 0:
            team_id = away_matches.iloc[-1]["away_team_api_id"]
        team_name = teams_df[teams_df["team_api_id"] == team_id].iloc[0]["team_long_name"] if team_id else "Inconnue"
        print(f"\n--- {p['player_name']} ---")
        print("\nInfos personnelles :")
        print(f"  Date de naissance : {p['birthday']}")
        print(f"  Taille : {p['height (cm)']} cm")
        print(f"  Poids : {p['weight (kg)']} kg")
        print("\nÉquipe :")
        print(f"  Équipe : {team_name}")
        print("\nStats :")
        print(f"  Matchs joués : {total_matches}")
        print(f"  Matchs gagnés : {total_wins}")

    elif competition and competition.nom == "champions_league":
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['player_name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        p = players_df.loc[index]
        matches_df = pd.read_csv("./data/football_champions_league/match.csv")
        club = p["club"]
        home_matches = matches_df[matches_df["team_home"] == club]
        away_matches = matches_df[matches_df["team_away"] == club]
        home_wins = home_matches[home_matches["score_team_home"] > home_matches["score_team_away"]]
        away_wins = away_matches[away_matches["score_team_away"] > away_matches["score_team_home"]]
        print(f"\n--- {p['player_name']} ---")
        print("\nÉquipe :")
        print(f"  Club : {p['club']}")
        print(f"  Position : {p['position']}")
        print("\nStats :")
        print(f"  Matchs joués : {p['match_played']}")
        print(f"  Matchs gagnés : {len(home_wins) + len(away_wins)}")
        print(f"  Buts : {p['goals']}")
        print(f"  Passes : {p['assists']}")
        print(f"  Minutes jouées : {p['minutes_played']}")

    elif sport.nom == "starcraft_2":
        for i, row in players_df.iterrows():
            print(f"{i} - {row['name']}")
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        p = players_df.loc[index]
        matches_df = pd.read_csv("./data/starcraft_2/match.csv")
        played = matches_df[(matches_df["player_1"] == p["pseudo"]) | (matches_df["player_2"] == p["pseudo"])]
        wins = played[((played["player_1"] == p["pseudo"]) & (played["score_player_1"] > played["score_player_2"])) |
                      ((played["player_2"] == p["pseudo"]) & (played["score_player_2"] > played["score_player_1"]))]
        print(f"\n--- {p['name']} ({p['pseudo']}) ---")
        print("\nInfos personnelles :")
        print(f"  Nationalité : {p['nationality']}")
        print(f"  Date de naissance : {p['birthdate']}")
        print(f"\nÉquipe :")
        print(f"  Team : {p['team']}")
        print(f"\nStats :")
        print(f"  Race : {p['race']}")
        print(f"  Matchs joués : {len(played)}")
        print(f"  Matchs gagnés : {len(wins)}")

    elif sport.nom == "chess":
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        p = players_df.loc[index]
        matches_df = pd.read_csv("./data/chess/match.csv")
        played = matches_df[(matches_df["player_1"] == p["name"]) | (matches_df["player_2"] == p["name"])]
        wins = played[((played["player_1"] == p["name"]) & (pd.to_numeric(played["score_player_1"], errors='coerce') > pd.to_numeric(played["score_player_2"], errors='coerce'))) |
                      ((played["player_2"] == p["name"]) & (pd.to_numeric(played["score_player_2"], errors='coerce') > pd.to_numeric(played["score_player_1"], errors='coerce')))]
        print(f"\n--- {p['name']} ---")
        print("\nInfos personnelles :")
        print(f"  Année de naissance : {p['birth_year']}")
        print(f"  Genre : {p['gender']}")
        print(f"  Fédération : {p['federation']}")
        print("\nStats :")
        print(f"  Titre FIDE : {p['fide_title']}")
        print(f"  Rating standard : {p['rating_standard']}")
        print(f"  Rating rapide : {p['rating_rapid']}")
        print(f"  Rating blitz : {p['rating_blitz']}")
        print(f"  Matchs joués : {len(played)}")
        print(f"  Matchs gagnés : {len(wins)}")

    else:  # basketball
        teams_df = pd.read_csv("./data/basketball/team.csv")
        players_df["full_name"] = players_df["first_name"] + " " + players_df["last_name"]
        if len(players_df) == 1:
            index = players_df.index[0]
        else:
            for i, row in players_df.iterrows():
                print(f"{i} - {row['full_name']}")
            index = int(input("Sélectionne un joueur (numéro) : "))
        p = players_df.loc[index]
        games_df = pd.read_csv("./data/basketball/game.csv")
        team_id_val = p["team_id"]
        home_matches = games_df[games_df["team_id_home"] == team_id_val]
        away_matches = games_df[games_df["team_id_away"] == team_id_val]
        home_wins = home_matches[home_matches["pts_home"] > home_matches["pts_away"]]
        away_wins = away_matches[away_matches["pts_away"] > away_matches["pts_home"]]
        team_row = teams_df[teams_df["id"] == p["team_id"]]
        team_name = team_row.iloc[0]["full_name"] if len(team_row) > 0 else "Inconnue"
        print(f"\n--- {p['first_name']} {p['last_name']} ---")
        print("\nInfos personnelles :")
        print(f"  Date de naissance : {p['birthdate']}")
        print(f"  Taille : {p['height']}")
        print(f"  Poids : {p['weight']} lbs")
        print("\n Équipe :")
        print(f"  Équipe : {team_name}")
        print(f"  Numéro : {p['jersey']}")
        print(f"  Position : {p['position']}")
        print("\nStats :")
        print(f"  Matchs joués : {len(home_matches) + len(away_matches)}")
        print(f"  Matchs gagnés : {len(home_wins) + len(away_wins)}")