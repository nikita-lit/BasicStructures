# --------------------------------------
# Praktiline töö: "E-posti klient Minu Oma Outlook"
# --------------------------------------

import tkinter as tk
from tkinter import filedialog, messagebox
import smtplib
from email.message import EmailMessage
import ssl
import json
import datetime as dt
import os

# --------------------------------------

window = None
main_area = None

# send email
entry_theme = None
entry_to = None
text_area = None
file_list = None
attached_files = []
but_letter_frame = None

cur_letter = {}
cur_letter_readonly = False

# settings
entry_app_email = None
entry_app_password = None
#selected_theme = None

app_drafts = {}
app_logs = {}
app_logs2 = {}

#THEME_BLACK = "Must"
#THEME_WHITE = "Valge"

app_password = ""
app_email = ""
#app_theme = THEME_BLACK

TXT_SETTING = "outlook_settings.json"
TXT_DRAFTS = "outlook_drafts.json"
TXT_LOG = "outlook_log.json"

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600
MAIN_BG = "gray20"
TITLE_BG = "steel blue"
TITLE_FG = "white"
TB_BG = "gray15"
TBB_BG = "gray28"
TBB_BG_H = "gray50"
TBB_FG = "white"

def on_close():
    save_draft_letter()
    window.destroy() 

def create_window():
    load_settings()
    load_draft_letters()
    load_logs()

    global window, main_area

    window = tk.Tk()
    window.title("Outlook3000")
    window.resizable(width=False, height=False)
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.iconbitmap("icon.ico")
    window.grid_columnconfigure(1, weight=1)
    window.protocol("WM_DELETE_WINDOW", on_close)

    top_frame = tk.Frame(window, bg=TITLE_BG, height=20)
    top_frame.pack(fill=tk.X)

    create_taskbar()
    main_area = tk.Frame(window, bg=MAIN_BG)
    main_area.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    eval(taskbar_options[cur_option][1]+"()")

    window.mainloop()

def send_letter(insert: bool = True):
    set_cur_option(0)
    for widget in main_area.winfo_children():
        widget.destroy()

    global entry_to, entry_theme, text_area, file_list

    send_letter_frame = tk.Frame(main_area, bg=MAIN_BG)
    send_letter_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    # --------------------------------------
    # to
    frame_to = tk.Frame(send_letter_frame, bg=MAIN_BG, height=20)
    frame_to.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

    label_to = tk.Label(frame_to, text="Saaja e-post", bg=TITLE_BG, fg=TITLE_FG, width=12, font=("TkHeadingFont", 16))
    label_to.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)
    
    entry_to = tk.Entry(frame_to, bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 16))
    entry_to.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=True)
    
    # --------------------------------------
    # theme
    frame_theme = tk.Frame(send_letter_frame, bg=MAIN_BG, height=20)
    frame_theme.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

    label_theme = tk.Label(frame_theme, text="Teema", bg=TITLE_BG, fg=TITLE_FG, width=12, font=("TkHeadingFont", 16))
    label_theme.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)

    entry_theme = tk.Entry(frame_theme, bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 16))
    entry_theme.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=True)

    # --------------------------------------
    # atachments
    frame_attach = tk.Frame(send_letter_frame, bg=MAIN_BG, height=20)
    frame_attach.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

    label_attach = tk.Label(frame_attach, text="Failid", bg=TITLE_BG, fg=TITLE_FG, width=12, font=("TkHeadingFont", 16))
    label_attach.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)

    file_list_frame = tk.Frame(frame_attach, bg=MAIN_BG, height=5)
    file_list_frame.pack(fill=tk.BOTH, expand=True)

    file_list = tk.Listbox(file_list_frame, bg="gray20", fg="white", height=4, font=("TkDefaultFont", 12), highlightthickness=0, selectmode=tk.SINGLE)
    file_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(file_list_frame, orient=tk.VERTICAL, command=file_list.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    file_list.config(yscrollcommand=scrollbar.set)

    # --------------------------------------
    # text
    frame_text = tk.Frame(send_letter_frame, bg=MAIN_BG, height=16)
    frame_text.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

    text_area = tk.Text(frame_text, bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 16), wrap=tk.WORD, height=15)
    text_area.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.LEFT, expand=False)

    # --------------------------------------
    # buttons (send, attach)
    global but_letter_frame
    but_letter_frame = tk.Frame(send_letter_frame, bg=MAIN_BG, height=20)
    but_letter_frame.pack(fill=tk.BOTH, side=tk.BOTTOM)

    but_send = tk.Button(but_letter_frame, text="Saada kiri", command=cmd_send_email, bg=TITLE_BG, fg=TITLE_FG, font=("TkDefaultFont", 16), relief=tk.FLAT)
    but_send.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=True)

    but_attach = tk.Button(but_letter_frame, text="Lisa fail", command=cmd_attach_file, width=10, bg=TITLE_BG, fg=TITLE_FG, font=("TkDefaultFont", 16), relief=tk.FLAT)
    but_attach.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)

    but_clear = tk.Button(but_letter_frame, text="Puhasta", width=7, command=cmd_clear, bg=TBB_BG, fg=TITLE_FG, font=("TkDefaultFont", 16), relief=tk.FLAT)
    but_clear.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)

    if insert and cur_letter and not cur_letter_readonly:
        insert_letter(cur_letter)

