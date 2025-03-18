# --------------------------------------
# Töö 4.3: Praktiline iseseisevtöö "Wordle"
# --------------------------------------

import random
import colorama
colorama.just_fix_windows_console()

# --------------------------------------
words = [
    'rakendus', 
    'töö', 
    'python', 
    'andmebaas', 
    'server', 
    'interneti', 
    'pilv'
]

GREEN = '\033[92m'
YELLOW = '\033[93m'
WHITE = '\033[0m'

ATTEMPTS = 6

while True:
    random_word = random.choice(words)
    random_word_length = len(random_word)

    print(f"Arvake sõna, mille pikkus on {random_word_length} tähemärki. Teil on {ATTEMPTS} katset.")

    for i in range(ATTEMPTS):
        while True:
            guess = input(f"Proov {i + 1}. => ").lower()
        
            if len(guess) == random_word_length:
                break
            else:
                print(f"Palun sisestage sõna, mille pikkus on täpselt {random_word_length} tähemärki.")
    
        colored_guess = []
        yellow_letters  = []
    
        for j in range(random_word_length):
            if guess[j] == random_word[j]:
                colored_guess.append(f"{GREEN}{guess[j]}{WHITE}")
            else:
                colored_guess.append(None)
                yellow_letters.append(random_word[j])

        for j in range(random_word_length):
            if colored_guess[j] == None:
                if guess[j] in yellow_letters:
                    colored_guess[j] = f"{YELLOW}{guess[j]}{WHITE}"
                    yellow_letters.remove(guess[j])
                else:
                    colored_guess[j] = f"{WHITE}{guess[j]}{WHITE}"
    
        print("".join(colored_guess))
    
        if guess == random_word:
            print()
            print("Palju õnne! Sa arvasid sõna õigesti!")
            break
        elif i == (ATTEMPTS-1):
            print()
            print(f"Õige sõna oli: {random_word}. Kahjuks ei õnnestunud ära arvata.")

    try:
        choice = int(input("Kas te soovite jätkata? (1 - jah, 0 - ei) => "))
        if choice != 1:
            break
    except Exception as e:
        print(f"ERROR: {e}")
        break