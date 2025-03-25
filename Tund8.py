# --------------------------------------
# Mäng "Kivi-paber-käärid"
# --------------------------------------

from Tund8_Module import *
import time

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

def get_user(name):
    for user in users:
        if user[USER_NAME] == name:
            return user

    return False

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
        if user_name.lower() == "guest":
            print("Ei saa külaliseks registreeruda.")
        elif is_user_name_valid(user_name):
            break

    user_password = "12345"

    choice = get_input(str, "Kas sa soovid automaatset parooli genereerimist? (jah/ei) => ")
    if choice == "jah" or choice == "1":
        user_password = generate_password()
    else:
        while True:
            user_password = get_input(str, "Sisestage parool => ")
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
        if user_name.lower() == "guest":
            print("Ei saa külalisena sisse logida.")
            break

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

    choice = get_input(str, "Kas te soovite oma kontolt välja logida? (jah/ei) => ")
    if choice == "jah" or choice == "1":
        global current_user
        current_user = 0

    time.sleep(2)
    open_menu()

def ask_new_password():
    while True:
        new_password = get_input(str, "Sisestage uus parool => ")
        if is_password_valid(new_password):
            break

    return new_password

def change_account_details():
    print(options[CHANGE_DETAILS][0])

    while True:
        choice = get_input(str,"Mida soovite oma parooli või nime muuta? (parool/nimi) => ").lower()

        if choice == "parool":
            new_password = ask_new_password()
            users[current_user][USER_PSW] = new_password
            print("Parool on muutunud.")
            print(f"Teie uus parool on {users[current_user][USER_PSW]}.")
            break
        elif choice == "nimi":
            if is_guest(users[current_user]):
                print("Külalise nime ei saa muuta.")
                break
            elif is_admin(users[current_user]):
                print("Admin nime ei saa muuta.")
                break

            while True:
                new_user_name = get_input(str, "Sisestage uus nimi => ")
                if is_user_name_valid(new_user_name):
                    users[current_user][USER_NAME] = new_user_name
                    print("Nimi on muutunud.")
                    print(f"Teie uus nimi on {users[current_user][USER_NAME]}.")
                    break
            break
        else:
            print("Vale valik!")

    time.sleep(2)
    open_menu()
    
def recover_password():
    print(options[RECOVER][0])

    while True:
        user_name = get_input(str, "Sisestage kasutajanimi, mille parool tuleb taastada => ")
        if user_name.lower() == "guest":
            print("Külalise parooli ei saa taastada.")
        else:
            break
        
    user = get_user(user_name)
    if user:
        new_password = ask_new_password()
        user[USER_PSW] = new_password
        print("Parool on muutunud.")
        print(f"{user[USER_NAME]} uus parool on {user[USER_PSW]}.")
    else:
        print("Vale kasutajanimi!")

    time.sleep(2)
    open_menu()
    
def show_users():
    print(options[SHOW_USERS][0])
    for key, user in enumerate(users):
        print(f"{key+1}.\n  Nimi: {user[USER_NAME]}\n   Parool: {user[USER_PSW]}\n   Õigused: {user[USER_RIGHTS]}")

    time.sleep(2)
    open_menu()

def open_option(option: int):
    if not option >= 0 or not option < len(options):
        open_menu()
        return

    for right in users[current_user][USER_RIGHTS]:
        if right in options[option][2]:
            eval(options[option][1])
            break
    else:
        print("Teil ei ole õigusi.")
        time.sleep(2)
        open_menu()
        return

options = [
    ["Registreerimine", "registration()", ["user", "admin", "guest"]],
    ["Autoriseerimine", "login()", ["user", "admin", "guest"]],
    ["Unustanud parooli taastamine", "recover_password()", ["user", "admin", "guest"]],
    ["Väljalogimine", "logout()", ["user", "admin"]],
    ["Nime või parooli muutmine", "change_account_details()", ["user", "admin"]],
    ["Näita kasutajaid", "show_users()", ["admin"]]
]

def open_menu():
    print()
    print("-------------------------------------")
    print(f"Praegune kasutaja on [{users[current_user][USER_NAME]}]")
    print("-------------------------------------")
    print()

    for key, option in enumerate(options):
        for right in users[current_user][USER_RIGHTS]:
            if right in option[2]:
                print(f"{key+1}. {option[0]}")
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

open_menu()