def disable_buttons():
    global cur_letter_readonly
    cur_letter_readonly = True
    for widget in but_letter_frame.winfo_children():
        widget.destroy()

def drafts():
    set_cur_option(1)
    for widget in main_area.winfo_children():
        widget.destroy()

    global app_drafts
    for draft_date, draft in app_drafts.items():    
        but_frame = tk.Frame(main_area, bg=TBB_BG_H, height=20)
        but_frame.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.TOP, expand=False)
        
        date = dt.datetime.strptime(draft_date, "%Y-%m-%d %H:%M:%S.%f")
        but_open = tk.Button(but_frame, text="Ava ["+draft["subject"]+"]    "+date.strftime("%m/%d/%y %H:%M:%S"), command=lambda draft=draft: open_letter(draft), bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 12), relief=tk.FLAT)
        but_open.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=True)
        
        but_delete = tk.Button(but_frame, text="Kustuta", command=lambda draft_date=draft_date: delete_draft(draft_date), bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 12), relief=tk.FLAT)
        but_delete.pack(padx=5, pady=5, fill="x", side=tk.RIGHT, expand=False)
        
def inbox():
    set_cur_option(2)
    for widget in main_area.winfo_children():
        widget.destroy()
    
    global app_logs2
    for letter_date, letter in app_logs2.items():    
        but_frame = tk.Frame(main_area, bg=TBB_BG_H, height=20)
        but_frame.pack(padx=5, pady=5, fill=tk.BOTH, side=tk.TOP, expand=False)
        
        date = dt.datetime.strptime(letter_date, "%Y-%m-%d %H:%M:%S.%f")
        but_open = tk.Button(but_frame, text="Ava ["+letter["subject"]+"]    "+date.strftime("%m/%d/%y %H:%M:%S")+" ["+(letter["sent"] and "Toimetatud" or "Ei toimetatud") + "]", command=lambda letter=letter: open_letter(letter, True), bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 12), relief=tk.FLAT)
        but_open.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=True)
        
        but_delete = tk.Button(but_frame, text="Kustuta", command=lambda letter_date=letter_date: delete_log_letter(letter_date), bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 12), relief=tk.FLAT)
        but_delete.pack(padx=5, pady=5, fill="x", side=tk.RIGHT, expand=False)

