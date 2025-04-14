# --------------------------------------
# Praktiline töö 7.1 Работа со словарями "Euroopa riigid"
# --------------------------------------

from EuroopaRiigid import *
from SuperModule import *
import time

# --------------------------------------

def open_option(option: int):
    if not option >= 0 or not option < len(options):
        open_menu()
        return

    print("-------------------------------------")
    result = eval(options[option][1])
    if result:
        return
    print("-------------------------------------")

    time.sleep(1)
    open_menu()

options = [
    ["Otsige pealinna või riiki", "find_country_or_capital()"],
    ["Lisage uus kirje", "add_new_entry()"],
    ["Parandage kirje", ""],
    ["Teadmiste kontroll", ""],
    ["Salvesta ja välju", "save_and_quit()"],
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