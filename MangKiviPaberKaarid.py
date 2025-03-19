# --------------------------------------
# Mäng "Kivi-paber-käärid"
# --------------------------------------

import random
import os
import time

# --------------------------------------

CHOICES = ["kivi", "käärid", "paber"]

player1 = input("Sisestage Player 1 nimi => ").title()
player1_score = 0

player2 = input("Sisestage Player 2 nimi või 'robot' => ").title()
player2_score = 0

while True:
    try:
        rounds = int(input("Kui palju voorusid tahad mängida? "))
        break
    except Exception as e:
        print(f"ERROR: {e}")

for round_num in range(rounds):
    print()
    print(f"Voor {round_num+1}. algab!")

    for i in range(2):
        while True:
            time.sleep(0.5)
            if "robot" in player2.lower() and i != 0:
                choice = random.choice(CHOICES)
            else:
                if i == 0:
                    choice = input(f"Player 1 [{player1}] vali {CHOICES} => ").lower()
                else:
                    choice = input(f"Player 2 [{player2}] vali {CHOICES} => ").lower()

            if choice in CHOICES:
                if i == 0:
                    player1_choice = choice
                    print(f"Player 1 [{player1}] valis: {player1_choice}")
                else:
                    player2_choice = choice
                    print(f"Player 2 [{player2}] valis: {player2_choice}")

                print()
                break
            else:
                os.system("cls")
                print("Vale valik!")

    if player1_choice == player2_choice:
        print(f"Viik vahel {player1} ja {player2}")
    elif (player1_choice == "kivi" and player2_choice == "käärid") or \
        (player1_choice == "käärid" and player2_choice == "paber") or \
        (player1_choice == "paber" and player2_choice == "kivi"):
        print(f"{player1} võitis {player2}")
        player1_score += 1
    else:
        player2_score += 1

time.sleep(1)
print()
print("Mängu lõpp!")

print(f"Player 1 [{player1}] punktid: {player1_score}")
print(f"Player 2 [{player2}] punktid: {player2_score}")

if player1_score > player2_score:
    print(f"{player1} on võitja!")
elif player1_score < player2_score:
    print(f"{player2} on võitja!")
else:
    print("Viik!")

print()