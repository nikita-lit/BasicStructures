from Tund7_Moodul import *

# arithmetic funktsiooni kasutamine

# a = float(input("Sisestage arv 1 => "))
# b = float(input("Sisestage arv 2 => "))
# t = str(input("Tehe => "))

# result = arithmetic(a, b, t)
# print(f"Vastus = {result}")

# year = int(input("Mis aasta tahad kontrollide? => "))
# vastus = is_year_leap(year) and f"{year} on liigaasta" or f"{year} ei ole liigaasta"
# print(vastus)

side = float(input("Sisestage külg => "))
result = square(side)

print(f"P = {result[0]} cm, S = {result[1]} cm2, D = {result[2]:.2f} cm")