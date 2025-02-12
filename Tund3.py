# --------------------------------------
# Tund 3
# --------------------------------------

import random

# --------------------------------------
# Näidis 1

number = random.randint(0, 10)
print(number)

if number > 5:
    print("--------------------------------------")
    print(f"Arv {number} suurem kui 5")
    print("--------------------------------------")

# --------------------------------------
# Näidis 2

number = random.randint(-10, 10)
print(number)

if number > 0:
    print(f"Arv {number} on positiivne")
else:
    print(f"Arv {number} on negatiivne")

if number > 0:
    print(f"Arv {number} on positiivne")
elif number == 0:
    print(f"Arv {number} on 0")
else:
    print(f"Arv {number} on negatiivne")