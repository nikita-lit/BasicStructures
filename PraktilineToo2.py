from tkinter import W


funcs_list = [
    "swapcase()",
    "test()",
    "test()",
    "test()",
    "test()",
    "test()",
    "test()",
    "test()",
    "test()",
    "test()",
]

while True:
    print("Millist funktsiooni te soovite näha?")

    for i in range(len(funcs_list)):
        print(f"{i+1}. {funcs_list[i]}")

    while True:
        try:
            choice = int(input("Sisestage arv => "))
            break
        except Exception as e:
            print(f"ERROR: {e}")

    try:
        if choice == 1:
            word = str(input("Sisestage sõna => "))
            print(f"Teie sõna: {word}")
            print(f"Sõna pärast swapcase(): {word.swapcase()}")

            pass
        elif choice == 2:
            pass    
        elif choice == 3:
            pass    
        elif choice == 4:
            pass    
        elif choice == 5:
            pass    
        elif choice == 6:
            pass    
        elif choice == 7:
            pass    
        elif choice == 8:
            pass    
        elif choice == 9:
            pass    
        elif choice == 10:
            pass
    except Exception as e:
        print(f"ERROR: {e}")

    break