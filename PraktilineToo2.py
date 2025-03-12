# --------------------------------------
# Praktiline töö 1: Sõne ja järjesti funktsioonid.
# --------------------------------------

funcs_list = [
    "swapcase()",   # 1. Muudab kõik suurtähed väikesteks ja vastupidi. (Меняет все большие буквы на маленькие и наоборот.)
    "join()",       # 2. Liidab stringide loendi üheks stringiks, kasutades määratud eraldajat. (Соединяет элементы списка строк в одну строку, вставляя между ними указанный разделитель.)
    "partition()",  # 3. Jagab stringi kolmnurgaks: enne eraldajat, eraldaja ise ja pärast eraldajat olev osa. (Разделяет строку на три части: до разделителя, сам разделитель и после разделителя.)
    "zfill()",      # 4. Täidab stringi vasakult nullidega, et saavutada määratud pikkus. (Дополняет строку нулями слева до заданной длины.)
    "strip()",      # 5. Eemaldab stringi algusest ja lõpust tühikud. (Убирает лишние пробелы в начале и в конце строки.)
    "startswith()", # 6. Kontrollib, kas string algab määratud prefiksiga. (Проверяет, начинается ли строка с указанного префикса.)
    "title()",      # 7. Muudab iga sõna esimesed tähed suureks. (Делает первую букву каждого слова в строке заглавной.)
    "replace()",    # 8. Asendab kõik alamsõnad teise alamsõnaga. (Заменяет одно слово на другое.)
    "split()",      # 9. Jagab stringi loendiks, kasutades määratud eraldajat. (Разбивает строку на список строк, используя указанный разделитель.)
    "count()",      # 10. Tagastab määratud alamsõna esinemiskordade arvu stringis. (Возвращает количество вхождений подстроки в строке.)
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
        if choice != 0:
            print(f"Teie valik on {funcs_list[choice-1]}")

        if choice == 0:
            break
        elif choice == 1:
            word = input("Sisestage sõna => ")
            print(f"Teie sõna: {word}")
            print(f"Sõna pärast swapcase(): {word.swapcase()}")
        elif choice == 2:
            words = []

            for i in range(4):
                word = input(f"Sisestage {i+1}. sõna => ")
                words.append(word)

            separator = input("Sisestage separator sõna => ")
            result = separator.join(words)
            print(result)   
        elif choice == 3:
            sentence = input("Sisestage lause => ")
            separator = input("Sisestage separator sõna => ")
            result = sentence.partition(separator)
            print(result)
        elif choice == 4:
            word = input("Sisestage sõna => ")
            length = int(input("Sisestage pikkus => "))
            result = word.zfill(length)
            print(result)
        elif choice == 5:
            word = input("Sisestage sõna => ")
            result = word.strip()
            print(result)
        elif choice == 6:
            word = input("Sisestage sõna => ")
            prefix = input("Sisestage prefix => ")
            result = word.startswith(prefix)

            if result:
                print(f"Sõna „{word}“ algab „{prefix}“-ga.")
            else:
                print(f"Sõna „{word}“ ei alga „{prefix}“-ga.")
        elif choice == 7:
            word = input("Sisestage sõna => ")
            title = word.title()
            print(f"Algne sõna: {word}")
            print(f"Pealkirjaga sõna: {title}")
        elif choice == 8:
            sentence = input("Sisestage lause => ")
            word = input("Sisestage sõne mida muuda => ")
            new_word = input("Sisestage uus sõne => ")

            new_sentence = sentence.replace(word, new_word)
            print(f"Algne lause: {sentence}")
            print(f"Pärast asendamist: {new_sentence}")
        elif choice == 9:
            word = input("Sisestage sõna => ")
            separator = input("Sisestage separator => ")
            result = word.split(separator)
            print(f"Split sõna: {result}")
        elif choice == 10:
            word = input("Sisestage sõna => ")
            sub = input("Sisestage alamsõna => ")
            result = word.count(sub)
            print(f"Alamsõna esinemine: {result}")

        print()
        choice = int(input("Kas te soovite jätkata? (1 - jah, 0 - ei) => "))
        if choice != 1:
            break
        print()

    except Exception as e:
        print()
        print(f"ERROR: {e}")
        print()