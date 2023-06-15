import constants
import copy


if __name__ == "__main__":
    def clean_data():
        players_copy = copy.deepcopy(constants.PLAYERS)
        for player in players_copy:
            height_split = player["height"].split()
            player["height"] = height_split[0]
            if player["experience"] == "YES":
                player["experience"] = True
            else:
                player["experience"] = False
            guardian_split = player["guardians"].split(" and ")
            player["guardians"] = guardian_split
        return players_copy
    

    def experienced_list(players_copy):
        experienced_players = []
        for player in players_copy:
            if player["experience"] == True:
                experienced_players.append(player)
        return experienced_players
    

    def non_experienced_list(players_copy):
        non_experienced_players = []
        for player in players_copy:
            if player["experience"] == False:
                non_experienced_players.append(player)
        return non_experienced_players
    

    def create_teams(team_a, team_b, team_c, players_copy, experienced_players, non_experienced_players):
        teams_copy = copy.deepcopy(constants.TEAMS)
        players_per_team = len(players_copy) / len(teams_copy)
        exp_players_per_team = len(experienced_players) / len(teams_copy)
        nonexp_players_per_team = len(non_experienced_players) / len(teams_copy)
        team_a[0]["name"] = teams_copy[0]
        team_b[0]["name"] = teams_copy[1]
        team_c[0]["name"] = teams_copy[2]
        # Add experienced players to team rosters
        while len(team_a[1]["exp_players"]) < exp_players_per_team:
            add_exp_player = experienced_players[0]
            team_a[1]["exp_players"].append(add_exp_player)
            experienced_players.pop(0)
        while len(team_b[1]["exp_players"]) < exp_players_per_team:
            add_exp_player = experienced_players[0]
            team_b[1]["exp_players"].append(add_exp_player)
            experienced_players.pop(0)
        while len(team_c[1]["exp_players"]) < exp_players_per_team:
            add_exp_player = experienced_players[0]
            team_c[1]["exp_players"].append(add_exp_player)
            experienced_players.pop(0)
        # Add non-experienced players to team rosters
        while len(team_a[2]["nonexp_players"]) < nonexp_players_per_team:
            add_nonexp_player = non_experienced_players[0]
            team_a[2]["nonexp_players"].append(add_nonexp_player)
            non_experienced_players.pop(0)
        while len(team_b[2]["nonexp_players"]) < nonexp_players_per_team:
            add_nonexp_player = non_experienced_players[0]
            team_b[2]["nonexp_players"].append(add_nonexp_player)
            non_experienced_players.pop(0)
        while len(team_c[2]["nonexp_players"]) < nonexp_players_per_team:
            add_nonexp_player = non_experienced_players[0]
            team_c[2]["nonexp_players"].append(add_nonexp_player)
            non_experienced_players.pop(0)
        return team_a, team_b, team_c
    

    def display_league(league):
        for team in league:
            print(f'''  
                    Team name: {team[0]["name"]}
                    Players On Team: {len(team[1]["exp_players"]) + len(team[2]["nonexp_players"])}
                        Experienced Players: {len(team[1]["exp_players"])}
                        Non-Experienced Players: {len(team[2]["nonexp_players"])}
                  ''')
            print("Roster:")
            for player in team[1]["exp_players"]:
                print(f'''{team[1]["exp_players"][0]["name"]}''')

team_a = [{"name":""},{"exp_players":[]},{"nonexp_players":[]}]
team_b = [{"name":""},{"exp_players":[]},{"nonexp_players":[]}]
team_c = [{"name":""},{"exp_players":[]},{"nonexp_players":[]}]



players_copy = clean_data()
experienced_players = experienced_list(players_copy)
non_experienced_players = non_experienced_list(players_copy)
create_teams(team_a, team_b, team_c, players_copy, experienced_players, non_experienced_players)

league = [team_a, team_b, team_c]

display_league(league)

