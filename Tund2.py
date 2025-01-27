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
mündi_läbimõõt_mm = 25

mundi_läbimõõt_km = mündi_läbimõõt_mm / 1000

maa_ümbermõõt_km = 2 * pi * maa_raadius_km
muntide_arv = maa_ümbermõõt_km / mundi_läbimõõt_km

print(f"Maa ümbermõõt ekvaatori kohal on: {round(maa_ümbermõõt_km, 2)} km")
print(f"2-euroseid münte on vaja: {round(muntide_arv, 2)} tükki")

# --------------------------------------
# 5.
print("\n------- Ülesanne 5 -------\n")

sõna1 = "kill-koll ".capitalize()
sõna2 = "killadi-koll ".capitalize()

print(sõna1 * 2 + sõna2 + sõna1 * 2 + sõna2 + sõna1 * 4)

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
    pikkus = float(input("Sisesta ristküliku pikkus: "))
    laius = float(input("Sisesta ristküliku laius: "))

    ümbermõõt = 2 * (pikkus + laius)
    pindala = pikkus * laius

    print(f"Ristküliku ümbermõõt on {round(ümbermõõt, 2)}")
    print(f"Ristküliku pindala on {round(pindala, 2)}")
except:
    print("VIGA! Vale sisse andmed.")

# --------------------------------------
# 8.
print("\n------- Ülesanne 8 -------\n")

try:
    liitrid = float(input("Sisesta tangitud kütuse liitrid: "))
    kilomeetrid = float(input("Sisesta läbitud kilomeetrid: "))

    kütusekulu = (liitrid / kilomeetrid) * 100
    print(f"Keskmine kütusekulu 100 km kohta on {kütusekulu}")
except:
    print("VIGA! Vale sisse andmed.")

# --------------------------------------
# 9.
print("\n------- Ülesanne 9 -------\n")

kiirus = 29.9

try:
    M = int(input("Sisesta aeg minutites: "))

    aeg = M / 60 # tundiseks
    kaugus = kiirus * aeg

    print(f"Kaugus {M} minutiga on {round(kaugus, 2)} km.")
except:
    print("VIGA! Vale sisse andmed.")

# --------------------------------------
# 10.
print("\n------- Ülesanne 10 -------\n")

try:
    M = int(input("Sisesta aeg minutites: "))
    tund = M // 60
    minutites = M % 60

    print(f"Minutites tunniseks ja minutiseks on {tund}:{minutites}")
except:
    print("VIGA! Vale sisse andmed.")