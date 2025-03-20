from Tund7_Moodul import *

# # --------------------------------------
# # 1. arithmetic funktsiooni kasutamine

# a = float(input("sisestage arv 1 => "))
# b = float(input("sisestage arv 2 => "))
# t = str(input("tehe => "))

# result = arithmetic(a, b, t)
# print(f"vastus = {result}")

# # --------------------------------------
# # 2.

# year = int(input("mis aasta tahad kontrollide? => "))
# vastus = is_year_leap(year) and f"{year} on liigaasta" or f"{year} ei ole liigaasta"
# print(vastus)

# # --------------------------------------
# # 3.

# side = float(input("sisestage külg => "))
# result = square(side)

# print(f"p = {result[0]} cm, s = {result[1]} cm2, d = {result[2]:.2f} cm")

# # --------------------------------------
# # 4.

# month = int(input("Sisestage kuu number => "))

# if month > 12:
#     print("Vale kuu!")
# elif month <= 0:
#     print("Vale kuu!")
# else:
#     print(f"See on {season(month)}")

# # --------------------------------------
# # 5.

# summa = float(input("Sisestage summa => "))
# years = int(input("Sisestage aastad => "))
# print(f"Summa aastal {years} on {bank(summa, years):.2f}")

# # --------------------------------------
# # 6.

# number = int(input("Sisestage number => "))
# print(is_prime(number) and f"{number} on algarv" or f"{number} ei ole algarv")

# # --------------------------------------
# # 7.

# day = int(input("Sisestage päev => "))
# month = int(input("Sisestage kuu => "))
# year = int(input("Sisestage aasta => "))

# print(date(day, month, year) and "Kuupäev on olemas" or "Kuupäev ei ole olemas")

# --------------------------------------
# 8.

cipher = XOR_cipher("test", "key")
print(cipher)

uncipher = XOR_uncipher(cipher, "key")
print(uncipher)