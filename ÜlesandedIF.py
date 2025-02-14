# --------------------------------------
# Ülesanded: Tingimuslik operaator IF
# --------------------------------------

from random import *

# --------------------------------------
# 1. Juku

# print("Kino")

# nimi = input("Mis on sinu nimi? ")

# if nimi.isupper() and nimi.lower() == "juku":
#     print("Lähme kinno")

#     try:
#         vanus = int(input("Kui vana sa oled? "))

#         if vanus < 0 or vanus > 100:
#             pilet = "!!!"
#         elif vanus < 6:
#             pilet = "Tasuta"
#         elif vanus <= 14:
#             pilet = "Lastepilet"
#         elif vanus <= 65:
#             pilet = "Täospilet"
#         elif vanus <= 100:
#             pilet = "Sooduspilet"

#         print(pilet)
#     except Exception as e:
#         print(f"ERROR {e}")
# else:
#     print("Ma olen hõivatud")

# --------------------------------------
# 2. Pinginaabrid

# nimi1 = input("Sisesta esimese inimese nimi: ")
# nimi2 = input("Sisesta teise inimese nimi: ")

# if nimi1.isalpha() and nimi2.isalpha():
#     nimi1 = nimi1.lower()
#     nimi2 = nimi2.lower()

#     if (nimi1 == "maksim" and nimi2 == "nikita") or (nimi1 == "nikita" and nimi2 == "maksim"):
#         print("Nad olevad pinginaaber!")
#     else:
#         print("Nad ei ole pinginaaber!")

# else:
#     print("ERROR")

# --------------------------------------
# 3. Remont

# try:
#     pikkus = float(input("Sisesta toa pikkus: "))
#     laius = float(input("Sisesta toa laius: "))
#     põranda_pindala = pikkus * laius
#     print(f"Põranda pindala on {põranda_pindala} ruutmeetrit.")

#     remont = input("Kas sa soovid põrandat vahetada? jah/ei: ").lower()

#     if remont == "jah":
#         hind = float(input("Kui palju maksab ruutmeeter põranda vahetus? "))
#         koguhind = hind * põranda_pindala
#         print(f"Põranda vahetamise hind on {koguhind} eurot.")
# except Exception as e:
#     print(f"ERROR: {e}")

# --------------------------------------
# 4. Allahindus

# try:
#     alghind = float(input("Sisesta toote hind: "))

#     if alghind > 700:
#         print(f"Toote hind pärast 30% soodustust on {(alghind - (alghind * 0.3))} eurot.")
#     else:
#         print("Toode ei ole soodustuse jaoks piisavalt kallis.")
# except Exception as e:
#     print(f"ERROR: {e}")

# --------------------------------------
# 5. Temperatuur

# try:
#     temperatuur = float(input("Sisesta toa temperatuur: "))

#     if temperatuur > 18:
#         print("Temperatuur on üle 18 kraadi, see on sobiv toasoojus talvel.")
#     else:
#         print("Temperatuur on madalam kui 18 kraadi, võib olla liiga külm.")
# except Exception as e:
#     print(f"ERROR: {e}")

# --------------------------------------
# 6. Pikkus

# try:
#     pikkus = float(input("Sisesta oma pikkus (cm): "))

#     if pikkus < 165:
#         print("Sa oled lühike.")
#     elif pikkus < 180:
#         print("Sa oled keskmine.")
#     else:
#         print("Sa oled pikk.")
# except Exception as e:
#     print(f"ERROR: {e}")

# --------------------------------------
# 7. Pikkus ja sugu

# try:
#     pikkus = float(input("Sisesta oma pikkus (cm): "))
#     sugu = input("Sisesta oma sugu mees/naine: ").lower()

