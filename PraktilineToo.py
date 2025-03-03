
import random

ül_tehtud = 0
debug = False

while True:
    try:
        while True:
            try:
                tase = int(input(f"Sisesta tase (1, 2, 3) => "))
                if tase > 3 or tase <= 0:
                    print("Vale tase!")
                else:
                    while True:
                        ül_arv = int(input(f"Mitu ülesannet soovite lahendada? => "))
                        if ül_arv <= 0:
                            print("Vale number!")
                        else:
                            break
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

                if oper == 2 or oper == 3: # / or *
                    arv1 = random.randint(-10, 10)
                    arv2 = random.randint(-10, 10)
            elif tase == 3:
                oper = random.randint(0, 4)

                if oper == 4: # **             
                    arv1 = random.randint(1, 6)
                    arv2 = random.randint(1, 6)
                elif oper == 2: # /
                    arv1 = random.randint(-10, 10)
                    arv2 = random.randint(-10, 10)

                    while arv1 == 0 and oper == 2:
                        arv1 = random.randint(-10, 10)                    
                    while arv2 == 0 and oper == 2:
                        arv2 = random.randint(-10, 10)
                else:
                    arv1 = random.randint(-50, 50)
                    arv2 = random.randint(-50, 50)
            else:
                print("Vale tase!")
                break

            vastus = float(eval(str(arv1)+tehed[oper]+str(arv2)))
            vastus = round(vastus, 2)

            print()
            print("--------------------------------------")
            print(f"[{i+1} / {ül_arv}]")
            print("--------------------------------------")
            print()
            print(f"{arv1} {tehed[oper]} {arv2} = ?")
            if debug:
                print(f"[Debug] Vastus: {vastus}")
            print()

            while True:
                try:
                    kasutaja_vastus = float(input("Sisesta vastus => "))
                    break
                except Exception as e:
                    print(f"ERROR: {e}")

            print(f"Teie vastus: {kasutaja_vastus}")
            print(f"Õige vastus: {vastus}")

            if kasutaja_vastus == vastus or kasutaja_vastus == round(vastus):
                print("Tore!")
                ül_tehtud += 1
            else:
                print("Vale!")

            print()

        print("--------------------------------------")
        print(f"Õigesti tehtud ülesanded kokku: {ül_tehtud}/{ül_arv}")

        protsent = (ül_tehtud/ül_arv) * 100
        print(f"Protsent: {protsent}%")
        if protsent >= 90:
            hinne = 5
        elif protsent >= 75 and protsent <= 90:
            hinne = 4
        elif protsent >= 60 and protsent <= 75:
            hinne = 3
        else:
            hinne = 2
        print(f"Teie hinne:  {hinne}")
        print("--------------------------------------")

        print()

        veel = int(input("Kas te soovite rohkem ülesanded? (jah - 1, ei - 0) => "))

        if veel != 1:
            break

        print()

    except Exception as e:
        print(f"ERROR: {e}")