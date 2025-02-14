# --------------------------------------
# Iseseisev töö "Vigade otsing -1"
# --------------------------------------

from math import * # import oli vale

# --------------------------------------
try:
    print("Ruudu karakteristikud")
    a = float(input("Sisesta ruudu külje pikkus => ")) # input() peab olema konverteeritud float'iks
    S= a ** 2
    print(f"Ruudu pindala: {S}")
    P = 4 * a
    print(f"Ruudu ümbermõõt: {P}")
    di = a * sqrt(2) # "sqr(2)" ei ole korrektne, õige on "sqrt(2)"

    print("Ruudu diagonaal", round(di,2))
except Exception as e:
    print(f"ERROR: {e}")

print()

try:
    print("Ristküliku karakteristikud")

    b = float(input("Sisesta ristküliku 1. külje pikkus => ")) # input() peab olema konverteeritud float'iks
    c = float(input("Sisesta ristküliku 2. külje pikkus => ")) # input() peab olema konverteeritud float'iks
    S = b * c

    print("Ristküliku pindala", S) # Sõnumis olid puudu jutumärgid ja vale süntaks
    P = 2 * (b + c)  # Puudu oli korrutamise operaator
    print("Ristküliku ümbermõõt", P)
    di = sqrt( b ** 2 + c ** 2 ) # Korrektne valem diagonaali jaoks on "b**2 + c**2"

    print("Ristküliku diagonaal", round(di)) # Sulgude puudavad lõpus
except Exception as e:
    print(f"ERROR: {e}")

print()

try:
    print("Ringi karakteristikud")

    r = float(input("Sisesta ringi raadiusi pikkus => ")) # input() peab olema konverteeritud float'iks
    d = 2 * r # Puudu oli korrutamise operaator
    print("Ringi läbimõõt", d)

    S = pi * r ** 2 # pi() -> pi ("pi" ei ole funktsiooni); Valem pindala jaoks oli vale, õige on "pi * r**2"
    print("Ringi pindala", round(S))

    C = 2 * pi * r # Valem ringjoone pikkuse jaoks oli vale, õige on "2 * pi * r"'""
    print("Ringjoone pikkus", round(C)) # Sulgude puudavad lõpus
except Exception as e:
    print(f"ERROR: {e}")