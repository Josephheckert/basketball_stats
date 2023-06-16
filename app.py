import constants
import copy


if __name__ == "__main__":

    team_a = [
    {"name":""},
    {"roster":[]},
    [], # List of player names only
    [], # List of guardian(s) names only
    [], # List of experienced players
    []  # List of non-experienced players
    ] 
    team_b = [
    {"name":""},
    {"roster":[]},
    [], # List of player names only
    [], # List of guardian(s) names only
    [], # List of experienced players
    []  # List of non-experienced players
    ] 
    team_c = [
    {"name":""},
    {"roster":[]},
    [], # List of player names only
    [], # List of guardian(s) names only
    [], # List of experienced players
    []  # List of non-experienced players
    ] 
    league = [team_a, team_b, team_c]




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
    

    def create_teams(league, team_a, team_b, team_c, players_copy, experienced_players, non_experienced_players):
        teams_copy = copy.deepcopy(constants.TEAMS)
        team_a[0]["name"] = teams_copy[0]
        team_b[0]["name"] = teams_copy[1]
        team_c[0]["name"] = teams_copy[2]
        exp_players_count = 0
        nonexp_players_count = 0
        players_per_team = len(players_copy) / len(teams_copy)
        exp_players_per_team = len(experienced_players) / len(teams_copy)
        nonexp_players_per_team = len(non_experienced_players) / len(teams_copy)
        for team in league:
            while len(team[1]["roster"]) < players_per_team:
                if exp_players_count < exp_players_per_team:
                    exp_player = experienced_players[0]
                    team[1]["roster"].append(exp_player)
                    team[2].append(exp_player["name"])
                    team[3].append(exp_player["guardians"])
                    team[4].append(exp_player)
                    experienced_players.pop(0)
                    exp_players_count += 1
                else:
                    break
                if nonexp_players_count < nonexp_players_per_team:
                    nonexp_player = non_experienced_players[0]
                    team[1]["roster"].append(nonexp_player)
                    team[2].append(nonexp_player["name"])
                    team[3].append(nonexp_player["guardians"])
                    team[5].append(nonexp_player)
                    non_experienced_players.pop(0)
                    nonexp_players_count += 1
                else:
                    break
                exp_players_count = 0
                nonexp_players_count = 0
        return team_a, team_b, team_c
    

    def menu_select():
        print(f"""---- MENU -----
                  
  Here are your choices:
    A) Display Team Stats
    B) Quit
""")
        main_menu_choice = input("Enter an option:    ").lower()
        if main_menu_choice != "a" and main_menu_choice != "b":
            print("Sorry, that's an invalid selection. Please choose one of the available options.\n")
        else:
            main_menu = main_menu_choice
            return main_menu


    def print_team(team_print):
        continue_prog = "y"
        guardians_list = ''
        for guardian in team_print[3]:
            guardians_list += ", ".join(guardian) + ", "
        guardians_list = guardians_list[:-2]
        player_count = len(team_print[4]) + len(team_print[5])
        experienced_players_count = len(team_print[4])
        non_experienced_players_count = len(team_print[5])
        key = "height"
        agg_height = 0
        for player in team_print[1]["roster"]:
            if key in player:
                agg_height += int(player["height"])
        avg_height = agg_height / player_count
        print(f'''
---- ROSTER ----
              
PLAYERS: 
    {", ".join(team_print[2])}
    
GUARDIANS:''')

        print(f'''    {guardians_list}

STATS:
    Player Count: {player_count}
    Experienced Players: {experienced_players_count}
    Non-Experienced Players: {non_experienced_players_count}
    Average Height: {avg_height}
    ''')


    def continue_program():
        continue_prog = "y"
        while continue_prog == "y":
            prompt = input(f'''
Would you like to continue?  Y/N    ''').lower()
            if prompt != "y" and prompt != "n":
                print("Sorry, that's not a valid entry. Please enter Y or N")
            elif prompt == "n":
                print("Have a great day! <END>")
                continue_prog = "n"
                return continue_prog
            else:
                continue_prog = "y"
                print("\n")
                return continue_prog


    def display_league(league):
        main_menu = menu_select()
        while main_menu == "a":
            print(f'''---- TEAMS ----
                  
    A) {team_a[0]["name"]}
    B) {team_b[0]["name"]}
    C) {team_c[0]["name"]}
''')
            team_choice = input("Enter an option:    ").lower()
            if team_choice == "a":
                team_print = team_a
                print_team(team_print)
                continue_prog = continue_program()
                if continue_prog == "n":
                    return
                main_menu = menu_select()
            elif team_choice == "b":
                team_print = team_b
                print_team(team_print)
                continue_prog = continue_program()
                if continue_prog == "n":
                    return
                main_menu = menu_select()
            elif team_choice == "c":
                team_print = team_c
                print_team(team_print)
                continue_prog = continue_program()
                if continue_prog == "n":
                    return
                main_menu = menu_select()




players_copy = clean_data()
experienced_players = experienced_list(players_copy)
non_experienced_players = non_experienced_list(players_copy)
create_teams(league, team_a, team_b, team_c, players_copy, experienced_players, non_experienced_players)
display_league(league)
