# --------------------------------------

import customtkinter as ctk
from tkinter import messagebox, colorchooser, filedialog
from CTkColorPicker import *
from PIL import Image, ImageTk
import pygame
import os
import random
import json

# --------------------------------------

#pygame.mixer.init()
#pygame.mixer.music.load("music.mp3")

def play_music():
    #pygame.mixer.music.play(-1)  
    pass

def stop_music():
    #pygame.mixer.music.stop()
    pass

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# --------------------------------------
FACE_PARTS = {
    "Pea": {
        "Puudub": None,
        "Tavaline": "fotorobot/images/base1.png",
        "Karvane": "fotorobot/images/base2.png",
        "Kohev": "fotorobot/images/base3.png",
    },
    "Kõrvad": {
        "Puudub": None,
        "Väikesed": "fotorobot/images/forehead1.png",
        "Karvased": "fotorobot/images/forehead2.png",
        "Kohevad": "fotorobot/images/forehead3.png",
    },
    "Silmad": {
        "Puudub": None,
        "Suured pupillid": "fotorobot/images/eyes1.png",
        "Huvitatud": "fotorobot/images/eyes2.png",
        "Kurjad": "fotorobot/images/eyes3.png",
    },
    "Nina": {
        "Puudub": None,
        "Tavaline": "fotorobot/images/nose1.png",
        "Suur": "fotorobot/images/nose2.png",
        "Väike": "fotorobot/images/nose3.png",
    },
    "Suu": {
        "Puudub": None,
        "Lai": "fotorobot/images/mouth1.png",
        "Keelega": "fotorobot/images/mouth2.png",
        "Suur": "fotorobot/images/mouth3.png",
    },
}

window = None
canvas = None
pictures = {}
objects = {}
parts = {}
bg_label = None
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 550

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400

JSON_PARTS_FILE = "fotorobot/naoosad.json"

# --------------------------------------
def on_close():
    save_parts()
    window.destroy()

def create_window():
    global window
    window = ctk.CTk()
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.resizable(False, False)
    window.title("Näo koostaja nuppudega")
    window.iconbitmap("icon.ico")
    window.protocol("WM_DELETE_WINDOW", on_close)

    os.makedirs("fotorobot/images", exist_ok=True)
    load_parts()

    create_canvas()
    create_buttons()
    
    window.mainloop()

# --------------------------------------
def toggle_part(name, file, x, y):
    global canvas
    if not file:
        pictures[name] = None
        if name in objects:
            canvas.delete(objects[name])
        parts[name] = None
    else:
        if parts.get(name):
            canvas.delete(objects[name])
        
        img = Image.open(file).convert("RGBA").resize((CANVAS_WIDTH, CANVAS_HEIGHT), 1)
        tk_image = ImageTk.PhotoImage(img)
        pictures[name] = tk_image
        objects[name] = canvas.create_image(x, y, image=tk_image)
        parts[name] = file
        
def update_part(part_name, option_name):
    file = FACE_PARTS[part_name][option_name]
    toggle_part(part_name, file, CANVAS_WIDTH/2, CANVAS_HEIGHT/2)
      
def random_parts():
    for face_part, parts in FACE_PARTS.items():
        part = random.choice(list(parts))
        while part == "Puudub":
            part = random.choice(list(parts))

        update_part(face_part, part)
        dropdowns[face_part].set(part)

def ask_face_part():
    selected_part = ctk.CTkInputDialog(text="Sisestage näoosa nimi (nt. Silmad, Nina):", title="Uus näoosa").get_input()
    if not selected_part:
        return None
    
    if selected_part not in FACE_PARTS:
        messagebox.showerror("Viga", f"Näoosa '{selected_part}' ei eksisteeri.")
        return None
    
    return selected_part

def add_face_part():
    selected_part = ask_face_part()
    if not selected_part:
        return
    
    file = filedialog.askopenfile(title="Vali pildifail", filetypes=[("PNG Pildid", "*.png")])
    if not file:
        return
    
    name_part = ctk.CTkInputDialog(text="Sisestage osa nimi:", title="Uus osa").get_input()
    if not name_part:
        return

    if name_part in FACE_PARTS[selected_part]:
        messagebox.showwarning("Hoiatus", f"Osa nimega '{name_part}' on juba olemas!")
        return

    FACE_PARTS[selected_part][name_part] = file.name

    dropdown = dropdowns[selected_part]
    new_values = list(FACE_PARTS[selected_part].keys())
    dropdown.configure(values=new_values)
    dropdown.set(name_part)
    update_part(selected_part, name_part)
    save_parts()

    messagebox.showinfo("Info", f"Osa '{name_part}' lisatud!")

