# --------------------------------------
# Tund 5
# --------------------------------------

from itertools import count
import math
import random

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

for i in range(10, 20, 1):
    print(f"i = {i} - math.sqrt(i) = {math.sqrt(i)}")

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

summa = 0
n_summa = 0

while True:
    try:
        N = int(input("Sisesta N => "))

        if N >= 1:
            for i in range(1, N+1):
                while True:
                    try:
                        arv = float(input(f"Sisesta {i}. arv => "))
                        break
                    except:
                        print("Kirjuta ainult numbrid")

                if arv < 0: 
                    n_summa += arv
                else:
                    summa += arv

            break
        else:
            print("Arv N peab olema rohkem kui 1")
    except Exception as e:
         print(f"ERROR: {e}")

print(f"Positiivne summa: {summa}")
print(f"Negatiivne summa: {n_summa}")

# --------------------------------------
# 7.

while True:
    try:
        A = int(input("Sisesta arv A => "))
        B = int(input("Sisesta arv B => "))
        K = int(input("Sisesta arv K => "))

        for i in range(A, B + 1):
            if i % K == 0:
                print(i)

        break
    except Exception as e:
         print(f"ERROR: {e}")

# --------------------------------------
# 8.

# --------------------------------------
# 15.

for j in range(10):
    for i in range(10):
        print(i, end=" ")
    print()
print()