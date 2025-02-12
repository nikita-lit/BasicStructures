print("Kino")

nimi = input("Mis on sinu nimi? ")

if nimi.isupper() and nimi.lower() == "juku":
    print("Lähme kinno")

    try:
        vanus = int(input("Kui vana sa oled? "))

        if vanus < 0 or vanus > 100:
            pilet = "!!!"
        elif vanus < 6:
            pilet = "Tasuta"
        elif vanus >= 14:
            pilet = "Lastepilet"
        elif vanus >= 65:
            pilet = "Täospilet"
        elif vanus <= 100:
            pilet = "Sooduspilet"

        print(pilet)
    except Exception as e:
        print(f"ERROR {e}")
else:
    print("Ma olen hõivatud")