def remove_face_part():
    selected_part = ask_face_part()
    if not selected_part:
        return

    part = ctk.CTkInputDialog(text="Sisestage osa nimi:", title="Kustuta näoosa").get_input()
    if not part:
        return
    
    parts = FACE_PARTS[selected_part]
    for name, file in parts.items():
        if name == part:
            parts.pop(name)

            dropdown = dropdowns[selected_part]
            new_values = list(FACE_PARTS[selected_part].keys())
            dropdown.configure(values=new_values)
            dropdown.set("Puudub")

            update_part(selected_part, "Puudub")
            messagebox.showinfo("Info", f"Osa '{name}' kustutatud!")
            return
            
    messagebox.showwarning("Hoiatus", f"Osa '{part}' ei leitud!")

def save_parts():
    global FACE_PARTS

    with open(JSON_PARTS_FILE, "w", encoding="utf-8") as f:
        json.dump(FACE_PARTS, f, indent=4, ensure_ascii=False)

def load_parts():
    global FACE_PARTS
    try:
        with open(JSON_PARTS_FILE, "r", encoding="utf-8") as f:
            FACE_PARTS = json.load(f)
    except:
        pass
      
# -------------------------------------- 
def save_face():
    dialog_filename = ctk.CTkInputDialog(text="Sisesta faili nimi (ilma laiendita):", title="Salvesta pilt")
    filename = dialog_filename.get_input()
    if not filename:
        return
    
    if bg_filepath and os.path.exists(bg_filepath):
        image_result = Image.open(bg_filepath).convert("RGBA").resize((CANVAS_WIDTH, CANVAS_HEIGHT), 1)
    else:
        image_result = Image.new("RGBA", (CANVAS_WIDTH, CANVAS_HEIGHT), bg_color_code)

    for face_part in FACE_PARTS:
        if parts.get(face_part):
            part = Image.open(parts[face_part]).convert("RGBA").resize((CANVAS_WIDTH, CANVAS_HEIGHT), 1)
            image_result.alpha_composite(part)
    
    try:
        image_result.save(f"fotorobot/{filename}.png")
        messagebox.showinfo("Info", f"Pilt '{filename}.png' salvestatud!")
    except Exception as e:
        messagebox.showerror("Viga", f"{e}")
    
def clear_canvas():
    for face_part in FACE_PARTS:
        update_part(face_part, "Puudub")

    for face_part, dropdown in dropdowns.items():
        dropdown.set("Puudub")
       
# --------------------------------------   
bg_rect = None
bg_filepath = None
bg_color_code = "#ffffff"
bg_image = None
            
def choose_color():
    global bg_label, bg_rect, bg_color_code, bg_filepath
    pick_color = AskColor(title="Valige värv")
    color_code = pick_color.get()

    if bg_rect:
        canvas.delete(bg_rect)
    
    if color_code:
        bg_label.configure(text=f"Valitud värv: {color_code}")
        bg_rect = canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill=color_code)
        canvas.tag_lower(bg_rect)

        bg_filepath = None
        bg_color_code = color_code
        
def choose_background_img():
    global bg_label, bg_rect, bg_image, bg_color_code, bg_filepath
    filepath = filedialog.askopenfile(title="Valige fail", filetypes=[("PNG pildid", "*.png")])

    if filepath and os.path.exists(filepath.name):
        if bg_rect:
            canvas.delete(bg_rect)
            
        img = Image.open(filepath.name).convert("RGBA").resize((CANVAS_WIDTH, CANVAS_HEIGHT), 1)
        tk_image = ImageTk.PhotoImage(img)
        
        bg_rect = canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=tk_image)
        bg_image = tk_image
        canvas.tag_lower(bg_rect)
        
        bg_label.configure(text=f"Valitud fail: {os.path.basename(filepath.name)}")

        bg_filepath = filepath.name
        bg_color_code = None

