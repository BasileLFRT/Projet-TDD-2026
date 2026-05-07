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
            if total == 0:
                print(f"\n{label} — {p['player_name']} : Aucun match trouvé.")
            else:
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
        if total1 == 0 and total2 == 0:
            print("Aucun match trouvé pour ces joueurs.")
        else:
            print(f"{'Matchs joués':<20} {str(total1):<25} {str(total2):<25}")
            print(f"{'Victoires':<20} {str(wins1):<25} {str(wins2):<25}")

    elif sport.nom == "starcraft_2":
        name1 = p1["name"]
        name2 = p2["name"]
        wins1 = len(matches_df[((matches_df["player_1"] == name1) & (matches_df["score_player_1"] > matches_df["score_player_2"])) |
                               ((matches_df["player_2"] == name1) & (matches_df["score_player_2"] > matches_df["score_player_1"]))])
        wins2 = len(matches_df[((matches_df["player_1"] == name2) & (matches_df["score_player_1"] > matches_df["score_player_2"])) |
                               ((matches_df["player_2"] == name2) & (matches_df["score_player_2"] > matches_df["score_player_1"]))])
        total1 = len(matches_df[(matches_df["player_1"] == name1) | (matches_df["player_2"] == name1)])
        total2 = len(matches_df[(matches_df["player_1"] == name2) | (matches_df["player_2"] == name2)])
        print(f"\n{'Stat':<20} {name1:<25} {name2:<25}")
        print("-" * 70)
        print(f"{'Nationalité':<20} {str(p1['nationality']):<25} {str(p2['nationality']):<25}")
        print(f"{'Race':<20} {str(p1['race']):<25} {str(p2['race']):<25}")
        print(f"{'Team':<20} {str(p1['team']):<25} {str(p2['team']):<25}")
        if total1 == 0 and total2 == 0:
            print("Aucun match trouvé pour ces joueurs.")
        else:
            print(f"{'Matchs joués':<20} {str(total1):<25} {str(total2):<25}")
            print(f"{'Victoires':<20} {str(wins1):<25} {str(wins2):<25}")

    elif sport.nom == "chess":
        name1 = p1["name"]
        name2 = p2["name"]
        wins1 = len(matches_df[((matches_df["player_1"] == name1) & (pd.to_numeric(matches_df["score_player_1"], errors='coerce') > pd.to_numeric(matches_df["score_player_2"], errors='coerce'))) |
                               ((matches_df["player_2"] == name1) & (pd.to_numeric(matches_df["score_player_2"], errors='coerce') > pd.to_numeric(matches_df["score_player_1"], errors='coerce')))])
        wins2 = len(matches_df[((matches_df["player_1"] == name2) & (pd.to_numeric(matches_df["score_player_1"], errors='coerce') > pd.to_numeric(matches_df["score_player_2"], errors='coerce'))) |
                               ((matches_df["player_2"] == name2) & (pd.to_numeric(matches_df["score_player_2"], errors='coerce') > pd.to_numeric(matches_df["score_player_1"], errors='coerce')))])
        total1 = len(matches_df[(matches_df["player_1"] == name1) | (matches_df["player_2"] == name1)])
        total2 = len(matches_df[(matches_df["player_1"] == name2) | (matches_df["player_2"] == name2)])
        print(f"\n{'Stat':<20} {name1:<25} {name2:<25}")
        print("-" * 70)
        print(f"{'Fédération':<20} {str(p1['federation']):<25} {str(p2['federation']):<25}")
        print(f"{'Titre FIDE':<20} {str(p1['fide_title']):<25} {str(p2['fide_title']):<25}")
        print(f"{'Rating std':<20} {str(p1['rating_standard']):<25} {str(p2['rating_standard']):<25}")
        if total1 == 0 and total2 == 0:
            print("Aucun match trouvé pour ces joueurs.")
        else:
            print(f"{'Matchs joués':<20} {str(total1):<25} {str(total2):<25}")
            print(f"{'Victoires':<20} {str(wins1):<25} {str(wins2):<25}")

    elif sport.nom == "volleyball":
        name1 = p1["name"]
        name2 = p2["name"]
        country1 = p1["country_code"]
        country2 = p2["country_code"]
        if competition.nom == "volleyball_men":
            team1_col, team2_col = "country_code_1", "country_code_2"
            key1, key2 = country1, country2
        else:
            team1_col, team2_col = "country_1", "country_2"
            country_mapping = {
                "ARG": "Argentina", "BRA": "Brazil", "CAN": "Canada", "CHN": "China",
                "DOM": "Dominican Republic", "EGY": "Egypt", "FRA": "France",
                "GER": "Germany", "ITA": "Italy", "JPN": "Japan", "KEN": "Kenya",
                "NED": "Netherlands", "POL": "Poland", "SLO": "Slovenia",
                "SRB": "Serbia", "TUR": "Türkiye", "USA": "United States"
            }
            key1 = country_mapping.get(country1, country1)
            key2 = country_mapping.get(country2, country2)
        def count_wins(key):
            m = matches_df[(matches_df[team1_col] == key) | (matches_df[team2_col] == key)]
            return len(m[
                ((m[team1_col] == key) & (m["set_country_1"] > m["set_country_2"])) |
                ((m[team2_col] == key) & (m["set_country_2"] > m["set_country_1"]))
            ])
        wins1 = count_wins(key1)
        wins2 = count_wins(key2)
        total1 = len(matches_df[(matches_df[team1_col] == key1) | (matches_df[team2_col] == key1)])
        total2 = len(matches_df[(matches_df[team1_col] == key2) | (matches_df[team2_col] == key2)])
        print(f"\n{'Stat':<20} {name1:<25} {name2:<25}")
        print("-" * 70)
        print(f"{'Pays':<20} {country1:<25} {country2:<25}")
        print(f"{'Taille':<20} {str(p1['height']):<25} {str(p2['height']):<25}")
        if total1 == 0 and total2 == 0:
            print("Aucun match trouvé pour ces joueurs.")
        else:
            print(f"{'Matchs joués':<20} {str(total1):<25} {str(total2):<25}")
            print(f"{'Victoires':<20} {str(wins1):<25} {str(wins2):<25}")

    elif sport.nom == "badminton":
        name1 = p1["name"]
        name2 = p2["name"]
        wins1 = len(matches_df[matches_df["winner"] == name1])
        wins2 = len(matches_df[matches_df["winner"] == name2])
        total1 = len(matches_df[(matches_df["player_1"] == name1) | (matches_df["player_2"] == name1)])
        total2 = len(matches_df[(matches_df["player_1"] == name2) | (matches_df["player_2"] == name2)])
        print(f"\n{'Stat':<20} {name1:<25} {name2:<25}")
        print("-" * 70)
        print(f"{'Pays':<20} {str(p1['country']):<25} {str(p2['country']):<25}")
        print(f"{'Continent':<20} {str(p1['continent']):<25} {str(p2['continent']):<25}")
        if total1 == 0 and total2 == 0:
            print("Aucun match trouvé pour ces joueurs.")
        else:
            print(f"{'Matchs joués':<20} {str(total1):<25} {str(total2):<25}")
            print(f"{'Victoires':<20} {str(wins1):<25} {str(wins2):<25}")

    elif sport.nom == "league_of_legends":
        name1 = f"{p1['name']} ({p1['pseudo']})"
        name2 = f"{p2['name']} ({p2['pseudo']})"
        blue_cols = ["top_team_blue", "jungle_team_blue", "mid_team_blue", "bot_team_blue", "sup_team_blue"]
        red_cols = ["top_team_red", "jungle_team_red", "mid_team_red", "bot_team_red", "sup_team_red"]
        def count_wins_lol(pseudo):
            played = matches_df[matches_df[blue_cols + red_cols].isin([pseudo]).any(axis=1)]
            return len(played[
                (played[blue_cols].isin([pseudo]).any(axis=1) & (played["winner"] == played["team_blue"])) |
                (played[red_cols].isin([pseudo]).any(axis=1) & (played["winner"] == played["team_red"]))
            ])
        def count_played_lol(pseudo):
            return len(matches_df[matches_df[blue_cols + red_cols].isin([pseudo]).any(axis=1)])
        wins1 = count_wins_lol(p1["pseudo"])
        wins2 = count_wins_lol(p2["pseudo"])
        total1 = count_played_lol(p1["pseudo"])
        total2 = count_played_lol(p2["pseudo"])
        print(f"\n{'Stat':<20} {name1:<30} {name2:<30}")
        print("-" * 80)
        print(f"{'Pays':<20} {str(p1['country_of_birth']):<30} {str(p2['country_of_birth']):<30}")
        print(f"{'Rôle':<20} {str(p1['role']):<30} {str(p2['role']):<30}")
        print(f"{'Équipe':<20} {str(p1['team']):<30} {str(p2['team']):<30}")
        if total1 == 0 and total2 == 0:
            print("Aucun match trouvé pour ces joueurs.")
        else:
            print(f"{'Matchs joués':<20} {str(total1):<30} {str(total2):<30}")
            print(f"{'Victoires':<20} {str(wins1):<30} {str(wins2):<30}")

    elif sport.nom == "counter_strike_2":
        name1 = f"{p1['name']} ({p1['pseudo']})"
        name2 = f"{p2['name']} ({p2['pseudo']})"
        def count_cs2(team):
            played = matches_df[(matches_df["team_1"] == team) | (matches_df["team_2"] == team)]
            wins = played[((played["team_1"] == team) & (played["score_team_1"] > played["score_team_2"])) |
                          ((played["team_2"] == team) & (played["score_team_2"] > played["score_team_1"]))]
            return len(played), len(wins)
        total1, wins1 = count_cs2(p1["team"])
        total2, wins2 = count_cs2(p2["team"])
        print(f"\n{'Stat':<20} {name1:<30} {name2:<30}")
        print("-" * 80)
        print(f"{'Nationalité':<20} {str(p1['nationality']):<30} {str(p2['nationality']):<30}")
        print(f"{'Rôle':<20} {str(p1['role']):<30} {str(p2['role']):<30}")
        print(f"{'Équipe':<20} {str(p1['team']):<30} {str(p2['team']):<30}")
        if total1 == 0 and total2 == 0:
            print("Aucun match trouvé pour ces joueurs.")
        else:
            print(f"{'Matchs joués':<20} {str(total1):<30} {str(total2):<30}")
            print(f"{'Victoires':<20} {str(wins1):<30} {str(wins2):<30}")

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