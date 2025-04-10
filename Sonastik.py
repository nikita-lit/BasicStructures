# --------------------------------------
# Praktiline töö 6.2 "Sõnastik" kome keelne
# --------------------------------------

from SuperModule import *
import time
import pyttsx3

# --------------------------------------

languages = {
    "est": "Eesti keel", 
    "rus": "Vene keel", 
    "eng": "Inglise keel"
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

def get_language_by_word(word):
    for lang, words in sonastik.items():
        if word in words:
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
        print(f"Sõna {word} on {languages[orig_lang]}")

    time.sleep(1)
    print()
    target_lang = get_input(str, "Sisestage teine keel => ")
    translated_word = translate_word(orig_lang, target_lang, word)
    print(f"Sõna {word} {languages[target_lang]}es on {translated_word}")

def translate_word(orig_lang: str, target_lang: str, word: str) -> str:
    if not orig_lang in languages:
        return f"Keel [{orig_lang}] ei leitud!"

    try:
        for lang, words in sonastik.items():
            if lang == orig_lang.lower():
                orig_index = words.index(word.lower())
                if words[orig_index]:
                    return sonastik[target_lang][orig_index]
    except:
        return "Sõna ei leitud!"

def add_word_to_dict():
    words = {}
    for lang, lang_name in languages.items():
        words[lang] = ""

    for lang, lang_name in languages.items():
        while True:
            word = get_input(str, f"Sisestage sõna {lang_name}es => ")

            for char in word:
                if char.isnumeric():
                    print("Sõnas ei saa olla numbrit!")
                    break
            else: 
                if len(word) <= 0:
                    print("Sõna peab koosnema vähemalt ühest märgist!")
                else:
                    words[lang] = word.strip().lower()
                    break