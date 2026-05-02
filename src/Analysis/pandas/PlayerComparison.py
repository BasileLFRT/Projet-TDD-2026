import pandas as pd
from src.Model.Competition import Competition
from src.Model.Sport import Sport

def show_player_comparison(players_df, matches_df, sport: Sport, competition: Competition = None, choix_recherche_1 = None, choix_recherche_2 = None):
    p1 = players_df.iloc[choix_recherche_1]
    p2 = players_df.iloc[choix_recherche_2]

    if competition and competition.nom == "european_leagues":        
        print(f"\n{'Stat':<20} {'Joueur 1':<25} {'Joueur 2':<25}")
        print("-" * 70)
        print(f"{'Nom':<20} {p1['player_name']:<25} {p2['player_name']:<25}")
        print(f"{'Taille (cm)':<20} {str(p1['height (cm)']):<25} {str(p2['height (cm)']):<25}")
        print(f"{'Poids (kg)':<20} {str(p1['weight (kg)']):<25} {str(p2['weight (kg)']):<25}")

        for p, label in [(p1, "Joueur 1"), (p2, "Joueur 2")]:
            pid = p["player_api_id"]
            home_cols = [f"home_player_{i}" for i in range(1, 12)]
            away_cols = [f"away_player_{i}" for i in range(1, 12)]
            home_m = matches_df[matches_df[home_cols].isin([pid]).any(axis=1)]
            away_m = matches_df[matches_df[away_cols].isin([pid]).any(axis=1)]
            wins = len(home_m[home_m["home_team_goal"] > home_m["away_team_goal"]]) + \
                   len(away_m[away_m["away_team_goal"] > away_m["home_team_goal"]])
            total = len(home_m) + len(away_m)
            print(f"\n{label} — {p['player_name']} : {total} matchs, {wins} victoires")

    elif competition and competition.nom == "champions_league":
        print(f"\n{'Stat':<20} {str(p1['player_name']):<25} {str(p2['player_name']):<25}")
        print("-" * 70)
        for col in ["position", "club", "goals", "assists", "minutes_played", "match_played"]:
            print(f"{col:<20} {str(p1[col]):<25} {str(p2[col]):<25}")

    elif sport.nom == "tennis":
        name1 = f"{p1['name_first']} {p1['name_last']}"
        name2 = f"{p2['name_first']} {p2['name_last']}"
        pid1 = str(p1["player_id"])
        pid2 = str(p2["player_id"])
        wins1 = len(matches_df[matches_df["winner_id"].astype(str) == pid1])
        wins2 = len(matches_df[matches_df["winner_id"].astype(str) == pid2])
        total1 = len(matches_df[(matches_df["winner_id"].astype(str) == pid1) | (matches_df["loser_id"].astype(str) == pid1)])
        total2 = len(matches_df[(matches_df["winner_id"].astype(str) == pid2) | (matches_df["loser_id"].astype(str) == pid2)])
        print(f"\n{'Stat':<20} {name1:<25} {name2:<25}")
        print("-" * 70)
        print(f"{'Taille':<20} {str(p1['height']):<25} {str(p2['height']):<25}")
        print(f"{'Main':<20} {str(p1['hand']):<25} {str(p2['hand']):<25}")
        print(f"{'Matchs joués':<20} {str(total1):<25} {str(total2):<25}")
        print(f"{'Victoires':<20} {str(wins1):<25} {str(wins2):<25}")

    else:  # basketball
        name1 = f"{p1['first_name']} {p1['last_name']}"
        name2 = f"{p2['first_name']} {p2['last_name']}"
        teams_df = pd.read_csv("./data/basketball/team.csv")
        team1 = teams_df[teams_df["id"] == p1["team_id"]].iloc[0]["full_name"]
        team2 = teams_df[teams_df["id"] == p2["team_id"]].iloc[0]["full_name"]
        print(f"\n{'Stat':<20} {name1:<25} {name2:<25}")
        print("-" * 70)
        print(f"{'Équipe':<20} {team1:<25} {team2:<25}")
        print(f"{'Position':<20} {str(p1['position']):<25} {str(p2['position']):<25}")
        print(f"{'Taille':<20} {str(p1['height']):<25} {str(p2['height']):<25}")
        print(f"{'Poids':<20} {str(p1['weight']):<25} {str(p2['weight']):<25}")