def settings():
    set_cur_option(3)
    for widget in main_area.winfo_children():
        widget.destroy()

    global entry_app_email, entry_app_password#, selected_theme

    # --------------------------------------
    # email
    frame_app_email = tk.Frame(main_area, bg=MAIN_BG, height=20)
    frame_app_email.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

    label_app_email = tk.Label(frame_app_email, text="E-post", bg=TITLE_BG, fg=TITLE_FG, width=10, font=("TkHeadingFont", 16))
    label_app_email.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)

    entry_app_email = tk.Entry(frame_app_email, bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 16), width=25)
    entry_app_email.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)
    entry_app_email.insert(0, app_email)

    # --------------------------------------
    # password
    frame_app_password = tk.Frame(main_area, bg=MAIN_BG, height=20)
    frame_app_password.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

    label_app_password = tk.Label(frame_app_password, text="App Parool", bg=TITLE_BG, fg=TITLE_FG, width=10, font=("TkHeadingFont", 16))
    label_app_password.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)

    entry_app_password = tk.Entry(frame_app_password, bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 16), show="*", width=25)
    entry_app_password.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)
    entry_app_password.insert(0, app_password)

    show_password_var = tk.BooleanVar(value=False)

    show_password = tk.Checkbutton(frame_app_password, text="Näita", bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 16), relief=tk.FLAT)
    show_password.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)
    show_password.config(    
        variable=show_password_var,
        command=lambda: entry_app_password.config(show="" if show_password_var.get() else "*"),
    )

    # --------------------------------------
    # theme color
    # frame_theme_color = tk.Frame(main_area, bg=MAIN_BG, height=20)
    # frame_theme_color.pack(fill=tk.BOTH, side=tk.TOP, expand=False)

    # label_theme_color = tk.Label(frame_theme_color, text="Teema värv", bg=TITLE_BG, fg=TITLE_FG, width=10, font=("TkHeadingFont", 16))
    # label_theme_color.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)

    # options = ["Must", "Valge"]
    # selected_theme = tk.StringVar(value=options[0])
    # selected_theme.set(app_theme)

    # dropdown = tk.OptionMenu(frame_theme_color, selected_theme, *options)
    # dropdown.config(bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 16), 
    #                 width=10, height=1, 
    #                 relief=tk.FLAT, 
    #                 activebackground=TBB_BG_H, 
    #                 activeforeground=TBB_FG, 
    #                 highlightthickness=2,
    #                 highlightbackground=TB_BG)
    # dropdown["menu"].config(
    #     bg=TBB_BG,
    #     fg=TBB_FG,
    #     activebackground="steelblue",
    #     activeforeground=TBB_FG,
    # )
    # dropdown.pack(padx=5, pady=5, fill="x", side=tk.LEFT, expand=False)

    # --------------------------------------
    # save
    frame_bottom_buttons = tk.Frame(main_area, bg=MAIN_BG, height=20)
    frame_bottom_buttons.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=False)

    but_save = tk.Button(frame_bottom_buttons, text="Salvesta", command=save_settings, bg=TITLE_BG, fg=TITLE_FG, font=("TkDefaultFont", 16), width=15, relief=tk.FLAT)
    but_save.pack(padx=5, pady=5, side=tk.RIGHT, expand=False)

# --------------------------------------
def save_settings():
    settings = {
        "email": entry_app_email.get(),
        "password": entry_app_password.get(),
        #"theme_color": selected_theme.get(),
    }

    with open(TXT_SETTING, "w") as file:
        json.dump(settings, file)

    messagebox.showinfo("Info", "Seaded salvestatud!")

def load_settings():
    global app_email, app_password#, app_theme

    try:
        with open(TXT_SETTING, "r") as file:
            settings = json.load(file)
            app_email = settings["email"]
            app_password = settings["password"]
            #app_theme = settings["theme_color"]
    except:
        pass

def cmd_send_email():
    global app_email, app_password

    save_cur_letter()
    to = cur_letter["to"]
    subject = cur_letter["subject"]
    body = cur_letter["body"]
    
    if not to or not subject or not body:
        messagebox.showwarning("Hoiatus", "Palun täitke kõik väljad.")
        return
    
    emails = cur_letter["to"].strip().split(",")
    for email in emails:
        email = email.strip()
        if not email:
            continue
        if "@" not in email or "." not in email:
            messagebox.showwarning("Hoiatus", f"Vale e-posti aadress: {email}")
            return

    error = False
    try:
        message = EmailMessage()
        message["Subject"] = subject
        message["From"] = app_email
        message["To"] = to
        message.set_content(body)
        
        for file in cur_letter["attachments"]:
            if not os.path.exists(file):
                messagebox.showwarning("Hoiatus", f"Faili ei leitud: {file}")
                return
            
            with open(file, "rb") as f:
                    file_content = f.read()
                    file_name = file.split("/")[-1]
                    message.add_attachment(file_content, maintype="application", subtype="octet-stream", filename=file_name)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
            server.login(app_email, app_password)
            server.send_message(message)

        error = False
        messagebox.showinfo("Info", "Kiri saadetud.")
    except Exception as e:
        messagebox.showerror("Viga", e)
        error = True
        
    cur_letter["sent"] = not error
    log_letter(cur_letter)
    
    if not error:
        for draft_date, draft in app_drafts.items():
            if draft["to"].lower() == cur_letter["to"].lower() and draft["subject"].lower() == cur_letter["subject"].lower():
                delete_draft(draft_date)
                break

    cmd_clear()

def cmd_attach_file():
    file_path = filedialog.askopenfilename()
    if file_path and file_list:
        attached_files.append(file_path)
        file_list.insert(tk.END, file_path)

def cmd_clear():
    entry_to.delete(0, tk.END)
    entry_theme.delete(0, tk.END)
    text_area.delete("1.0", tk.END)
    file_list.delete(0, tk.END)
    attached_files.clear()

