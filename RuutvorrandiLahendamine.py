# --------------------------------------
# Töö 8.3 Ruutvõrrandi lahendamine
# --------------------------------------

import tkinter as tk
from turtle import bgcolor
import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------
window = None
entry_a = None
entry_b = None
entry_c = None
label_result = None

entry_bg = "lightgray"
entry_fg = "darkgreen"
label_bg = "darkgray"

def is_entry_data_valid():
    valid = True
    for entry in (entry_a, entry_b, entry_c):
        try:
            float(entry.get())
            entry.config(bg=entry_bg)
        except:
            entry.config(bg="red")
            valid = False
    
    return valid

def solve():
    if not is_entry_data_valid():
        label_result.config(text="Valed andmed")
        return

    a, b, c = float(entry_a.get()), float(entry_b.get()), float(entry_c.get())

    D = b**2 - 4 * a * c

    if D < 0:
        result = "Puuduvad tegelikud juured"
    elif D == 0:
        x = -b / (2 * a)
        result = f"Üks juur: {round(x,3)}"
    else:
        sqrt_D = D**0.5
        x1 = (-b + sqrt_D) / (2 * a)
        x2 = (-b - sqrt_D) / (2 * a)
        result = f"D = {round(D, 2)}\n X1 = {round(x1, 2)}\n X2 = {round(x2, 2)}"

    label_result.config(text=result)

def graph():
    if not is_entry_data_valid():
        label_result.config(text="Valed andmed")
        return

    a, b, c = float(entry_a.get()), float(entry_b.get()), float(entry_c.get())

    vx = -b / (2 * a)
    xs = np.linspace(vx - 10, vx + 10, 100)
    ys = a * xs**2 + b * xs + c

    plt.figure()
    plt.plot(xs, ys)

    D = b**2 - 4 * a * c
    if D >= 0:
        sqrt_D = D**0.5
        x1 = (-b + sqrt_D) / (2 * a)
        x2 = (-b - sqrt_D) / (2 * a)
        plt.plot([x1, x2], [0, 0], "go", markersize=8)

    plt.title("Paraboola")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)
    plt.show()

# --------------------------------------
def create_result():
    global label_result
    label_result = tk.Label(
        window,
        text="Vastus",
        bg="gray",
        font=("Arial", 16),
        fg="white"
    )
    label_result.place(
        x=5, 
        y=105, 
        width=WINDOW_WIDTH-10, 
        height=WINDOW_HEIGHT-110
    )

def create_buttons():
    btn_solve = tk.Button(
        window,
        text="Lahenda",
        command=solve,
        bg="#008800",
        fg="white",
        font=("Arial", 14)
    ).place(
        x=5, 
        y=70, 
        width=80, 
        height=30
    )

    btn_graph = tk.Button(
        window,
        text="Graafik",
        bg="#008800",
        fg="white",
        font=("Arial", 14),
        command=graph
    ).place(
        x=90, 
        y=70, 
        width=80, 
        height=30
    )


# --------------------------------------
def on_focus_in(event):
    event.widget.config(bg="wheat")
    
def on_focus_out(event):
    event.widget.config(bg=entry_bg)

def create_entry():
    base_x = WINDOW_WIDTH/4
    global entry_a, entry_b, entry_c

    # a*x^2
    entry_a = tk.Entry(window, width=3,bg=entry_bg, fg=entry_fg, font=("Arial", 18))
    entry_a.place(
        x=5+(base_x), 
        y=35, 
        width=50, 
        height=30
    )

    tk.Label(window, text="x**2+", font=("Arial", 14), bg=label_bg, fg=entry_fg).place(
        x=55+(base_x), 
        y=35, 
        width=60, 
        height=30
    )

    # b*x
    entry_b = tk.Entry(window, width=3,bg=entry_bg, fg=entry_fg, font=("Arial", 18))
    entry_b.place(
        x=110+(base_x), 
        y=35, 
        width=50, 
        height=30
    )

    tk.Label(window, text="x+", font=("Arial", 14), bg=label_bg, fg=entry_fg).place(
        x=160+(base_x), 
        y=35, 
        width=30, 
        height=30
    )

    # # c
    entry_c = tk.Entry(window, width=3,bg=entry_bg, fg=entry_fg, font=("Arial", 18))
    entry_c.place(
        x=190+(base_x), 
        y=35, 
        width=50, 
        height=30
    )

    tk.Label(window, text="=0", font=("arial", 14), bg=label_bg, fg=entry_fg).place(
        x=240+(base_x), 
        y=35, 
        width=30, 
        height=30
    )

    entry_a.bind("<FocusIn>", on_focus_in)
    entry_b.bind("<FocusIn>", on_focus_in)
    entry_c.bind("<FocusIn>", on_focus_in)    
    
    entry_a.bind("<FocusOut>", on_focus_out)
    entry_b.bind("<FocusOut>", on_focus_out)
    entry_c.bind("<FocusOut>", on_focus_out)

# --------------------------------------
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 200

def create_window():
    window = tk.Tk()
    window.title("Kvadraatilised võrrandid")
    window.resizable(width=False, height=False)
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.iconbitmap("icon.ico")

    header = tk.Label(
        window,
        text="Kvadraatilise võrrandi lahendamine",
        bg="gray",
        fg="white",
        font=("Arial", 20)
    )
    header.place(x=0, y=0, width=WINDOW_WIDTH, height=30)

    create_entry()
    create_buttons()
    create_result()

    window.mainloop()

create_window()