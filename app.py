import copy
import string
from constants import PLAYERS
from constants import TEAMS

players_copy = copy.deepcopy(PLAYERS)
team_copy = copy.deepcopy(TEAMS)
clean_players = []
clean_teams = []


def clean_data():
    for player in players_copy:
        fixed_player = {}
        fixed_player["name"] = player["name"]
        fixed_player["guardians"] = player["guardians"].split(" and ")
        if player["experience"] == "YES":
            fixed_player["experience"] = True

        else:
            fixed_player["experience"] = False

        fixed_player["Height"] = int(player["height"].split(" ")[0])
        clean_players.append(fixed_player)


def experience_sorter():
    experienced_players = []
    inexperienced_players = []
    for fixed_player in clean_players:
        if fixed_player["experience"] == True:
            experienced_players.append(fixed_player)

        else:
            inexperienced_players.append(fixed_player)

    experienced_players_team = int(len(experienced_players) / len(team_copy))
    inexperienced_players_team = int(
        len(inexperienced_players) / len(team_copy))

    for team in team_copy:
        roster = []

        for fixed_player in range(0, experienced_players_team):
            roster.append(experienced_players.pop(0))
        for fixed_player in range(0, inexperienced_players_team):
            roster.append(inexperienced_players.pop(0))

        team_info = {
            "Team Name": team,
            "Team Roster": roster,
            "Total Players": len(roster)
        }

        clean_teams.append(team_info)


def start():
    print("BASKETBALL TEAM STATS TOOL\n")
    print("What would you like to do?")
    print("\nA) Display Team Stats")
    print("B) Quit")
    while True:
        first_choice = input("\nPick an option: ")
        print()
        if first_choice.lower() != "a" and first_choice.lower() != "b":
            print("Please Just enter A or B")
            continue
        elif first_choice.lower() == "b":
            quit()
        elif first_choice.lower() == "a":
            break

    for i, team in zip(string.ascii_uppercase, clean_teams):  # Changes the key to letters
        print(i + ")", team["Team Name"])

    while True:
        team_selection = input(
            "\nPick the letter of the team you would like to view.").upper()
        if team_selection in string.ascii_uppercase[:len(clean_teams)]:
            team_index = string.ascii_uppercase.index(team_selection)
            selected_team = clean_teams[team_index]

            print("\nTeam:", selected_team["Team Name"], "Stats")
            print("--------------------")
            print("Total players:", selected_team["Total Players"])

            total_experienced = sum(player["experience"]
                                    for player in selected_team["Team Roster"])
            total_inexperienced = selected_team["Total Players"] - \
                total_experienced
            print("Total experienced:", total_experienced)
            print("Total inexperienced:", total_inexperienced)

            total_height = sum(player["Height"]
                for player in selected_team["Team Roster"])
            average_height = float(
                total_height / selected_team["Total Players"])
            print("Average height:", average_height)

            print("\nPlayers on Team:")
            for player in selected_team["Team Roster"]:
                print("  " + player["name"], end=", ")
            print()

            print("\nGuardians:")
            for player in selected_team["Team Roster"]:
                for guardian in player["guardians"]:
                    print("  " + guardian, end=", ")
            print()
            break
        else:
            print("Please just enter the first letter.")
            continue
    restart = input("\nPress enter to return to the main menu")
    if restart != None:
        start()


if __name__ == "__main__":
    clean_data()
    experience_sorter()
    start()
