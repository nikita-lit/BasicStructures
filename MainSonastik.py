# --------------------------------------
# Praktiline töö 6.2 "Sõnastik" kome keelne
# --------------------------------------

from Sonastik import *
from SuperModule import *
import time

# --------------------------------------

def open_option(option: int):
    if not option >= 0 or not option < len(options):
        open_menu()
        return

    print("-------------------------------------")
    eval(options[option][1])
    print("-------------------------------------")

    time.sleep(1)
    open_menu()

options = [
    ["Tõlge", "translate()"],
    ["Lisa uus sõna", "add_word_to_dict()"],
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

init_dictionary()
open_menu()