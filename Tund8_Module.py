# --------------------------------------

import random
from email.message import EmailMessage
import smtplib
import ssl

# --------------------------------------

USER_NAME = 0
USER_PSW = 1
USER_EMAIL = 2
USER_RIGHTS = 3

EMAIL = "nikitalitvinenko28@gmail.com"
EMAIL_PSW = "" # aaaa aaaa aaaa aaaa

def get_input(data_type: type, text: str) -> any:
    """
    Tagastab määratud andmetüübiga sisendi andmed.
    :param (tüüp) data_type: andmetüüp.
    :param (str) tekst: kasutajale kuvatav tekst.
    """

    try:
        data = data_type(input(text))
    except:
        return False

    return data

def generate_password() -> str:
    """
    Genereerib parooli juhuslikult.
    Generates password using random.
    """

    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()

    str4 = str0+str1+str2+str3
    ls = list(str4)
    random.shuffle(ls)
    psword = ''.join([random.choice(ls) for x in range(12)])
    return psword

def is_password_valid(password: str) -> bool:
    """
    Tagastab tõene, kui parool on õige. 
    Parool peab sisaldama vähemalt numbreid või tähti ja olema vähemalt 4 tähemärki pikk.
    Возвращает True если пароль корректный. 
    Пароль состоит хотябы из цифр или букв и длина не менее 4 символов.
    """

    alpha = 0
    num = 0
    for char in password:
        if char.isalpha():
            alpha += 1
        elif char.isnumeric():
            num += 1

    if alpha == 0 and num == 0:
        print("Parool ei sisalda vähemalt numbreid või tähti!")
        return False

    if len(password) < 4:
        print("Parool on liiga väike. Vähemalt 4 tähemärki!")
        return False

    return True

def is_user_name_valid(user_name: str) -> bool:
    """
    Tagastab väärtuse Tõene, kui nimi on õige.
    Nimi ei koosne ainult numbritest ja nime pikkus on üle 3 tähemärgi.
    Возвращает True если имя корректное. 
    Имя состоит не только из цифр и длина имени не менее 3 символов.
    """

    if user_name.isnumeric():
        print("Nimi ei saa koosneda ainult numbritest.")
        return False

    if len(user_name) < 3:
        print("Nimi on liiga väike. Vähemalt 3 tähemärki!")
        return False

    return True

def is_admin(user: list) -> bool:
    """
    Tagastab väärtuse Tõene, kui kasutajal on külalisõigused.
    Возвращает True если у пользователя есть права гостя
    """

    return "admin" in user[USER_RIGHTS]

def is_guest(user: list) -> bool:
    """
    Tagastab väärtuse Tõene, kui kasutajal on administraatori õigused.
    Возвращает True если у пользователя есть права админа.
    """

    return "guest" in user[USER_RIGHTS]

def create_email_msg(subject: str, sender: str, receiver: str) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver

    return message

def send_email(subject: str, receiver: str, content: str):
    subject = subject
    content = content
    sender = EMAIL
    password = EMAIL_PSW

    html_content = f"""
    <!DOCTYPE html>
    <head>
    </head>
        <body>
            <h1>Sending an HTML email from Python</h1>
            <p>{content}</p>
            <a href="https://moodle.edu.ee/course/view.php?id=8327">Moodle</a>
            <br>
            <a href="https://github.com/nikita-lit">My Github</a>
        </body>
    </html>
    """

    message = create_email_msg(subject, sender, receiver)
    message.set_content(html_content, subtype="html")

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(sender, password)
            server.send_message(message)
        print("Kiri saadetud!")
    except Exception as e:
        print(f"ERROR: {e}")