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

for i in range(3):
    player = [f"Player {i+1}", 0, ""]
    if i == 0:
        player[PLY_NAME] = input(f"Sisestage Player {i+1} nimi => ").title()
    else:
        player[PLY_NAME] = input(f"Sisestage Player {i+1} nimi või 'robot' => ").title()

    if i > 0:
        if player[PLY_NAME] == players[i-1][PLY_NAME]:
            player[PLY_NAME] = player[PLY_NAME] + str(i)

    player[PLY_SCORE] = 0
    player[PLY_CHOICE] = ""
    players.append(player)

while True:
    try:
        rounds = int(input("Kui palju voorusid tahad mängida? "))
        break
    except Exception as e:
        print(f"ERROR: {e}")

for round_num in range(0, rounds):
    print()
    print(f"Voor {round_num+1}. algab!")

    for i in range(len(players)):
        while True:
            time.sleep(0.5)
            if "robot" in players[i][PLY_NAME].lower() and i != 0:
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
        for j in range(i + 1, len(players)):
            choice1 = players[i][PLY_CHOICE]
            choice2 = players[j][PLY_CHOICE]
            if choice1 == choice2:
                print(f"Viik vahel {players[i][PLY_NAME]} ja {players[j][PLY_NAME]}")
            elif (choice1 == "kivi" and choice2 == "käärid") or \
                 (choice1 == "käärid" and choice2 == "paber") or \
                 (choice1 == "paber" and choice2 == "kivi"):
                print(f"{players[i][PLY_NAME]} võitis {players[j][PLY_NAME]}")
                players[i][PLY_SCORE] += 1
            else:
                print(f"{players[j][PLY_NAME]} võitis {players[i][PLY_NAME]}")
                players[j][PLY_SCORE] += 1


print()
print("Mängu lõpp!")
points = []

for i in range(len(players)):
    player = players[i]
    print(f"Player {player[PLY_NAME]} punktid: {player[PLY_SCORE]}")
    points.append(player[PLY_SCORE])

max_points = max(points)

winner_indixes = []
for i in range(len(players)):
    if players[i][PLY_SCORE] == max_points:
        winner_indixes.append(i)

if len(winner_indixes) == 1:
    print(f"{players[winner_indixes[0]] [PLY_NAME]} on võitja!")
else:
    print("Viik!")