# --------------------------------------
# Tund 1 "Funktsioonide print(),input(), float(), int() kasutamine"
# --------------------------------------

from math import *
from random import *

# --------------------------------------
# 1.

print("Tere, maailm!")
nimi = input("Nimi: ").capitalize()
print("Tere, maailm! Tervitan sind", nimi+".")
vanus = int(input("Vanus: "))
print("Tere, maailm! Tervitan sind", nimi+"!", "Sa oled", str(vanus), "aastat vana.")

# --------------------------------------
# 2.

# a) vanus = 18  - int
# b) eesnimi = "Jaak" - str
# c) pikkus = 16.5 - float
# d) kas_käib_koolis = True - bool

# Mis võimalus veel peale True oleks viimast muutujat väärtustada? - False

# Kuidas võiks nende muutujate väärtusi koodis kontrollida? - type()

# Kirjuta kood tüüpide kontrollimiseks.

vanus = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True

print("vanus", vanus, "on", type(vanus))
print("eesnimi", eesnimi, "on", type(eesnimi))
print("pikkus", pikkus, "on", type(pikkus))
print("kas_käib_koolis", kas_käib_koolis, "on", type(kas_käib_koolis))

# --------------------------------------
# 3.

kommide_arv = randint(10, 100)
print("Laua peal on", kommide_arv)

print("Mitu kommi sa soovid laualt ära võtta?")
mitu = int(input("Mitu tahad süüja? "))

print("Laua peal on jäänud", kommide_arv - mitu)

# --------------------------------------
# 4.

pikkus = float(input("Puu ümbermõõdu pikkus: "))
d = round( pikkus / pi, 3 )
print("Puu läbimõõdu =", d)

# --------------------------------------
# 5.

N = float(input("Esimene külg: "))
M = float(input("Teine külg: "))

diagonaal = round( sqrt(N**2 + M**2), 3 )

print("Diagonaali pikkus on =", diagonaal)

# --------------------------------------
# 6.

# Leidke järgnevast näiteprogrammist semantiline viga:
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = aeg / teepikkus <--------- Kiiruse arvutamise valem on vale

# print("Sinu kiirus oli " + str(kiirus) + " km/h")

aeg = float(input("Mitu tundi kulus sõiduks? "))
teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
kiirus = teepikkus / aeg  #<--------- Õige variant

print("Sinu kiirus oli " + str(kiirus) + " km/h")

# --------------------------------------
# 7.

a = 2
b = 4
c = 7
d = 5
e = 6

aritmeetilise_keskmise = (a + b + c + d + e) / 5

print("Aritmeetilise keskmise =", aritmeetilise_keskmise)

# --------------------------------------
# 8.

print("   @..@\n  (----)\n ( \__/ )\n ^^ \"\" ^^  ")

# --------------------------------------
# 9.

a = int(input("Külg a: "))
b = int(input("Külg b: "))
c = int(input("Külg c: "))

P = a + b + c

print("Ümbermõõdu: ", P)

# --------------------------------------
# 10.

pitsa_hind = 12.90
jootraha_protsent = 10 / 100
jootraha = pitsa_hind * jootraha_protsent
kogu_summa = pitsa_hind + jootraha

print("Pitsa kogu summa = ", kogu_summa)

inimesi = int(input("Kui palju inimesi on? "))
print("Igaüks peab maksma:", kogu_summa / inimesi,"€")