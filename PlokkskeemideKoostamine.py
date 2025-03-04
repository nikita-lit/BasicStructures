# --------------------------------------

import time

# --------------------------------------
# V2
# --------------------------------------
# 1. Määrake ja väljastage kasutaja poolt sisestatud N numbri maksimum.
max_number = float("-inf")

try:
    N = int(input("Sisestage N => "))

    for i in range(N):
        number = int(input(f"Sisestage arv {i+1}. => "))
 
        if number > max_number:
            max_number = number

    print(f"Max number on: {max_number}")
except Exception as e:
    print(f"ERROR: {e}")

# --------------------------------------
# V2
# --------------------------------------
# 2. Kirjutage programm, mis küsib täisarvu ja väljastab mis tahes selle väärtuse, välja arvatud13. Kui antud arv on13, siis trükitakse selle asemel arv 77.

try:
    number = int(input("Sisestage arv => "))

    if number == 13:
        number = 77
    
    print(f"Teie arv on {number}")
except Exception as e:
    print(f"ERROR: {e}")

# --------------------------------------
# 3. Pärast treeningutega alustamist jooksis sportlane esimesel päeval 10 km. Iga päev suurendas ta oma päevanormi 10% võrra eelmise päeva normist. Kui palju on kogu distants, mille sportlane 7 päeva jooksul läbib?

print()
D = float(input("Mitu kilomeetrit sa täna jooksid? => "))
protsent = float(input("Kui palju protsenti te iga päev distantsi suurendate? => "))

for i in range(7):
    D = D * ((protsent / 100) + 1)

print(f"Seitsme päeva pärast jooksed: {round(D, 2)}")

# --------------------------------------
# 4. On olemas riidetükk pikkusega M meetrit. Sellest lõigatakse järjestikku erineva pikkusega tükke. Kõik andmed riide kasutamise kohta sisestatakse arvutisse. Arvutis peaks ilmuma teade, et materjali ei ole piisavalt, kui soovitakse kasutada olemasolevast pikemat kangatükki.

print()
try:
    while True:
        M = float(input("Sisestage pikkus => "))
        if M > 0:
            X = float(input("Sisestage tükkide arv => "))
            if X > 0:
                if M > X:
                    print("Materjali on piisavalt!")
                else:
                    print("Materjali ei ole piisavalt!")
                break
            else:
                print("Vale tükkide arv!")
        else:
            print("Vale pikkus!")
except Exception as e:
    print(f"ERROR: {e}")

# --------------------------------------
# V5
# --------------------------------------
# 3. Rühm 20 õpilast sooritas ühe sessiooni jooksul kolm eksamit. Tehke algoritm eksamivormi täitmiseks.

print()
for õ in range(20):
    print(f"Soritab eksamit {õ+1}")
    for e in range(3):
        print(f"{e+1}. eksam")

# --------------------------------------
# V4
# --------------------------------------
# 2. Koostage programmi plokkskeem, et arvutada ainult negatiivsete P antud arvude summa.

print()
vastus = 0

try:
    P = int(input("Mitu korda kordame? => "))

    while True:
        arv = float(input("Sisestage arv => "))
        if arv < 0:
            vastus += arv

        P -= 1

        if P <= 0:
            print(f"Summa on {vastus}")
            break

except Exception as e:
    print(f"ERROR: {e}")
    
print()
vastus = 0

try:
    P = int(input("Mitu korda kordame? => "))

    for i in range(P):
        arv = float(input("Sisestage arv => "))
        if arv < 0:
            vastus += arv

    print(f"Summa on {vastus}")

except Exception as e:
    print(f"ERROR: {e}")

# --------------------------------------
# V1
# --------------------------------------
# 4. Koostage plokkskeem kotlette praadiva roboti jaoks.

print()
panni_maht = 6
aeg = 0.5

try:
    while True:
        kotlette_kogu_number = int(input("Sisestage kotlette arv => "))
        if kotlette_kogu_number > 0:
            break
        else:
            print("Vale kotlette arv!")

    lahenemine = kotlette_kogu_number // panni_maht
    jaak = kotlette_kogu_number % panni_maht
    if jaak > 0:
        lahenemine += 1

    print(f"Lahenemine arv on {lahenemine}")
    print()

    for i in range(lahenemine):
        print("----------------------------------")
        print(f"{i+1}. Lahenemine")
        if i == (lahenemine-1) and jaak > 0:
            kotlette_number = jaak
        else:
            kotlette_number = panni_maht

        print(f"Panni peal on {kotlette_number} kotlet.")

        print()
        print("Praeme esimene pool")
        time.sleep(aeg)
        print("Ümberpöörame")
        print("Praeme teine pool")
        time.sleep(aeg)

        print("----------------------------------")
        print(f"Valmis!")
        print("----------------------------------")
        print()

except Exception as e:
    print(f"ERROR: {e}")