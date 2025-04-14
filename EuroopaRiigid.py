# --------------------------------------
# Praktiline töö 7.1 Работа со словарями "Euroopa riigid"
# --------------------------------------

from itertools import count
from SuperModule import *

# --------------------------------------

riik_pealinn = {}

TXT = "riigid_pealinnad.txt"

def init_dictionary():
    global riik_pealinn
    riik_pealinn = file_to_dict(TXT)
    #show_dict()

def file_to_dict(file: str):
    riik_pealinn = {}
    for line in read_file(file):
        key, value = line.strip().split("-")
        riik_pealinn[key] = value

    return riik_pealinn

def save_dict_to_file():
    lines = []
    for country, capital in riik_pealinn.items():
        lines.append(f"{country}-{capital}")

    write_file(TXT, lines)

def find_country_or_capital():
    input_name = get_input(str, "Sisestage riik or pealinn => ")
    print(find_value(input_name))

def find_value(name: str):
    name = name.strip().lower()
    for country, capital in riik_pealinn.items():
        if name == country.strip().lower():
            return f"{name.capitalize()} — Pealinn {capital}"
        elif name == capital.strip().lower():
            return f"{name.capitalize()} — Riik {country}"

    return "Tundmatu"

def add_new_entry():
    country = get_input(str, "Sisestage riik => ")
    capital = get_input(str, "Sisestage pealinn => ")
    riik_pealinn[country] = capital
    print("Kirje lisatud!")

def show_dict():
    for country, capital in riik_pealinn.items():
        print(f"{country}-{capital}")

def save_and_quit():
    save_dict_to_file()
    return True