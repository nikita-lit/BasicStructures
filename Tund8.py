# --------------------------------------
# Mäng "Kivi-paber-käärid"
# --------------------------------------

from Tund8_Module import *
from SuperModule import *
import time

# --------------------------------------

current_option = 0

TXT = "Tund8.txt"

users = [
    ["guest", " ", " ", ["guest"]],
    ["admin", "0000", " ", ["admin", "user"]]
]
current_user = 1

# --------------------------------------
def load_users():
    users = []
    lines = read_file(TXT)
    if len(lines) <= 0:
        reset_users()
        return

    for line in lines:
        user_key, user_data = line.strip().split("=")
        user_key = int(user_key)
        data_parts = user_data.split(",")
        user = []
        
        for key, data in enumerate(data_parts):
            if key == USER_RIGHTS:
                user.insert(key, data.split(";"))
            else:
                user.insert(key, data)

        users.insert(user_key, user)

    return users

def save_users():
    time.sleep(1.5)
    lines = []
    for user_key, user_data in enumerate(users):
        datas = []

        for key, data in enumerate(user_data):
            if key == USER_RIGHTS:
                data_joined = ";".join(data)
                datas.append(data_joined)
            else:
                datas.append(data)

        joined_data = ",".join(datas)
        lines.append(f"{user_key}={joined_data}")

    write_file(TXT, lines)
    print("Kasutajad on salvestatud!")

def reset_users():
    global users
    users = [
        ["guest", " ", " ", ["guest"]],
        ["admin", "0000", " ", ["admin", "user"]]
    ]
    print("Kasutajad on lähtestatud!")
    save_users()
    time.sleep(2)
    open_menu()

def send_verif_code(subject: str, user_email: str):
    code = random.randint(10000, 99999)
    send_email(subject, user_email, f"Teie kood: {code}")
    print("Kood on saadetud.")

    while True:
        input_code = get_input(int, "Sisestage kood => ")
        if input_code == code:
            print("Kood on õige!")
            break
        else:
            print("Vale kood!")
            choice = get_input(str, "Kas proovite uuesti? (jah/ei) => ")
            if choice != "jah" and choice != "1":
                return False

    return True

# --------------------------------------
def get_user(name: str) -> any:
    for user in users:
        if user[USER_NAME] == name:
            return user

    return False

# --------------------------------------
def ask_menu():
    print()
    choice = get_input(str, "Kas soovite minna tagasi menüüsse? (jah/ei) => ")
    if choice == "jah" or choice == "1":
        open_menu()

# --------------------------------------
def registration():
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

    while True:
        user_email = get_input(str, "Sisetage email => ").lower()
        if not "@gmail.com" in user_email:
            print("Toetatud on ainult gmail.com!")
            ask_menu()
        else:
            for user in users:
                if user[USER_EMAIL] == user_email:
                    print("E-post on juba kasutusel")
                    ask_menu()
                    break
            else:
                break

    print("Kinnitage oma e-posti aadress. Kood on saadetud.")
    if not send_verif_code("E-posti kinnitus.", user_email):
        time.sleep(2)
        open_menu()
        return

    user = [user_name, user_password, user_email, ["user"]]
    users.append(user)
    global current_user
    current_user = users.index(user)

    print(f"Teie parool: {user_password}")
    print(f"Kasutaja {user_name} on edukalt registreeritud.")
    save_users()
    time.sleep(2)
    open_menu()

# --------------------------------------
def login():
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

                time.sleep(2)
                open_menu()
                return
        else:
            print("Vale nimi või parool!")

        time.sleep(1)
        ask_menu()

# --------------------------------------
def logout():
    choice = get_input(str, "Kas te soovite oma kontolt välja logida? (jah/ei) => ")
    if choice == "jah" or choice == "1":
        global current_user
        current_user = 0

    time.sleep(2)
    open_menu()

# --------------------------------------
def ask_new_password() -> str:
    while True:
        new_password = get_input(str, "Sisestage uus parool => ")
        if is_password_valid(new_password):
            break

    return new_password

# --------------------------------------
def change_account_details():
    while True:
        choice = get_input(str,"Mida soovite oma parooli või nime muuta? (parool/nimi) => ").lower()

        if choice == "parool":
            new_password = ask_new_password()
            users[current_user][USER_PSW] = new_password
            print("Parool on muutunud.")
            print(f"Teie uus parool on {users[current_user][USER_PSW]}.")
            save_users()
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
                    save_users()
                    break
            break
        else:
            print("Vale valik!")

    time.sleep(2)
    open_menu()
    
# --------------------------------------
def recover_password():
    while True:
        user_email = get_input(str, "Sisestage selle kasutaja e-posti, kelle parooli soovite taastada => ").lower()
        if not "@gmail.com" in user_email:
            print("Toetatud on ainult gmail.com!")
            ask_menu()
        else:
            break

    if not send_verif_code("Parooli taastamine.", user_email):
        time.sleep(2)
        open_menu()
        return

    user = None

    for key, u in enumerate(users):
        if u[USER_EMAIL].lower() == user_email:
            user = key

    if user:
        new_password = ask_new_password()
        users[user][USER_PSW] = new_password
        print("Parool on muutunud.")
        print(f"{users[user][USER_NAME]} uus parool on {users[user][USER_PSW]}.")
        save_users()
    else:
        print("Vale kasutajanimi!")

    time.sleep(2)
    open_menu()
    
# --------------------------------------
def show_users():
    for key, user in enumerate(users):
        print(f"{key+1}.\n  Nimi: {user[USER_NAME]}\n   Parool: {user[USER_PSW]}\n   E-post: {user[USER_EMAIL]} \n   Õigused: {user[USER_RIGHTS]}")

    time.sleep(2)
    open_menu()

# --------------------------------------
def open_option(option: int):
    if not option >= 0 or not option < len(options):
        open_menu()
        return

    for right in users[current_user][USER_RIGHTS]:
        if right in options[option][2]:
            print("-------------------------------------")
            print(options[option][0])
            print("-------------------------------------")
            eval(options[option][1])
            break
    else:
        print("Teil ei ole õigusi.")
        time.sleep(2)
        open_menu()

# --------------------------------------
options = [
    ["Registreerimine", "registration()", ["user", "admin", "guest"]],
    ["Autoriseerimine", "login()", ["user", "admin", "guest"]],
    ["Unustanud parooli taastamine", "recover_password()", ["user", "admin", "guest"]],
    ["Väljalogimine", "logout()", ["user", "admin"]],
    ["Nime või parooli muutmine", "change_account_details()", ["user", "admin"]],
    ["Näita kasutajad", "show_users()", ["admin"]],
    ["Lähtestada kasutajad", "reset_users()", ["admin"]]
]

def open_menu():
    global users
    users = load_users()

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