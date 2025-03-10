# --------------------------------------
# Praktiline töö: Lihtsad prgrammid
# --------------------------------------

from datetime import *
from calendar import *
from math import *
from random import *

# --------------------------------------
# 1.
print("\n------- Ülesanne 1 -------\n")

täna = date.today()
formated_täna = str(täna)
print(f"Tere! Täna on {formated_täna}")

# 27/12/2022
formated_täna = täna.strftime("%d/%m/%Y")
print(f"Tere! Täna on {formated_täna}")

# December 27, 2022
formated_täna = täna.strftime("%B %d, %Y")
print(f"Tere! Täna on {formated_täna}")

# 12/27/22
formated_täna = täna.strftime("%m/%d/%y")
print(f"Tere! Täna on {formated_täna}")

# Dec-27-2022
formated_täna = täna.strftime("%b-%d-%Y")
print(f"Tere! Täna on {formated_täna}")

päev = täna.day
kuu = täna.month
aasta = täna.year

päevadekogus = monthrange(aasta, 1)[1]
print(f"Jaanuaris on {päevadekogus} päeva")

onjäänud = päevadekogus - päev
print(f"Jaanuaris on jäänud {onjäänud} päeva")

aastalõpuni = 365 - monthrange(aasta,1)[1]+onjäänud
print(f"Aasta lõpuni on jäänud {aastalõpuni} päeva")

# --------------------------------------
# 2.
print("\n------- Ülesanne 2 -------\n")

vastu = 3 + 8 / (4 - 2) * 4

# 1) (4 - 2) = 2
# 2) 8 / 2 = 4
# 3) 4 * 4 = 16
# 4) 3 + 16 = 19

# vastu = 19.0

print(f"3 + 8 / (4 - 2) * 4 = {vastu}")

# --------------------------------------
vastu2 = 3 + 8 / ((4 - 2) * 4)

# 1) (4 - 2) = 2
# 2) 2 * 4 = 8
# 3) 8 / 8 = 1
# 4) 3 + 1 = 4

# vastu2 = 4.0

print(f"3 + 8 / ((4 - 2) * 4) = {vastu2}")

# --------------------------------------
vastu3 = (3 + 8 / 4) - 2 * 4

# 1) 8 / 4 = 2
# 2) 3 + 2 = 5
# 3) 2 * 4 = 8
# 4) 5 - 8 = -3

# vastu3 = -3.0

print(f"(3 + 8 / 4) - 2 * 4 = {vastu3}")

# --------------------------------------
vastu4 = 3 + 8 / 4 - 2 * 4

# 1) 8 / 4 = 2
# 2) 2 * 4 = 8
# 3) 3 + 2 = 5
# 4) 5 - 8 = -3

# vastu4 = -3.0

print(f"3 + 8 / 4 - 2 * 4 = {vastu4}")

#Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd? - Sulud vastutavad toimingute järjekorra eest

# --------------------------------------
# 3.
print("\n------- Ülesanne 3 -------\n")

#R = randint(1, 100)

try:
    R = float(input("R: "))
except:
    print("VIGA! Sisesta ujukomaarvud! Raadius on random.\n")
    R = randint(1, 100)

print(f"Ringi raadius on {R}\n")

# Pindala - P
# Ümbermõõt - S

ruudu_pindala = (2 * R)**2
ruudu_ümbermõõt = 4 * (2*R)

ringi_pindala = pi * (R**2)
ringi_ümbermõõt = 2 * pi * R

print(f"Ruudu pindala = {round(ruudu_pindala, 2)}")
print(f"Ruudu ümbermõõt = {round(ruudu_ümbermõõt, 2)}")
print(f"Ringi pindala = {round(ringi_pindala, 2)}")
print(f"Ringi ümbermõõt = {round(ringi_ümbermõõt, 2)}")

# --------------------------------------
# 4.
print("\n------- Ülesanne 4 -------\n")

maa_raadius_km = 6378
maa_raadius_sm = maa_raadius_km * 100000

mündi_läbimõõt_sm = 2.575 # d

# --------------------------------------

maa_ümbermõõt_sm = 2 * pi * maa_raadius_sm # P
muntide_arv = maa_ümbermõõt_sm / mündi_läbimõõt_sm

print(f"Maa ümbermõõt ekvaatori kohal on {round(maa_ümbermõõt_sm, 2)} SM või {round(maa_ümbermõõt_sm / 100000, 2)} KM")
print(f"Meil on vaja {int(muntide_arv):,d} mündi.")
print(f"Meil on vaja {int(muntide_arv*2):,d} euro.")

# --------------------------------------
# 5.
print("\n------- Ülesanne 5 -------\n")

sõna1 = "kill-koll ".capitalize()
sõna2 = "killadi-koll ".capitalize()

print(sõna1 * 2 + sõna2 + sõna1 * 2 + sõna2 + sõna1 * 3 +"\n"+sõna1)

# --------------------------------------
# 6.
print("\n------- Ülesanne 6 -------\n")

print("Rong see sõitis tsuhh tsuhh tsuhh,".upper())
print("piilupart oli rongijuht.".upper())
print("Rattad tegid rat tat taa,".upper())
print("rat tat taa ja tat tat taa.".upper())
print("Aga seal rongi peal,".upper())
print("kas sa tead, kes olid seal?\n".upper())

print("Rong see sõitis tuut tuut tuut,".upper())
print("piilupart oli rongijuht.".upper())
print("Rattad tegid kill koll koll,".upper())
print("kill koll koll ja kill koll kill.".upper())

# --------------------------------------
# 7.
print("\n------- Ülesanne 7 -------\n")

try:
    a = float(input("A: "))
    b = float(input("B: "))

    if a > 0 and b > 0:
        print("Pindala ja ümbermõõdu arvutamine: ")
        S = a*b
        P = (a+b)*2
        print(f"S = {S}, P = {P}")
    else:
        print("Arvud peaval suurem kui 0 olla!")

except:
    print("VIGA! Vale sisendandmed.")

# --------------------------------------
# 8.
print("\n------- Ülesanne 8 -------\n")

try:
    liitrid = float(input("Sisesta tangitud kütuse liitrid: "))
    kilomeetrid = float(input("Sisesta läbitud kilomeetrid: "))

    if liitrid >= 0 and kilomeetrid > 0:
        kütusekulu = (liitrid / kilomeetrid) * 100

        print(f"Keskmine kütusekulu 100 km kohta on {kütusekulu}")
    else:
        print("VIGA! Vale sisendandmed.")
except:
    print("VIGA! Vale sisendandmed.")

# --------------------------------------
# 9.
print("\n------- Ülesanne 9 -------\n")

kiirus = 29.9

try:
    M = int(input("Sisesta aeg minutites: "))

    if M >= 0:
        aeg = M / 60 # tundiseks
        kaugus = kiirus * aeg

        print(f"Kiirus on {kiirus}")
        print(f"Kaugus {M} minutiga on {round(kaugus, 2)} km.")
    else:
        print("VIGA! Vale sisendandmed.")

except:
    print("VIGA! Vale sisendandmed.")

# --------------------------------------
# 10.
print("\n------- Ülesanne 10 -------\n")

try:
    M = int(input("Sisesta aeg minutites: "))
    if M >= 0:
        tund = M // 60
        minutites = M % 60

        print(f"Minutites tunniseks ja minutiseks on {tund}:{minutites:02}")
except:
    print("VIGA! Vale sisendandmed.")