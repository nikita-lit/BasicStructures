# --------------------------------------
# Praktiline töö 6.2 "Sõnastik" kome keelne
# --------------------------------------

from SuperModule import *
import time
import pyttsx3
import random

# --------------------------------------

languages = {
    "est": "Eesti", 
    "rus": "Vene", 
    "eng": "Inglise"
}

sonastik = {}

def init_dictionary():
    default_words = {
        "est": ["koer", "kass", "maja", "auto", "päike"], 
        "rus": ["собака", "кошка", "дом", "машина", "солнце"], 
        "eng": ["dog", "cat", "house", "car", "sun"]
    }

    for lang, lang_name in languages.items():
        sonastik[lang] = []

    for lang, words in default_words.items():
        sonastik[lang] = words

def get_language_code_by_name(name: str):
    for lang, lang_name in languages.items():
        if name.strip().lower() == lang_name.strip().lower() or \
           name.strip().lower() == lang.strip().lower():
            return lang

    return None

def get_language_by_word(word: str):
    for lang, words in sonastik.items():
        if word.strip().lower() in words:
            return lang

    return None

def translate():
    word = get_input(str, "Sisestage sõna => ")

    print()
    print("Keele määratlemine...")
    time.sleep(2)
    orig_lang = get_language_by_word(word)
    if not orig_lang:
        print("Tundmatu keel või sõna!")
        return
    else:
        print(f"Sõna {word} on {languages[orig_lang]} sõna.")

    time.sleep(1)
    print()
    target_lang_input = get_input(str, "Sisestage teine keel => ")
    target_lang = get_language_code_by_name(target_lang_input)

    if not target_lang:
        print("Tundmatu keel!")
        return

    translated_word = translate_word(orig_lang, target_lang, word)
    if not translated_word[0]:
        print(translated_word[1])
        return

    print("Tõlkimine...")
    time.sleep(1)
    print(f"Sõna {word} {languages[target_lang]}es on {translated_word}")

def translate_word(orig_lang: str, target_lang: str, word: str) -> str:
    if not orig_lang in languages:
        return False, f"Keel [{orig_lang}] ei leitud!"
    elif not target_lang in languages:
        return False, f"Keel [{target_lang}] ei leitud!"

    try:
        for lang, words in sonastik.items():
            if lang == orig_lang.lower():
                orig_index = words.index(word.lower())
                if words[orig_index]:
                    return sonastik[target_lang][orig_index]
    except:
        return False, "Sõna ei leitud!"

def does_word_exist(word: str, target_lang: str):
    if target_lang:
        if word in sonastik[target_lang]:
            return True
    else:
        for lang, words in sonastik.items():
            if word.strip().lower() in words:
                return True

    return False

def is_word_correct_for_dict(word: str, target_lang: str) -> bool:
    if not word.isalpha():
        print("Sõna peab koosnema märgist!")
        return False

    if does_word_exist(word, target_lang):
        print("Sõna on juba olemas!")
        return False

    return True

def add_word_to_dict():
    words = {}
    for lang, lang_name in languages.items():
        words[lang] = ""

    for lang, lang_name in languages.items():
        while True:
            word = get_input(str, f"Sisestage sõna {lang_name}es => ")
            if is_word_correct_for_dict(word, lang):
                words[lang] = word.strip().lower()
                break

    for lang, word in words.items():
        sonastik[lang].append(word)

def correct_word():
    target_lang_input = get_input(str, "Sisestage keel => ")
    target_lang = get_language_code_by_name(target_lang_input)

    if not target_lang: 
        print(f"Tundmatu keel [{target_lang_input}] !") 
        return

    word_to_correct = get_input(str, "Sisestage sõna, mida te soovite parandada => ")
    words = sonastik[target_lang]

    if word_to_correct in words:
        while True:
            correct_word = get_input(str, "Sisestage parandatud sõna => ")
            if is_word_correct_for_dict(correct_word):
                sonastik[target_lang][words.index(word_to_correct)] = correct_word
                break

def test_knowledge():
    orig_lang_input = get_input(str, "Sisestage esimene keel => ")
    orig_lang = get_language_code_by_name(orig_lang_input)

    if not orig_lang: 
        print(f"Tundmatu keel [{orig_lang_input}] !") 
        return

    target_lang_input = get_input(str, "Sisestage teine keel => ")
    target_lang = get_language_code_by_name(target_lang_input)

    if not target_lang: 
        print(f"Tundmatu keel [{target_lang_input}] !") 
        return

    print()
    print(f"Test: {languages[orig_lang]} → {languages[target_lang]}")
    print()

    max_words = get_input(int, "Mitu sõna soovite kontrollida? => ")
    orig_words = sonastik[orig_lang]
    if max_words >= len(orig_words):
        max_words = len(orig_words)

    words = random.sample(orig_words, max_words)
    points = 0
    num = 0

    for word in words:
        orig_index = orig_words.index(word)
        correct = sonastik[target_lang][orig_index]
        answer = get_input(str, f"{num+1}. Tõlgi sõna {word} => ").strip().lower()
        if answer == correct:
            print("Õige!")
            points += 1
        else:
            print(f"Vale! Õige vastus: {correct}")
        print()
        num += 1

    print(f"Test lõppenud! Sinu tulemus: {points}/{max_words}")

def show_dictionary():
    for lang, words in sonastik.items():
        print(f"Keel: {languages[lang]}")
        num = 0
        for word in words:
            print(f"    {num+1}. {word}")
            num += 1