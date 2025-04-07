
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
    max_salary = max(palgad)
    print(f"Suurim palk on {max_salary}")
    count = palgad.count(max_salary)
    index = palgad.index(max_salary)
    for i in range(count):
        index = palgad.index(max_salary, index)
        print(f"Saab kätte {inimesed[index]}")
        index += 1

def sorting(inimesed: list, palgad: list):
    while True:
        v = input("Vali märk: > (kasvav) või < (kahanev) => ")
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