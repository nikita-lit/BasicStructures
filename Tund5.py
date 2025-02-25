# --------------------------------------
# Tund 5
# --------------------------------------

from math import *
from random import *

# --------------------------------------
# 1.

# count = 0

# for i in range(15):
#     while True:
#         try:
#             arv = float(input(f"Sisesta {i+1}. arv => "))
#             break
#         except:
#             print("Kirjuta ainult numbrid")

#     if arv == int(arv):
#         count += 1

# print(f"Täisarvude kogus: {count}")

# --------------------------------------
# 2.

# while True:
#     try:
#         arv = int(input("Sisesta arv => "))
#         if arv > 1:
#             summa = 0

#             for i in range(1, arv):
#                 summa += i

#             print(f"Summa: {summa}")
#             break
#         else:
#             print("Arv ei saa olla negatiivne!")
#     except Exception as e:
#         print(f"ERROR: {e}")

# --------------------------------------
# 3.

# count = 0

# for i in range(8):
#     while True:
#         try:
#             arv = float(input(f"Sisesta {i+1}. arv => "))
#             break
#         except:
#             print("Kirjuta ainult numbrid")
#     if arv > 0:
#         count += arv

# print(count)

# --------------------------------------
# 4.

# for i in range(10, 20, 1):
#     print(f"i = {i} - math.sqrt(i) = {math.sqrt(i)}")

# --------------------------------------
# 5.

# summa = 0

# while True:
#     N = int(input("Sisesta N => "))

#     if N >= 1:
#         for i in range(1, N+1):
#             while True:
#                 try:
#                     arv = float(input(f"Sisesta {i}. arv => "))
#                     break
#                 except:
#                     print("Kirjuta ainult numbrid")

#             if arv < 0: 
#                 summa += arv

#         break
#     else:
#         print("Arv N peab olema rohkem kui 1")

# print(f"Summa: {summa}")

# --------------------------------------
# 6.

# summa = 0
# n_summa = 0

# while True:
#     try:
#         N = int(input("Sisesta N => "))

#         if N >= 1:
#             for i in range(1, N+1):
#                 while True:
#                     try:
#                         arv = float(input(f"Sisesta {i}. arv => "))
#                         break
#                     except:
#                         print("Kirjuta ainult numbrid")

#                 if arv < 0: 
#                     n_summa += arv
#                 else:
#                     summa += arv

#             break
#         else:
#             print("Arv N peab olema rohkem kui 1")
#     except Exception as e:
#          print(f"ERROR: {e}")

# print(f"Positiivne summa: {summa}")
# print(f"Negatiivne summa: {n_summa}")

# --------------------------------------
# 7.

# while True:
#     try:
#         A = int(input("Sisesta arv A => "))
#         B = int(input("Sisesta arv B => "))
#         K = int(input("Sisesta arv K => "))

#         for i in range(A, B + 1):
#             if i % K == 0:
#                 print(i)

#         break
#     except Exception as e:
#          print(f"ERROR: {e}")

# --------------------------------------
# 8.

# for i in range(1, 21):
#     cm = i * 2.5
#     print(f"{i} дюймы / {cm} см")

# --------------------------------------
# 9.

# while True:
#     try:
#         S = float(input("Sisesta sum => "))
#         N = int(input("Sisesta aastad => "))

#         for i in range(N):
#             S *= 1.03

#         break
#     except Exception as e:
#         print(f"ERROR: {e}")

# print(f"Vastus: {S:.2f}")

# --------------------------------------
# 10.

# while True:
#     try:
#         for i in range(1, 11):
#             arv1 = float(input("Sisesta esimine arv => "))
#             arv2 = float(input("Sisesta teise arv => "))

#             if arv1 > arv2:
#                 print(f"Suurem on {arv1}")
#             elif arv2 > arv1:
#                 print(f"Suurem on {arv2}")     
#         break
#     except Exception as e:
#         print(f"ERROR: {e}")

# --------------------------------------
# 11.

# try:
#     K = randint(1, 50)
#     print(f"Genereeritud number: {K}")

#     product = 1

#     for num in range(11, 100, 2):
#         if num % K == 0:
#             product *= num

#     if product > 1:
#         print(f"Kahekohaliste paaritute arvude korrutis, mis on jagatavad {K}: {product}")
#     else:
#         print(f"Ei ole kahekohalisi paarituid numbreid, mis on jagatavad {K}.")
# except Exception as e:
#     print(f"ERROR: {e}")

# --------------------------------------
# 12.

# try:
#     N = int(input("Sisestage heinategijate arv: "))
#     M = int(input("Sisestage esimese heinaküünla tööaeg (tundid): "))

#     tund = 0
#     for i in range(N):
#         tund += M + (i * 10 / 60)

#     print(f"Kogu meeskond töötas {round(tund)} tundi.")
# except Exception as e:
#     print(f"ERROR: {e}")

# --------------------------------------
# 13.

# arv = 0
# summa = 0

# for i in range(100, 1001):
#     if i % 7 == 0:
#         arv += 1
#         summa += i

# print(f"jagatavate arvude arv: {arv}")
# print(f"jagatavate arvude summa: {summa}")

# --------------------------------------
# 14.

# N = randint(1, 20)
# vastus = 1

# for i in range(1, N + 1):
#     vastus *= i

# print(f"Juhuslik number N: {N}")
# print(f"Numbrite 1 kuni {N}: {vastus}")

# --------------------------------------
# 15.

# for j in range(10):
#     for i in range(10):
#         print(i, end=" ")
#     print()
# print()

# --------------------------------------
# 16.

# for j in range(9):
#     for i in range(9):
#         if i == j:
#             print(j + 1, end=" ")
#         else:
#             print("0", end=" ")
#     print()

# --------------------------------------
# 17.

# for i in range(1, 10):
#     print(f"2*{i}={2 * i}")

# --------------------------------------
# 18.

# for num in range(20, 51):
#     if num % 3 == 0 and num % 5 != 0:
#         print(num)

# --------------------------------------
# 19.

# for num in range(35, 88):
#     if num % 7 in {1, 2, 5}:
#         print(num)

# --------------------------------------
# 20.

summa = 0

for num in range(1, 51):
    if num % 5 == 0 or num % 7 == 0:
        summa += num

print("Summa:", summa)