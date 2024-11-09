import time
import random

# Se creează lista pentru echipe
team_1 = []
team_2 = []

# Se pregătește variabilele unde se introduc numele jucătorilor
players = []

def run_program():
    input_the_players()
    genereaza_echipele()

def input_the_players():
    global players, teams_with_x_players
    print("Salut, sunt un generator de echipe")
    time.sleep(1)
    print("Alege câți jucători într-o echipă sunt")
    time.sleep(1)
    print("a) 3 Jucători per echipă")
    print("b) 4 Jucători per echipă")
    print("c) 5 Jucători per echipă")
    print("d) 6 Jucători per echipă")
    print("e) 7 Jucători per echipă")
    print("f) 8 Jucători per echipă")
    print("G) 9 Jucători per echipă")
    print("H) 10 Jucători per echipă")
    time.sleep(1)
    teams_with_x_players = str(input("Alege litera care trebuie: ")).upper()
    
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
        print("Opțiune invalidă!")
        return
    
    for i in range(1, num_players + 1):
        player_name = input(f"Jucătorul {i}: ")
        players.append(player_name)

def genereaza_echipele():
    global team_1, team_2, players, teams_with_x_players
    if teams_with_x_players in ["A", "B", "C", "D", "E", "F", "G"]:
        random.shuffle(players)
        half = len(players) // 2
        team_1 = players[:half]
        team_2 = players[half:]
        print(team_1)
        print(team_2)
        
        print("Echipa 1: " + ',' .join(team_1))
        print("Echipa 2: " + ',' .join(team_2))
    else:
        print("Echipele nu au putut fi generate din cauza unei opțiuni invalide.")

run_program()