def clear_bg():
    global bg_image, bg_label, bg_rect
    if bg_rect:
        canvas.delete(bg_rect)
        
    bg_image = None
    bg_label.configure(text=f"Valitud värv: #ffffff")
        
# --------------------------------------     
button_config = {
    "width": 150, "height": 40,
    "font": ("Segoe UI Emoji", 16),
    "text_color": "white",
    "corner_radius": 10,
}

dropdowns = {}

def create_faceparts(pframe):
    global dropdowns
    
    frame = ctk.CTkFrame(pframe)
    frame.pack(side="top", padx=5)
    
    dframe = ctk.CTkFrame(frame)
    dframe.pack(side="left", padx=5, pady=5)
    
    for part_name in FACE_PARTS:
        label = ctk.CTkLabel(dframe, text=part_name.capitalize(), font=("Segoe UI", 14))
        label.pack()

        options = list(FACE_PARTS[part_name].keys())
        var = ctk.StringVar(value=options[0])

        dropdown = ctk.CTkOptionMenu(
            dframe, values=options,
            command=lambda opt, p=part_name: update_part(p, opt),
            variable=var
        )
        dropdown.pack(padx=5, pady=5)
        dropdowns[part_name] = dropdown
        
    bframe = ctk.CTkFrame(frame)
    bframe.pack(side="right", padx=5, pady=5, fill=ctk.BOTH, expand=True)
    
    add_button = ctk.CTkButton(bframe, text="Lisa osa", command=add_face_part, **button_config)
    add_button.pack(side="top", pady=5, padx=5)

    remove_button = ctk.CTkButton(bframe, text="Kustuta osa", command=remove_face_part, **button_config)
    remove_button.pack(side="top", pady=5, padx=5)

    clear_button = ctk.CTkButton(bframe, text="Puhasta", command=clear_canvas, **button_config)
    clear_button.configure(height=30)
    clear_button.pack(side="top", pady=(25, 5), padx=5)

    rand_button = ctk.CTkButton(bframe, text="Juhuslik", command=random_parts, **button_config)
    rand_button.configure(height=30)
    rand_button.pack(side="top", pady=5, padx=5)
            
def create_canvas():
    frame = ctk.CTkFrame(window)
    frame.pack(side="right", padx=(0, 25))
    
    global canvas
    canvas = ctk.CTkCanvas(frame, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
    canvas.configure(highlightthickness=0)
    canvas.pack()
    
    button = ctk.CTkButton(frame, text="Salvesta nägu", command=save_face, **button_config)
    button.pack(pady=10)

def create_background_buttons(pframe):
    frame = ctk.CTkFrame(pframe)
    frame.pack(padx=5, pady=5)
    
    global bg_label
    bg_label = ctk.CTkLabel(frame, text="Valitud värv: #ffffff", width=30, height=4)
    bg_label.pack(pady=5)

    color_button = ctk.CTkButton(frame, text="Taustvärv", command=choose_color)
    color_button.pack(side="left", pady=5, padx=(5, 2))
    
    clear_button = ctk.CTkButton(frame, text="Puhasta", command=clear_bg, width=25)
    clear_button.pack(side="right", pady=5, padx=(2, 5))
    
    image_button = ctk.CTkButton(frame, text="Taustpilt", command=choose_background_img)
    image_button.pack(side="right", pady=5, padx=(2, 2))

def create_buttons():
    frame = ctk.CTkFrame(window)
    frame.pack(side="left", padx=5, pady=5)

    ctk.CTkLabel(frame, text="Vali näoosad", font= ("Segoe UI Emoji", 50), corner_radius=10).pack(pady=5)
    
    create_faceparts(frame)
    create_background_buttons(frame)

    frame_mus = ctk.CTkFrame(frame)
    frame_mus.pack(side="bottom", padx=5, pady=5, fill=ctk.BOTH, expand=True)

    button_mus = ctk.CTkButton(frame_mus, text="Mängi muusikat", command=play_music)
    button_mus.pack(side="left", padx=(5, 2), pady=5, fill=ctk.BOTH, expand=True)

    button_stop_mus = ctk.CTkButton(frame_mus, text="Peata muusika", command=stop_music)
    button_stop_mus.pack(side="right", padx=(2, 5), pady=5, fill=ctk.BOTH, expand=True)
    
create_window()