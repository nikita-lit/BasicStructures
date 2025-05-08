# --------------------------------------
# Praktiline töö: "E-posti klient Minu Oma Outlook"
# --------------------------------------

import tkinter as tk

# --------------------------------------

window = None
send_letter_frame = None
taskbar = None
titles = None

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600
TITLE_BG = "deep sky blue"
TITLE_FG = "white"
ENTRY_BG = "lightgray"
ENTRY_FG = "black"

LETTER_FRAME_WIDTH = (WINDOW_WIDTH-105)
LETTER_FRAME_HEIGHT = (WINDOW_HEIGHT-55)

def create_window():
    global window, send_letter_frame

    window = tk.Tk()
    window.title("Outlook3000")
    window.resizable(width=False, height=False)
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.iconbitmap("icon.ico")

    taskbar = tk.Frame(window, bg="gray85")
    taskbar.place(
        x=0, 
        y=0, 
        width=WINDOW_WIDTH, 
        height=50
    )   

    send_letter_frame = tk.Frame(window)
    send_letter_frame.place(
        x=100, 
        y=50, 
        width=LETTER_FRAME_WIDTH, 
        height=LETTER_FRAME_HEIGHT
    )

    create_titles()
    #create_entries()

    window.mainloop()

def create_titles():
    base_y = 5

    titles = tk.Frame(send_letter_frame, width=160, height=LETTER_FRAME_HEIGHT, bg="wheat")
    titles.place(
        x=0, 
        y=0, 
        width=160, 
        height=LETTER_FRAME_HEIGHT
    )
    titles.grid_columnconfigure(0, weight=1)

    tk.Label(titles, text="EMAIL: ", font=("arial", 25), bg=TITLE_BG, fg=TITLE_FG).grid(
        row=0, column=0, sticky="wn", padx=5, pady=5
    )    
    
    tk.Label(titles, text="TEMA: ", font=("arial", 25), bg=TITLE_BG, fg=TITLE_FG).grid(
        row=1, column=0, sticky="wn", padx=5, pady=5
    )    
    
    tk.Label(titles, text="KIRI: ", font=("arial", 25), bg=TITLE_BG, fg=TITLE_FG).grid(
        row=2, column=0, sticky="wn", padx=5, pady=5
    )

    #base_y += 45
    
    # tk.Label(titles, text="TEMA: ", font=("arial", 25), bg=TITLE_BG, fg=TITLE_FG).place(
    #     x=5, 
    #     y=base_y, 
    #     width=150, 
    #     height=40
    # )
    # base_y += 45

    # tk.Label(titles, text="KIRI: ", font=("arial", 25), bg=TITLE_BG, fg=TITLE_FG).place(
    #     x=5, 
    #     y=base_y, 
    #     width=150, 
    #     height=40
    # )
    # base_y += LETTER_FRAME_HEIGHT + 5

    # tk.Label(titles, text="LISA: ", font=("arial", 25), bg=TITLE_BG, fg=TITLE_FG).place(
    #     x=5, 
    #     y=base_y, 
    #     width=150, 
    #     height=40
    # )    

def create_entries():
    base_x = 160
    base_y = 5
    
    entries = tk.Frame(send_letter_frame, bg="black")

    email_entry = tk.Entry(entries, width=3, bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 18))
    email_entry.place(
        x=base_x, 
        y=base_y, 
        width=entries.winfo_width(), 
        height=40
    )  
    base_y += 45
    
    tema_entry = tk.Entry(entries, width=3,bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 18))
    tema_entry.place(
        x=base_x, 
        y=base_y, 
        width=WINDOW_WIDTH-215, 
        height=40
    )    
    base_y += 45

    letter_entry = tk.Text(entries,bg=ENTRY_BG, fg=ENTRY_FG, font=("Arial", 18))
    letter_entry.place(
        x=base_x, 
        y=base_y, 
        width=LETTER_FRAME_WIDTH-160, 
        height=LETTER_FRAME_HEIGHT-150
    )

    base_y += LETTER_FRAME_HEIGHT + 5

    attachment = tk.Label(entries, text="C:/Users/opilane/source/repos/BasicStructures", font=("arial", 15), bg=ENTRY_BG, fg=ENTRY_FG)
    attachment.place(
        x=base_x, 
        y=base_y, 
        width=WINDOW_WIDTH-215,  
        height=40
    )


create_window()