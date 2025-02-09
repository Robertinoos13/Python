import time
import random

# Creating the variables that will store the players' names to result on 2 teams
team_1 = []
team_2 = []

# Preparing the variables where the players' names are entered
players = []

def run_program():
    input_the_players()
    generate_the_teams()

def input_the_players():
    global players, teams_with_x_players
    print("Hello, im a teams generator")
    time.sleep(1)
    print("Choose how many players per team you want:")
    time.sleep(1)
    print("a) 3 players per team")
    print("b) 4 players per team")
    print("c) 5 players per team")
    print("d) 6 players per team")
    print("e) 7 players per team")
    print("f) 8 players per team")
    print("G) 9 players per team")
    print("H) 10 players per team")
    time.sleep(1)
    teams_with_x_players = str(input("Select the right letter: ")).upper()
    
    if teams_with_x_players == "A":
        num_players = 6
    elif teams_with_x_players == "B":
        num_players = 8
    elif teams_with_x_players == "C":
        num_players = 10
    elif teams_with_x_players == "D":
        num_players = 12
    elif teams_with_x_players == "E":
        num_players = 14
    elif teams_with_x_players == "F":
        num_players = 16
    elif teams_with_x_players == "G":
        num_players = 18
    elif teams_with_x_players == "H":
        num_players = 20
    else:
        print("Invalid Option!")
        return
    
    for i in range(1, num_players + 1):
        player_name = input(f"Player {i}: ")
        players.append(player_name)

def generate_the_teams():
    global team_1, team_2, players, teams_with_x_players
    if teams_with_x_players in ["A", "B", "C", "D", "E", "F", "G", "H"]:
        random.shuffle(players) # Reorganize the players' names randomly
        half = len(players) // 2 # Divide operation to get the half of the players' names (so it will always be an integer with //) 
        team_1 = players[:half]
        team_2 = players[half:]
        print(team_1)
        print(team_2)
        
        print("Team 1: " + ',' .join(team_1))
        print("Team 2: " + ',' .join(team_2))
    else:
        print("The teams could not be generated because of an invalid option")

run_program()