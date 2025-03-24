# --------------------------------------
# Mäng "Kivi-paber-käärid"
# --------------------------------------

import glob
from Tund8_Module import *
import time
import os

# --------------------------------------

REG = 0
LOGIN = 1
LOGOUT = 2
CHANGE_DETAILS = 3
RECOVER = 4
SHOW_USERS = 5

current_option = 0

users = [
    ["guest", "", ["guest"]],
    ["admin", "0000", ["admin", "user"]]
]
current_user = 1

def ask_menu():
    print()
    choice = get_input(str, "Kas soovite minna tagasi menüüsse? (jah/ei) => ")
    if choice == "jah" or choice == "1":
        open_menu()

def registration():
    print("-------------------------------------")
    print(options[REG][0])
    print("-------------------------------------")
    
    while True:
        user_name = get_input(str, "Sisestage nimi => ")
        if is_user_name_valid(user_name):
            break

    user_password = "12345"

    choice = input("Kas sa soovid automaatset parooli genereerimist? (jah/ei) => ")
    if choice == "jah" or choice == "1":
        user_password = generate_password()
    else:
        while True:
            user_password = input("Sisestage parool => ")
            if is_password_valid(user_password):
                break

    user = [user_name, user_password, ["user"]]
    users.append(user)
    global current_user
    current_user = users.index(user)

    print(f"Teie parool: {user_password}")
    print(f"Kasutaja {user_name} on edukalt registreeritud.")
    time.sleep(2)
    open_menu()

def login():
    print("-------------------------------------")
    print(options[LOGIN][0])
    print("-------------------------------------")

    logedin = False

    while True:
        user_name = get_input(str, "Sisestage kasutaja nimi => ")
        user_password = get_input(str, "Sisestage kasutaja parool => ")

        for key, user in enumerate(users):
            if user[USER_NAME] == user_name and user[USER_PSW] == user_password:
                print(f"Tere tulemast, {user[USER_NAME]}!")
                global current_user
                current_user = key
                logedin = True
                break
        else:
            print("Vale nimi või parool!")

        if logedin:
            break

        time.sleep(1)
        ask_menu()

    time.sleep(2)
    open_menu()

def logout():
    print(options[LOGOUT][0])

    choice = input("Kas te soovite oma kontolt välja logida? (jah/ei) => ")
    if choice == "jah" or choice == "1":
        global current_user
        current_user = 0

    time.sleep(2)
    open_menu()

def change_account_details():
    print(options[CHANGE_DETAILS][0])
    
def recover_password():
    print(options[RECOVER][0])
    
def show_users():
    print(options[SHOW_USERS][0])
    for key, user in enumerate(users):
        print(f"{key+1}. {user[USER_NAME]}")

    time.sleep(2)
    open_menu()

def open_option(option: int):
    if option >= 0 and option < len(options):
        eval(options[option][1])

options = [
    ["Registreerimine", "registration()", ["user", "admin", "guest"]],
    ["Autoriseerimine", "login()", ["user", "admin", "guest"]],
    ["Väljalogimine", "logout()", ["user", "admin"]],
    ["Nime või parooli muutmine", "change_account_details()", ["user", "admin"]],
    ["Unustanud parooli taastamine", "recover_password()", ["user", "admin", "guest"]],
    ["Näita kasutajaid", "show_users()", ["admin"]]
]

def open_menu():
    print()
    print("-------------------------------------")
    print(f"Praegune kasutaja on [{users[current_user][USER_NAME]}]")
    print("-------------------------------------")
    print()

    while True:
        num = 0
        for key, option in enumerate(options):
            for right in users[current_user][USER_RIGHTS]:
                if right in option[2]:
                    print(f"{num+1}. {option[0]}")
                    num += 1
                    break

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
        break

open_menu()