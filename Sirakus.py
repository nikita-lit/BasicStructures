from time import sleep


print("------------------------ Arvude mäng ------------------------")
print()

# --------------------------------------
while True:
    try:
        a = abs(int(input("Sisesta täisarv => ")))
        if a == 0:
            print("Nulliga on mõttetu töö")
        else:
            break
    except ValueError:
         print("See ei ole täisarv")

print()
# --------------------------------------
print("----------- Loendame, mitu on paaris ja mitu paaritu arv -----------")
print()

c = b = a
paaris = 0 # четные
paaritu = 0 # нечетные

while b > 0:
    if b % 2 == 0:
        paaris += 1
    else:
        paaritu += 1

    b = b // 10
    
print("Paaris arvude kogus:", paaris)
print("Paaritu on:", paaritu)
print()

# --------------------------------------
print("----------- *Ümberpöörame* sisestatud arv -----------")
print()

b = 0

while a > 0:
    number = a % 10
    a = a // 10
    b = b * 10
    b += number

print("*Ümberpööratud* arv", b)
print()

# --------------------------------------
print("----------- Tõestame teoreem -----------")
print()

while c > 0:
    if c % 2 == 0:
        print(f"{c} - Paaris arv, Jagame 2.")
        c = c / 2
    else:
        print(f"{c} - Paaritu arv. Korrutame 3, lisame 1 ja jagame 2.")
        c = (3 * c + 1) / 2

    if c == 1:
        print(f"{c} - Teoreem on tõestatud")
        break

print()