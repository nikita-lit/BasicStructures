# --------------------------------------
# Töö 5.4 Praktiline töö "Palgad"
# --------------------------------------

from PraktilineTooPalgad_Module import *
import time

# --------------------------------------


palgad = [1200,2500,750,395,1200]
inimesed = ["A","B","C","D","E"]

def open_option(option: int):
    if not option >= 0 or not option < len(options):
        open_menu()
        return

    eval(options[option][1])

    time.sleep(2)
    open_menu()

options = [
    ["Lisa andmed", "add_data(inimesed, palgad)"],
    ["Kustuta andmed", "delete_data(inimesed, palgad)"],
    ["Suurim palk", "biggest_salary(inimesed, palgad)"],
    ["Sorteerimine", "sorting(inimesed, palgad)"],
]

def open_menu():
    print()
    print("Andmed:")

    for key, value in enumerate(inimesed):
        print(f"Inimene: {value}\n  Palk: {palgad[key]}")

    print()

    for key, option in enumerate(options):
        print(f"{key+1}. {option[0]}")

    print()
    while True:
        choice = get_input(int, "Sisestage valik number => ")
        if choice and choice > 0 and choice <= len(options):
            current_option = (choice-1)
            break
        else:
            print("Vale valik!")

    print()
    open_option(current_option)

open_menu()