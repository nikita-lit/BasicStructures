
import random

ül_tehtud = 0

try:
    while True:
        try:
            tase = int(input(f"Sisesta tase (1, 2, 3) => "))
            if tase > 3 or tase < 0:
                print("Vale tase!")
            else:
                ül_arv = int(input(f"Mitu ülesannet soovite lahendada? => "))
                break
        except Exception as e:
            print(f"ERROR: {e}")

    for i in range(ül_arv):
        tehed = ["+", "-", "/", "*", "**"]

        if tase == 1:
            oper = random.randint(0, 1)
            arv1 = random.randint(0, 50)
            arv2 = random.randint(0, 50)
        elif tase == 2:
            oper = random.randint(0, 3)
            arv1 = random.randint(-50, 50)
            arv2 = random.randint(-50, 50)

            if oper == 2:
                arv1 = random.randint(-10, 10)
                arv2 = random.randint(-10, 10)
        elif tase == 3:
            oper = random.randint(0, 4)
            if oper == 4:                
                arv1 = random.randint(1, 6)
                arv2 = random.randint(1, 6)
            elif oper == 2:
                arv1 = random.randint(-10, 10)
                arv2 = random.randint(-10, 10)
            else:
                arv1 = random.randint(-50, 50)
                arv2 = random.randint(-50, 50)
        else:
            print("Vale tase!")
            break

        print()
        print(f"{arv1} {tehed[oper]} {arv2} = ?")

        while True:
            try:
                kasutaja_vastus = float(input("Sisesta vastus => "))
                break
            except Exception as e:
                print(f"ERROR: {e}")

        vastus = float(eval(str(arv1)+tehed[oper]+str(arv2)))

        print(f"Teie vastus: {kasutaja_vastus}")
        print(f"Õige vastus: {vastus}")

        if kasutaja_vastus == vastus or kasutaja_vastus == round(vastus):
            print("Tore!")
            ül_tehtud += 1
        else:
            print("Vale!")

        print()

    print()
    print(f"Õigesti tehtud ülesanded kokku: {ül_tehtud}/{ül_arv}")
    print()

except Exception as e:
    print(f"ERROR: {e}")