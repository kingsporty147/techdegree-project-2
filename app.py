import constants

if __name__ == "__main__":
    players = constants.PLAYERS
    teams = constants.TEAMS


def clean_data(players):

    xp_counter = 0

    inxp_counter = 0

    newCollection = []

    for player in players.copy():

        player['guardians'] = player['guardians'].replace('and', ',')

        player['guardians'] = player['guardians'].split(",")

        if player['experience'].lower() == "yes":
            player['experience'] = True
            xp_counter += 1
        else:
            player['experience'] = False
            inxp_counter += 1

        player['height'] = int(player['height'].split(" ")[0])

        newCollection.append(player)

    return newCollection


if __name__ == "__main__":
    clean_players = clean_data(players)


def balance_teams(teams, players):

    team_dic = {}
    number_of_players_per_team = len(players) / len(teams)
    number_of_players_per_team = int(number_of_players_per_team)

    list_of_exp_players = []
    list_of_inexp_players = []

    for player in players:
        if player['experience'] == True:
            list_of_exp_players.append(player)
        elif player['experience'] == False:
            list_of_inexp_players.append(player)

    for team in teams:

        team_dic[team] = list_of_exp_players[0:3] + list_of_inexp_players[0:3]
        del (list_of_exp_players[0:3])
        del (list_of_inexp_players[0:3])

    return team_dic


if __name__ == "__main__":
    balanced_team = balance_teams(teams, clean_players)


def team_stats(userInput):

    team_player = []

    just_player_name = ", "

    experienced_player = 0
    inexperienced_player = 0

    average_height = []

    guardian_names = []

    if userInput.lower() != "a" and userInput.lower() != "b" and userInput.lower() != "c":
        print("\n Please enter either a,b or c to view team stats \n")
        view_stats()
    else:

        if userInput.lower() == "a":
            team = teams[0]
        if userInput.lower() == "b":
            team = teams[1]

        if userInput.lower() == "c":
            team = teams[2]

        print("\n Team: {} Stats\n - - - - - - - - - - -".format(team))
        print("\n Total players: {}".format(len(balanced_team[team])))

        for player in balanced_team[team]:
            average_height.append(player['height'])
            if player['experience'] == True:
                experienced_player += 1
            if player['experience'] == False:
                inexperienced_player += 1

        print("\n Total experienced: {}".format(experienced_player))
        print("\n Total inexperienced: {}".format(inexperienced_player))
        print("\n Average height: {}".format(
            sum(average_height) / len(balanced_team[team])))

        for p in balanced_team[team]:
            team_player.append(p['name'])

            if len(p['guardians']) > 0:
                for g in p['guardians']:
                    guardian_names.append(g)

        print("\n Players on Team:\n  {}".format(
            just_player_name.join(team_player)))

        print("\n Guardians:\n  {}".format(
            just_player_name.join(guardian_names)))

        input("\n Press ENTER to continue...")

        view_stats()


def view_stats():
    print(
        "BASKETBALL TEAM STATS TOOL \n\n - - - - Menu - - - -\n\n Here are your choices: \n\n A) Display Team Stats\n B) Quit\n"
    )

    user_choice = input('Enter an option:  ')

    if user_choice.lower() == "a":
        print("\n A) {} \n B) {} \n C) {}".format(teams[0], teams[1],
                                                  teams[2]))
        option = input("Enter an option:  ")

        team_stats(option)

    else:
        print("GoodBye")


if __name__ == "__main__":
    view_stats()
