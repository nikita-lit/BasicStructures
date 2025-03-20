# --------------------------------------
# Mäng "Kivi-paber-käärid"
# --------------------------------------

from Tund8_Module import *

# --------------------------------------

REG = 0
LOGIN = 1
LOGOUT = 2
CHANGE_DETAILS = 3
RECOVER = 4

current_option = 0

def registration():
    print(options[REG][0])

def login():
    print(options[LOGIN][0])

def logout():
    print(options[LOGOUT][0])

def change_account_details():
    print(options[CHANGE_DETAILS][0])
    
def recover_password():
    print(options[RECOVER][0])

def open_option(option: int):
    if option >= 0 and option < len(options):
        eval(options[option][1])

options = [
    ["Registreerimine", "registration()"],
    ["Autoriseerimine", "login()"],
    ["Väljalogimine", "logout()"],
    ["Nime või parooli muutmine", "change_account_details()"],
    ["Unustanud parooli taastamine", "recover_password()"],
]

while True:
    for key, value in enumerate(options):
        print(f"{key+1}. {value[0]}")

    print()
    while True:
        choice = get_input(int, "Sisestage valik number => ")
        if choice and choice > 0 and choice <= len(options):
            current_option = (choice-1)
            break
        else:
            print("Vale valik!")

    open_option(current_option)
    break