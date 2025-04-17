# --------------------------------------

from email.message import EmailMessage
from fileinput import filename
import smtplib
import ssl
from tkinter import filedialog
from SuperModule import *

# --------------------------------------
TUNDTXT = "Tund9.txt"

def read_file(file: str) -> list:
    f = open(file, 'r', encoding="utf-8-sig")
    lines = []
    for line in f:
        lines.append(line.strip())
    f.close()
    return lines

def print_file(file: str):
    for line in read_file(file):
        print(line)

def write_file(file: str, lines:list):
    f = open(file, 'w', encoding="utf-8-sig")
    for line in lines:
        f.write(line + '\n')
    f.close()

# names_list = ["Ann", "Kati", "Mari"]
# write_file(TUNDTXT, names_list)

# print_file(TUNDTXT)

# with open(TUNDTXT, 'r', encoding="utf-8-sig") as f:
#     print(f.read())

def file_to_dict(file: str):
    riik_pealinn = {}
    pealinn_riik = {}
    riigid = []
    for line in read_file(file):
        k,v = line.strip().split("-")
        riik_pealinn[k] = v
        pealinn_riik[v] = k
        riigid.append(k)

    return riik_pealinn, pealinn_riik, riigid

# riik_pealinn, pealinn_riik, riigid = file_to_dict("riigid_pealinnad.txt")

# for key, value in riik_pealinn.items():
#     print(key, value)
    
# print()

# for key, value in pealinn_riik.items():
#     print(key, value)

# print()

# for value in riigid:
#     print(value)

def create_email_msg(subject: str, sender: str, receiver: str) -> EmailMessage:
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = receiver

    return message

def send_email():
    receiver = get_input(str, "Kellele saata => ")
    subject = get_input(str, "Teema => ")
    content = get_input(str, "Sisu => ")
    sender = "nikitalitvinenko28@gmail.com"
    password = get_input(str, "Salasõna => ")

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

    file = filedialog.askopenfilename(title="Vali fail", filetypes=[("All files", "*.*")])

    with open(file, "rb") as f:
        file_content = f.read()
        file_name = file.split("/")[-1]
        message.add_attachment(file_content, maintype="application", subtype="octet-stream", filename=file_name)

    print(f"Attachment: {file_name}")

    choice = get_input(str, "Kas saata kiri? ( 1-jah / 0-ei ) => ").lower()
    if choice != "1" and choice != "jah":
        return

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(sender, password)
            server.send_message(message)
        print("Kiri saadetud!")
    except Exception as e:
        print(f"ERROR: {e}")

send_email()