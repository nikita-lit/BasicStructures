
def get_inimene_index_by_name(inimesed: list, palgad: list, input_text: str) -> int:
    name = get_input(str, input_text)
    print()
    if name in inimesed:
        indixes = []
        for key, value in enumerate(inimesed):
            if value == name:
                indixes.append(key)

        if len(indixes) > 1:
            print(f"Leiti mitu inimest nimega {name}. Palun valige, keda muuta:")
            for i, index in enumerate(indixes):
                print(f"{i + 1}. Inimene: {inimesed[index]} Palk: {palgad[index]}")

            while True:
                choice_index = get_input(int, f"Valige arv (1-{len(indixes)}) => ")-1
                if 0 <= choice_index and choice_index < len(indixes):
                    return indixes[choice_index]
                else:
                    print("Vale valik!")
        else:
            return indixes[0]

    return -1

def get_input(data_type: type, text: str) -> any:
    """
    Tagastab määratud andmetüübiga sisendi andmed.
    :param (tüüp) data_type: andmetüüp.
    :param (str) tekst: kasutajale kuvatav tekst.
    """

    try:
        data = data_type(input(text))
    except:
        return False

    return data

def add_data(inimesed: list, palgad: list):
    """
    Lisada mitu inimest ja nende palgad.
    """

    while True:
        count = get_input(int, "Kui palju inimesi ja nende palka te soovite lisada? => ")
        if count > 0:
            break
        else:
            print("Vale arv!")
    
    for i in range(count):
        print(f"{i+1}.")
        while True:
            inimine_name = get_input(str, "Sisestage inimine nimi => ")
            if inimine_name.isnumeric():
                print("Nimi ei saa koosneda ainult numbritest.")
            else:
                break        
            
        while True:
            inimine_salary = get_input(float, "Sisestage inimine palk => ")
            if not inimine_salary or inimine_salary < 0:
                print("Vale palk!")
            else:
                break

        inimesed.append(inimine_name)
        palgad.append(inimine_salary)

def delete_data(inimesed: list, palgad: list):
    """
    Isiku ja tema palga kustutada(nimi sisestab kasutaja)
    """

    inimine_name = get_input(str, "Sisestage inimine nimi => ")
    count = inimesed.count(inimine_name)
    if count > 0:
        for i in range(count):
            index = inimesed.index(inimine_name)
            inimesed.pop(index)
            palgad.pop(index)

        print("Andmed on kustutatud!")
    else:
        print("Andmed puuduvad!")

def biggest_salary(inimesed: list, palgad: list):
    """
    Leida kes saab kätte suurim palk.
    """

    max_salary = max(palgad)
    print(f"Suurim palk on {max_salary}")
    count = palgad.count(max_salary)
    index = palgad.index(max_salary)
    for i in range(count):
        index = palgad.index(max_salary, index)
        print(f"Saab kätte {inimesed[index]}")
        index += 1

def sorting(inimesed: list, palgad: list):
    """
    Järjestada palgad kasvavas ja kahanevas järjekorras koos nimedega.
    """

    while True:
        v = get_input(str, "Vali märk: > (kasvav) või < (kahanev) => ")
        if not v in [">", "<"]:
            print("Vale märk!")
        else:
            break

    for n in range(0, len(inimesed)):
        for m in range(n, len(inimesed)):
            if eval( str(palgad[n])+v+str(palgad[m])):
                palgad[n], palgad[m] = palgad[m], palgad[n]
                inimesed[n], inimesed[m] = inimesed[m], inimesed[n]

def equal_salaries(inimesed: list, palgad: list):
    """
    Teada saada, kes saavad võrdset palka, leida, kui palju neid on ja kuvada nende andmed ekraanile.
    """

    hulk = set(palgad)
    print(hulk)
    for salary in hulk:
        count = palgad.count(salary)
        if count > 1:
            print(f"Palk {salary}")
            index = palgad.index(salary)
            for j in range(count):
                index = palgad.index(salary, index)
                print(f"Saab kätte {inimesed[index]}")
                index += 1

def average_salary(inimesed: list, palgad: list):
    """
    Keskmine palk ja selle saaja nimi/nimed.
    """

    avg = sum(palgad) / len(palgad)
    print(f"Keskmine palk on {avg}")

def change_data(inimesed: list, palgad: list):
    """
    Funktsioon andmete redigeerimiseks. Kasutaja valib, mida muuta: nime või palka.
    """

    selected_index = get_inimene_index_by_name(inimesed, palgad, "Sisestage nimi, mida muuta => ")

    if selected_index != -1:
        while True:
            choice = get_input(int, "Kas muuta nime või palka? (0/1) => ")
            if choice == 0:
                while True:
                    new_name = get_input(str, "Sisestage uus nimi => ")
                    if new_name.isnumeric():
                        print("Nimi ei saa koosneda ainult numbritest.")
                    else:
                        break 

                inimesed[selected_index] = new_name
                break
            elif choice == 1:
                while True:
                    new_salary = get_input(float, "Sisestage uus palk => ")
                    if not new_salary or new_salary < 0:
                        print("Vale palk!")
                    else:
                        break

                palgad[selected_index] = new_salary
                break
            else:
                print("Vale valik!")
    else:
        print("Isikut ei leitud!")

def find_inimesed_by_first_char(inimesed: list, palgad: list):
    """
    Leia nimed, mis algavad antud tähega.
    """

    char = get_input(str, "Sisestage täht, mille järgi otsida => ").lower()
    for key, value in enumerate(inimesed):
        lower_value = value.lower()
        if lower_value.startswith(char):
            print(f"Inimene: {value} Palk: {palgad[key]}")

def salary_increase(inimesed: list, palgad: list):
    """
    Arvutab töötaja palga pärast T aastat 5% aastase tõusuga.
    """

    selected_index = get_inimene_index_by_name(inimesed, palgad, "Sisestage nimi => ")
    if selected_index != -1:
        years = get_input(int, "Kui mitu aastat palka tõsta? => ")
        
        future_salary = palgad[selected_index] * (1.05 ** years)
        print(f"{inimesed[selected_index]} uus palk pärast {years} aastat on {future_salary:.2f} eurot.")
    else:
        print("Isikut ei leitud!")