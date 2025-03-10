import random

word = "Programmeerimine"
print(word)
words_list = list(word)

# print(words_list)
# words_list.reverse()
# print(words_list)
# print(words_list.index("P"))
# print(len(words_list))
# print(len(word))

# m_count = words_list.count("m")

# for i in range(m_count):
#     words_list.remove("m")

# stars = random.randint(1,2)
# for i in range(stars):
#     while True:
#         try:
#             w = input("Sisesta täht: ")
#             if w.isalpha():
#                 break
#             else:
#                 print("On vaja täht!")
#         except Exception as e:
#             print(f"ERROR: {e}")

#     words_list.append(w)

# print(words_list)

stars = random.randint(1,1)
for i in range(stars):
    while True:
        try:
            w = input("Sisesta täht: ")
            if w.isalpha():
                break
            else:
                print("On vaja täht!")
        except Exception as e:
            print(f"ERROR: {e}")    
    while True:
        try:
            index = input("Sisesta index: ")
            if index.isnumeric():
                if int(index) < len(words_list) and int(index) > 0:
                    break
                else:
                    print(f"Ainult numbrid 0-{len(words_list)-1}")
            else:
                print("Ainult numbrid!")
        except Exception as e:
            print(f"ERROR: {e}")

    words_list.insert(int(index), w)

print(words_list)

def func(e):
    return len(e)

words_list.sort(reverse=True, key=func)
print(words_list)