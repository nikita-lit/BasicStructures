# B-1 Kool

# Напишите функцию kool(), при запуске которой происходит заполнение двух списков: opilased[], puudumised[].
# После заполнения списков появляется меню с выбором действий:
# • Узнать n лучших учеников;
# • Упорядочить список в порядке возрастания прогулов. отобразить прогулы вместе с фамилиями учеников;
# • Вывести список учеников отправленных на комиссию ( критерий придумать самостоятельно);
# • Отчислить(удалить из списка)  учеников, у которых прогулов больше чем 100;
# • Свой вариант.
# Для решения задачи используйте функции.

from Tund8_Module import *
import random

opilased = []
puudumised = []
grades = []

STUDENTS_COUNT = 20

# --------------------------------------------
def fill_data():
    for i in range(STUDENTS_COUNT):
        student = [f"Eesnimi{i+1}", f"Perekonnanimi{i+1}"]
        opilased.append(student)

        absences = random.randint(0, 150)
        puudumised.append(absences)

        grade = random.randint(20, 50) / 10
        grades.append(grade)

# --------------------------------------------
def sort_best_students(student):
    return (-student[2], student[1])

def find_best_students(n: int):
    best_students = []
    for i in range(len(opilased)):
        best_students.append((opilased[i], puudumised[i], grades[i]))

    best_students.sort(key=sort_best_students)

    print("-----------------------------------")
    print("Parimad õpilased")
    print("-----------------------------------")
    num = 0
    for student in best_students:
        print(f"{num+1}. {student[0][1]} puudumised: {student[1]}, hinne: {student[2]}")
        num += 1
        if num == n:
            break
    print("-----------------------------------")
    print()

# --------------------------------------------
def sort_students_absences(student):
    return student[1]

def sort_absences():
    students_absences = []
    for i in range(len(opilased)):
        students_absences.append((opilased[i], puudumised[i]))

    students_absences.sort(key=sort_students_absences)

    print("-----------------------------------")
    print("Õpilased puudumiste arvu järgi")
    print("-----------------------------------")
    for student in students_absences:
        print(f"{student[0][1]}: {student[1]}")
    print("-----------------------------------")
    print()

# --------------------------------------------
def average_absences() -> float:
    """
    Tagastab keskmise puudumiste arvu.
    """
    sum = 0
    for i in range(len(puudumised)):
        sum += puudumised[i]

    return sum / len(puudumised)

# --------------------------------------------
def students_to_commission():
    print("-----------------------------------")
    print("Komisjoni saadetud õpilased (rohkem kui 50 puudumist ja hinne alla 3)")
    print("-----------------------------------")
    print()
    num = 0
    for i in range(len(opilased)):
        if puudumised[i] > 50 and grades[i] < 3:
            print(f"{opilased[i][0] } {opilased[i][1]}")
            print(f"puudumised: {puudumised[i]}, hinne: {grades[i]}")
            print()
            num += 1

    print(f"{num} õpilast saadetud komisjoni.")

# --------------------------------------------
def expel_students():
    print("-----------------------------------")
    print("Eemaldatud õpilased (rohkem kui 100 puudumist ja hinne alla 2.5)")
    print("-----------------------------------")

    to_expel = []
    for i in range(len(opilased)):
        if puudumised[i] > 100 and grades[i] < 2.5:
            to_expel.append(i)

    if len(to_expel) == 0:
        print("Ei ole õpilasi, keda eemaldada")
    
    for i in to_expel:
        print(f"{opilased[i][0] } {opilased[i][1]}")
        print(f"puudumised: {puudumised[i]}, hinne: {grades[i]}")
        print()

    print(f"{len(to_expel)} õpilast eemaldatud.")
    for i in reversed(to_expel):
        opilased.pop(i)
        puudumised.pop(i)
        grades.pop(i)

# --------------------------------------------
def kool():
    fill_data()

    while True:
        print()
        print("1. Uuri välja n parimat õpilast")
        print("2. Korrasta nimekiri puudumiste arvu järgi")
        print("3. Kuvada õpilased, keda saadetakse komisjoni")
        print("4. Eemalda õpilased, kellel on rohkem kui 100 puudumist")
        print("5. Keskmine puudumiste arv")
        print("6. Lõpeta programm")
        
        print()
        choice = get_input(int, "Sisestage valik number => ")
        print()

        if choice == 1:
            while True:
                number = get_input(int, "Sisestage parimate õpilaste arv, kes kuvatakse => ")
                if number and number > 0:
                    find_best_students(number)
                    break
                else:
                    print("Vale arv!")
        elif choice == 2:
            sort_absences()
        elif choice == 3:
            students_to_commission()
        elif choice == 4:
            expel_students()
        elif choice == 5:
            print(f"Keskmine puudumiste arv on {average_absences():.2f}")
        elif choice == 6:
            break
        else:
            print("Vale valik!")

kool()