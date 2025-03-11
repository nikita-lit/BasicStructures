funcs_list = [
    "swapcase()",
    "join()",
    "partition()",
    "zfill()",
    "strip()",
    "test()",
    "test()",
    "test()",
    "test()",
    "test()",
]

while True:
    print("---------------------------------------------")
    print("Millist funktsiooni te soovite näha?")
    print("---------------------------------------------")

    for i in range(len(funcs_list)):
        print(f"{i+1}. {funcs_list[i]}")

    print("0. välja")
    print()

    print("---------------------------------------------")

    while True:
        try:
            choice = int(input("Sisestage arv => "))
            break
        except Exception as e:
            print(f"ERROR: {e}")

    print("---------------------------------------------")
    print()

    try:
        if choice == 0:
            break
        elif choice == 1:
            word = str(input("Sisestage sõna => "))
            print(f"Teie sõna: {word}")
            print(f"Sõna pärast swapcase(): {word.swapcase()}")
        elif choice == 2:
            words = []

            for i in range(4):
                word = str(input(f"Sisestage {i+1}. sõna => "))
                words.append(word)

            separator = str(input("Sisestage separator sõna => "))
            result = separator.join(words)
            print(result)   
        elif choice == 3:
            sentence = str(input("Sisestage lause => "))
            separator = str(input("Sisestage separator sõna => "))
            result = sentence.partition(separator)
            print(result)
        elif choice == 4:
            word = str(input("Sisestage sõna => "))
            length = int(input("Sisestage pikkus => "))
            result = word.zfill(length)
            print(result)
        elif choice == 5:
            word = str(input("Sisestage sõna => "))
            result = word.strip()
            print(result)
        elif choice == 6:
            word = str(input("Sisestage sõna => "))
            prefix = str(input("Sisestage prefix => "))
            result = word.startswith(prefix)

            if result:
                print(f"Sõna „{word}“ algab „{prefix}“-ga.")
            else:
                print(f"Sõna „{word}“ ei alga „{prefix}“-ga.")
        elif choice == 7:
            pass    
        elif choice == 8:
            pass    
        elif choice == 9:
            pass    
        elif choice == 10:
            pass

        print()
        choice = int(input("Kas te soovite jätkata? (1 - jah, 0 - ei) => "))
        if choice != 1:
            break
        print()

    except Exception as e:
        print(f"ERROR: {e}")