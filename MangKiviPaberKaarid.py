# --------------------------------------
# Mäng "Kivi-paber-käärid"
# --------------------------------------

import random
import os
import time

# --------------------------------------

choices = ["kivi", "käärid", "paber"]

PLY_NAME = 0
PLY_SCORE = 1
PLY_CHOICE = 2

players = []

for i in range(2):
    player = [f"Player {i+1}", 0, ""]
    player[PLY_NAME] = input(f"Sisestage Player {i+1} nimi või 'robot' => ").title()
    player[PLY_SCORE] = 0
    player[PLY_CHOICE] = ""
    players.append(player)

rounds = int(input("Kui palju voorusid tahad mängida? "))

for round_num in range(0, rounds):
    print()
    print(f"Voor {round_num+1}. algab!")

    for i in range(len(players)):
        while True:
            time.sleep(0.5)
            if players[i][PLY_NAME].lower() == "robot":
                choice = random.choice(choices)
            else:
                choice = input(f"Player {players[i][PLY_NAME]} vali {choices} => ").lower()

            if choice in choices:
                players[i][PLY_CHOICE] = choice
                print(f"Player {players[i][PLY_NAME]} valis: {players[i][PLY_CHOICE]}")
                break
            else:
                os.system("cls")
                print("Vale valik!")

    print()
    for i in range(len(players)):
        player = players[i]
        print(f"Player {player[PLY_NAME]} valis: {player[PLY_CHOICE]}")

print()
print("Mängu lõpp!")
points = []

for i in range(len(players)):
    player = players[i]
    print(f"Player {player[PLY_NAME]} punktid: {player[PLY_SCORE]}")
    points.append(player[PLY_SCORE])

max_points = max(points)
winner_index = points.index(max_points)
draw = False

for i in range(len(players)):
    if players[winner_index][PLY_SCORE] == players[i][PLY_SCORE]:
        draw = True
        print("Viik!")
        break

if not draw:
    print(f"{players[winner_index][PLY_NAME]} on võitja!")
