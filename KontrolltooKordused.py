# --------------------------------------
# Kontrolltöö "Kordused" V5
# --------------------------------------

import random

# --------------------------------------
# 1.

print("--------------------------------------")
print("1.")
print("--------------------------------------")
print()

try:
    while True:
        try:
            N = int(input(f"Sisesta N => "))
            if N > 9 or N < 1:
                print("Kirjuta ainult numbrid 1-9")
            else:
                break
        except:
            print("Kirjuta ainult numbrid")

    print(" ~~~~~    " * N)
    print("/_____\\   " * N)
    print("| []  |   " * N)
    print(" -----    " * N)

except Exception as e:
    print(f"ERROR: {e}")

print()

# --------------------------------------
# 2. Известны оценки по физике каждого ученика двух классов. Определить среднюю оценку в каждом классе. Количество учащихся в каждом классе одинаковое.

print("--------------------------------------")
print("2.")
print("--------------------------------------")
print()

classes_number = 2
students_number = 5
grades_sum = 0
grades_count = 0

for c in range(classes_number):
    print()
    print(f"{c+1}. klass")
    for i in range(students_number):
        student_grade = random.randint(2, 5)
        grades_sum += student_grade
        grades_count += 1
        print(f"Õpilane {i+1}. hinne on {student_grade}")

avg_grade = (grades_sum) / grades_count

print()
print(f"Keskmine hinne on {round(avg_grade, 1)}")
print()

# --------------------------------------
# 3. Известны средние оценки каждого из  учеников класса. Определить минимальную и максимальную оценки. (Оценки и количество учеников получаем случайным образом). 
# Использовать только цикл и сравнительные операторы. max() и min() не использвать.

print("--------------------------------------")
print("3.")
print("--------------------------------------")
print()

students_number = random.randint(1, 15)
max_grade = 0
min_grade = 5

for i in range(students_number):
    student_grade = round(random.randint(20, 50) / 10, 1)
    print(f"Õpilane {i+1}. hinne on {student_grade}")
    if student_grade > max_grade:
        max_grade = student_grade

    if student_grade < min_grade:
        min_grade = student_grade

print()
print("--------------------------------------")
print(f"Maksimaalne hinne on {max_grade}")
print(f"Minimaalne hinne on {min_grade}")
print("--------------------------------------")
print()

# --------------------------------------
# 4. В области 12 районов. Известны количество жителей (в тысячах человек) и площадь (в км2) каждого района. 
# Определить среднюю плотность населения по области в целом. Исходные данные рандомные.

print("--------------------------------------")
print("4.")
print("--------------------------------------")
print()

district_number = 12
avg_districts_density = 0
districts_density_sum = 0

for i in range(district_number):
    population = random.randint(1000, 9999)
    area = random.randint(500, 5000)
    density = population / area
    districts_density_sum += density
    print(f"Ringkond {i+1}.")
    print(f"Rahvarv: {population}")
    print(f"Pindala: {area}")
    print(f"Asustustihedus: {round(density, 2)} inimest km² kohta")
    print()
    
avg_districts_density = (districts_density_sum) / district_number

print(f"Piirkonna keskmine asustustihedus on {round(avg_districts_density, 2)} inimest km² kohta")
print()

# --------------------------------------
# 5.Вывести таблицу значений функции y = -0.5x + x. Значения аргумента (x) задаются минимумом, максимумом и шагом. Например, если минимум задан как 1, максимум равен 3, а шаг 0.5. То надо вывести на экран изменение x от 1 до 3 с шагом 0.5 (1, 1.5, 2, 2.5, 3) и значения функции (y) при каждом значении x.

print("--------------------------------------")
print("5.")
print("--------------------------------------")
print()

try:
    print("Funktsioon on [y = -0.5x + x]")
    while True:
        try:
            min_X = int(input(f"Sisesta min X => "))
            max_X = int(input(f"Sisesta max X => "))
            step = float(input(f"Sisesta samm => "))

            if min_X > max_X:
                print("min X ei saa olla suurem kui max X")
            else:
                break
        except Exception as e:
            print(f"ERROR: {e}")

    print()
    X = min_X
    
    print("--------------------------------------")
    print("X         /         Y                 ")
    print("--------------------------------------")

    while X <= max_X:
        Y = (-0.5 * X) + X
        print(f"{X}             {Y}")
        #print(f"Y = -0.5x + {X}")
        #print(f"Y = {Y}")
        print()
        X += step

except Exception as e:
    print(f"ERROR: {e}")