# --------------------------------------
def save_draft_letter():
    if cur_letter_readonly:
        return
    
    try:
        if not entry_to.get() or not entry_theme.get() or not text_area.get("1.0", tk.END):
            return
    
        date = str(dt.datetime.now())
        for draft in app_drafts.values():
            if draft["to"] == entry_to.get() and draft["subject"] == entry_theme.get():
                date = draft["date"]

        new_draft = {
            "to": entry_to.get(),
            "subject": entry_theme.get(),
            "body": text_area.get("1.0", tk.END),
            "attachments": attached_files,
            "date": date,
        }
        app_drafts[date] = new_draft

        with open(TXT_DRAFTS, "w") as file:
            json.dump(app_drafts, file)
    except:
        pass

def load_draft_letters():
    try:
        with open(TXT_DRAFTS, "r") as file:
            global app_drafts
            app_drafts = json.load(file)
    except:
        pass
    
def delete_draft(date):
    if date in app_drafts:
        app_drafts.pop(date)
        with open(TXT_DRAFTS, "w") as file:
            json.dump(app_drafts, file)
        drafts()
    else:
        messagebox.showerror("Viga", "Mustandit ei leitud.")

def delete_log_letter(date):
    global app_logs, app_logs2
    if date in app_logs:
        app_logs.pop(date)
        with open(TXT_LOG, "w") as file:
            json.dump(app_logs, file)
        inbox()
    else:
        messagebox.showerror("Viga", "Log fail ei leitud.")
    app_logs2 = app_logs


# --------------------------------------
def load_logs():
    global app_logs, app_logs2
    try:
        with open(TXT_LOG, "r") as file:
            app_logs = json.load(file)
    except:
        pass
    app_logs2 = app_logs

def log_letter(data):
    global app_logs
    try:
        data["date"] = str(dt.datetime.now())
        data["attachments"] = attached_files
        app_logs[data["date"]] = data
        with open(TXT_LOG, "w") as file:
            json.dump(app_logs, file)
    except:
        pass
    
    global app_logs2
    app_logs2 = app_logs

# --------------------------------------
def save_cur_letter():
    if cur_letter_readonly:
        return
    
    if not entry_to or not entry_theme or not text_area:
        return

    global cur_letter

    text = text_area.get("1.0", tk.END)
    if text == "\n":
        text = ""

    letter = {
        "to": entry_to.get(),
        "subject": entry_theme.get(),
        "body": text,
        "attachments": attached_files,
    }
    cur_letter = letter

def open_letter(data: dict, onlyRead: bool = False):
    if not data:
        return

    if cur_option != 0:
        send_letter(False)
        if onlyRead:
            disable_buttons()
    
    insert_letter(data)

def insert_letter(data_to_insert: dict):
    if not data_to_insert:
        return

    entry_to.insert(0, data_to_insert["to"])
    entry_theme.insert(0, data_to_insert["subject"])
    text_area.insert("1.0", data_to_insert["body"])
    attached_files = data_to_insert["attachments"]
    for file in attached_files:
        file_list.insert(tk.END, file)

# --------------------------------------
def on_enter(event):
    event.widget.config(bg=TBB_BG_H)

def on_leave(event):
    event.widget.config(bg=TBB_BG)

cur_option = 0
taskbar_options = [
    ["Kirjuta", "send_letter"],
    ["Mustand", "drafts"],
    ["Saabunud", "inbox"],
    ["Seaded", "settings"]
]

def set_cur_option(index):
    global cur_option
    if cur_option == 0:
        save_draft_letter()
        save_cur_letter()

    cur_option = index

def open_taskbar(option):
    global cur_letter_readonly
    eval(option[1]+"()")
    cur_letter_readonly = False

def create_taskbar():
    taskbar = tk.Frame(window, bg=TB_BG, width=250)
    taskbar.pack(fill=tk.Y, side=tk.LEFT)
    taskbar.pack_propagate(False)

    label_name = tk.Label(taskbar, text="Outlook3000", bg=TITLE_BG, fg=TITLE_FG, font=("TkHeadingFont", 20))
    label_name.pack(padx=5, pady=5, fill="x")

    for option in taskbar_options:
        but_1 = tk.Button(taskbar, text=option[0], command=lambda option=option: open_taskbar(option), bg=TBB_BG, fg=TBB_FG, font=("TkDefaultFont", 16), anchor='w', relief=tk.FLAT)
        but_1.pack(padx=5, pady=5, fill="x")
        but_1.bind("<Enter>", on_enter)
        but_1.bind("<Leave>", on_leave)

# --------------------------------------
create_window()