#     if sugu == "mees":
#         if pikkus < 165:
#             print("Sa oled lühike.")
#         elif pikkus < 180:
#             print("Sa oled keskmine.")
#         else:
#             print("Sa oled pikk.")
#     elif sugu == "naine":
#         if pikkus < 160:
#             print("Sa oled lühike.")
#         elif pikkus < 175:
#             print("Sa oled keskmine.")
#         else:
#             print("Sa oled pikk.")
#     else:
#         print("Vale sugu.")
# except Exception as e:
#     print(f"ERROR: {e}")

# --------------------------------------
# 8. Poes

# try:
#     piim_arv = 0
#     saia_arv = 0
#     leiba_arv = 0

#     piim_hind = randint(130, 260)/100
#     saia_hind = randint(80, 180)/100
#     leiba_hind = randint(70, 150)/100

#     piim = input(f"Kas sa soovid osta piima? ({piim_hind:.2f} euro) jah/ei: ")
#     if piim == "jah":
#         piim_arv = int(input("Kui palju sa soovid osta piima? "))

#     saia = input(f"Kas sa soovid osta saia? ({saia_hind:.2f} euro) jah/ei: ").lower()
#     if saia == "jah":
#         saia_arv = int(input("Kui palju sa soovid osta saia? "))
        
#     leiba = input(f"Kas sa soovid osta leiba? ({leiba_hind:.2f} euro) jah/ei: ").lower()
#     if leiba == "jah":
#         leiba_arv = int(input("Kui palju sa soovid osta leiba? "))

#     if piim_arv > 0 or saia_arv > 0 or leiba_arv > 0:
#         print()
#         print("# --------------------------------------")
#         print("Tšekk:")
#         piim_kogu_hind = piim_arv*piim_hind
#         saia_kogu_hind = saia_arv*saia_hind
#         leiba_kogu_hind = leiba_arv*leiba_hind

#         if piim_arv > 0:
#             print(f"{piim_arv} x Piim - {piim_kogu_hind:.2f} euro")
#         if saia_arv > 0:
#             print(f"{saia_arv} x Saia - {saia_kogu_hind:.2f} euro")        
#         if leiba_arv > 0:
#             print(f"{leiba_arv} x Leiba - {leiba_kogu_hind:.2f} euro")

#         summa = piim_kogu_hind + leiba_kogu_hind + saia_kogu_hind
#         print("# --------------------------------------")
#         print(f"Summa: {summa:.2f}")
#         print("# --------------------------------------")

# except Exception as e:
#     print(f"ERROR: {e}")

# --------------------------------------
# 9. Ruut

# try:
#     a = float(input("Sisesta ruudu esimene külg: "))
#     b = float(input("Sisesta ruudu teine külg: "))
#     c = float(input("Sisesta ruudu kolmas külg: "))
#     d = float(input("Sisesta ruudu neljas külg: "))

#     if a == b == c == d:
#         print("See on ruut!")
#     else:
#         print("See ei ole ruut!")
# except Exception as e:
#     print(f"ERROR: {e}")

# --------------------------------------
# 10. Matemaatika

# try:
#     arv1 = float(input("Sisesta esimene arv: "))
#     arv2 = float(input("Sisesta teine arv: "))
#     operation = input("Sisesta tehe +, -, *, /: ")

#     if operation == "+":
#         print(f"Tulemus: {arv1 + arv2}")
#     elif operation == "-":
#         print(f"Tulemus: {arv1 - arv2}")
#     elif operation == "*":
#         print(f"Tulemus: {arv1 * arv2}")
#     elif operation == "/":
#         if arv2 == 0:
#             print("Arv ei saa olla 0!")
#         else:
#             print(f"Tulemus: {arv1 / arv2}")
#     else:
#         print("Vale tehe!")

# except Exception as e:
#     print(f"ERROR: {e}")

# --------------------------------------
# 10. Juubel

try:
    vanus = int(input("Sisesta vanus: "))

    if vanus % 10:
        print("See vanus ei ole juubel.")
    else:
        print("See vanus on juubel!")

except Exception as e:
    print(f"ERROR: {e}")