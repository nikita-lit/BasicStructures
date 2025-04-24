
# --------------------------------------
# Praktiline töö 7.2 "Tarkvaraarendaja vastuvõtt"
# --------------------------------------

from Kusimustik import *
from SuperModule import *
import time

# --------------------------------------

def open_option(option: int):
    print("-------------------------------------")
    eval(options[option][1])
    print("-------------------------------------")

    time.sleep(1)
    open_menu()

options = [
    ["Alusta küsimustikku", "start_test()"],
    ["Lisa uus küsimus", "add_new_question()"],
    ["Kuva küsimused ja osalejad", "show_questions_users()"],
]

def open_menu():
    print()
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

init_test()
open_menu()