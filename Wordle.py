# --------------------------------------
# Töö 4.3: Praktiline iseseisevtöö "Wordle"
# --------------------------------------

import random
import colorama
colorama.just_fix_windows_console()

# --------------------------------------
words = [
    'rakendus', 
    'matemaatika', 
    'python', 
    'andmebaas', 
    'server', 
    'interneti', 
    'pilv'
]

random_word = random.choice(words)
random_word_length = len(random_word)

GREEN = '\033[92m'
YELLOW = '\033[93m'
WHITE = '\033[0m'

ATTEMPTS = 6
print(f"Arvake sõna, mille pikkus on {random_word_length} tähemärki. Teil on {ATTEMPTS} katset.")

for i in range(ATTEMPTS):
    while True:
        guess = input(f"Proov {i + 1} => ").lower()
        
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
            yellow_letters .append(random_word[j])

    for j in range(random_word_length):
        if colored_guess[j] == None:
            if guess[j] in yellow_letters:
                colored_guess[j] = f"{YELLOW}{guess[j]}{WHITE}"
                yellow_letters.remove(guess[j])
            else:
                colored_guess[j] = f"{WHITE}{guess[j]}{WHITE}"
    
    print("".join(colored_guess))
    
    if guess == random_word:
        print("Palju õnne! Sa arvasid sõna õigesti!")
        break
else:
    print(f"Õige sõna oli: {random_word}. Kahjuks ei õnnestunud ära arvata.")