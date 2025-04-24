
# --------------------------------------
# Praktiline töö 7.2 "Tarkvaraarendaja vastuvõtt"
# --------------------------------------

from SuperModule import *
from email.message import EmailMessage
import time
import smtplib
import ssl
import random

# --------------------------------------

questions = {}
users = {}

USERS_NUM = 3
QUESTIONS_NUM = 5

TXT = "kusimused.txt"
TXT_USERS = "osalejad.txt"
APP_EMAIL = "nikitalitvinenko28@gmail.com"
APP_PASSWORD = "aaaa aaaa aaaa aaaa"

# --------------------------------------
def load_questions() -> list:
    lines = read_file(TXT)
    quests = {}
    for line in lines:
        k,v = line.strip().split("=")
        quests[k] = v

    return quests

def load_users() -> list:
    lines = read_file(TXT_USERS)
    users = {}
    for line in lines:
        k,v = line.strip().split("=")
        email, score = v.split(";")
        users[k] = {"email": email, "score": score}

    return users

def save_questions():
    time.sleep(1.5)
    lines = []
    for question, answer in questions.items():
        lines.append(f"{question}={answer}")

    write_file(TXT, lines)
    print("Küsimused salvestatud!")
    
def save_users():
    time.sleep(1.5)
    lines = []
    for name, data in users.items():
        email = data["email"]
        score = data["score"]
        lines.append(f"{name}={email};{score}")

    write_file(TXT_USERS, lines)
    print("Osalejad salvestatud!")

# --------------------------------------
def init_test():
    global questions, users
    questions = load_questions()
    users = load_users()

# --------------------------------------
def start_test():
    for i in range(USERS_NUM):
        print(f"{i+1}. Osaleja")
        while True:
            input_name = get_input(str, "Sisestage nimi => ").strip().lower()
            if not input_name in users:
                break
            else:
                print(f"{input_name} on juba testi teinud.")

        while True:
            email = get_input(str, "Sisestage e-post => ").strip().lower()
            for name, data in users.items():
                if email == data["email"]:
                    print("E-post on juba kasutusel!")
                    break
            else:
                break

        random_questions = get_random_questions(QUESTIONS_NUM)
        score = 0

        for question in random_questions:
            answer = questions[question]
            user_answer = get_input(str, f"{question} ").lower()
            if user_answer == answer.lower():
                print("Õige")
                score += 1
            else:
                print(f"Vale! Õige vastus on {answer}")

        if score > QUESTIONS_NUM / 2:
            send_email("Testi tulemused - edukas!", f"Tere {input_name.capitalize()}!\nTeie skoor: {score}/{QUESTIONS_NUM} õigesti.\nOlete testi läbi teinud!", APP_EMAIL, email)
            print(f"Teie skoor on {score}/{QUESTIONS_NUM}.")
        else:
            send_email("Testi tulemused - pahad!", f"Tere {input_name.capitalize()}!\nTeie skoor: {score}/{QUESTIONS_NUM} õigesti.\nKahjuks ei läinud test hästi.", APP_EMAIL, email)
            print(f"Kahjuks, te ei lähe läbi, {input_name}. Teie skoor on {score}/{QUESTIONS_NUM}.")

        users[input_name] = {"email": email, "score": score}
        save_users()

        print()

    send_report_to_employer()

def get_random_questions(num: int) -> dict:
    return random.sample(list(questions), min(len(questions), num))

def send_report_to_employer():
    content = "Tere!\nTänased testi tulemused:\n"

    num = 0
    best_score = 0
    best_result = ""
    for name, data in users.items():
        email = data["email"]
        score = data["score"]

        status = (score > QUESTIONS_NUM / 2) and "SOBIB" or "EI SOBI"
        content += f"{num+1}. {name} - {score} punkti - {email} - {status}\n"
        num += 1
        if score > best_score:
            best_score = score
            best_result = f"Parim kandidaat: {name} ({score} punkti)\n"

    content += best_result

    send_email("Tulemuste aruanne", content, APP_EMAIL, APP_EMAIL)

# --------------------------------------
def add_new_question():
    question = get_input(str, "Sisestage uus küsimus => ")
    answer = get_input(str, "Sisestage õige vastus => ")
    questions.append({question: answer})
    save_questions()

# --------------------------------------
def show_questions_users():
    print("Küsimused:")
    for question, answer in questions.items():
        print(f"{question} - {answer}")

    print()
    print("Osalejad:")
    for name, data in users.items():
        email = data["email"]
        score = data["score"]
        print()
        print(f"{name}\n E-post: {email}\n Skoor: {score}")

# --------------------------------------
def send_email(subject: str, content: str, sender: str, receiver: str):
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver
    message.set_content(content)

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(sender, APP_PASSWORD)
            server.send_message(message)
        print("Kiri saadetud!")
    except Exception as e:
        print(f"ERROR: {e}")