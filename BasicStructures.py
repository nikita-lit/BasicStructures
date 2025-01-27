# -------------------------------------

#prints tere tulemast twice
print("Tere tulemast! 1", "Tere tulemast! 2", end="...\n", sep="----")

# ------------ Andmetüübid ------------
# täisarv - int
# ujukomaarv - float
# sõne - str
# tõeväärtused - bool
# -------------------------------------
# Astendamine ( ** )

a = 5
aste = 2

tulemus = a ** aste
print(a, "**", aste, "=", tulemus)

# -------------------------------------
# Korrutamine ( * )

arv1 = int(input("Esimene korrutaja: "))
arv2 = int(input("Teine korrutaja: "))
tulemus = arv1 * arv2

print(arv1, "*", arv2, "=", tulemus)

# -------------------------------------
# Jagamine ( / )

arv1 = int(input("Esimene arv: "))
arv2 = int(input("Jagaja: "))
tulemus = arv1 / arv2

print(arv1, "/", arv2, "=", tulemus)
print(type(tulemus))

# -------------------------------------
# Jagamisjääk ( % )

arv1 = int(input("Esimene arv: "))
arv2 = int(input("Teine arv: "))
tulemus = arv1 % arv2

print(arv1, "%", arv2, "=", tulemus)

# -------------------------------------
# Liitmine / Lahutamine ( + / - )

arv1 = int(input("Esimene arv: "))
arv2 = int(input("Teine arv: "))

tulemus = arv1 + arv2
print(arv1, "+", arv2, "=", tulemus)

tulemus = arv1 - arv2
print(arv1, "-", arv2, "=", tulemus)

# -------------------------------------
# Jagamise täisarvulise osa leidmine ( // )

arv1 = int(input("Esimene arv: "))
arv2 = int(input("Teine arv: "))

tulemus = arv1 // arv2
print(arv1, "//", arv2, "=", tulemus)

# -------------------------------------
# Tekstide liitmine / teksti kordamine ( + / * )

sõne1 = input("Esimene sõne: ")
sõne2 = input("Teine sõne: ")

tulemus = sõne1 + sõne2

print(sõne1, "+", sõne2, "=", tulemus)

sõne = input("Sõne: ")
arv1 = int(input("Korrutaja: "))

tulemus = sõne * arv1