# --------------------------------------
# Töö 5.4 Praktiline töö "Palgad"
# --------------------------------------

from PraktilineTooPalgad_Module import *
import time

# --------------------------------------


palgad = [1200,2500,750,395,1200,10000,1500]
inimesed = ["A","B","C","D","E","F","G"]

def open_option(option: int):
    if not option >= 0 or not option < len(options):
        open_menu()
        return

    print("-------------------------------------")
    eval(options[option][1])
    print("-------------------------------------")

    time.sleep(2)
    open_menu()

options = [
    ["Lisa andmed", "add_data(inimesed, palgad)"],
    ["Kustuta andmed", "delete_data(inimesed, palgad)"],
    ["Suurim palk", "biggest_salary(inimesed, palgad)"],
    ["Sorteerimine", "sorting(inimesed, palgad)"],
    ["Võrdsed palgad", "equal_salaries(inimesed, palgad)"],

    ["Keskmine palk", "average_salary(inimesed, palgad)"],
    ["Muuta nimi või palk", "change_data(inimesed, palgad)"],
    ["Leia nimed, mis algavad antud tähega", "find_inimesed_by_first_char(inimesed, palgad)"],
    ["Palga tõus", "salary_increase(inimesed, palgad)"],
    ["Tulemaks", "income_tax(inimesed, palgad)"],
]

def open_menu():
    print()
    print("-------------------------------------")
    print("Andmed:")
    print("-------------------------------------")

    for key, value in enumerate(inimesed):
        print(f"Inimene: {value}\n  Palk: {palgad[key]}")

    print("-------------------------------------")
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