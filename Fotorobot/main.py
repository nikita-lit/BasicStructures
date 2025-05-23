import customtkinter as ctk
from tkinter import messagebox, colorchooser, filedialog
from CTkColorPicker import *
from PIL import Image, ImageTk
import pygame
import os

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

FACE_PARTS = {
    #müts
    "Nägu": {
        "Puudub": None,
        "Face1": "fotorobot/images/base1.png",
        "Face2": "fotorobot/images/base2.png",
    },
    "Kõrvad": {
        "Puudub": None,
        "Ears1": "fotorobot/images/forehead1.png",
        "Ears2": "fotorobot/images/forehead2.png",
    },
    "Silmad": {
        "Puudub": None,
        "Eyes1": "fotorobot/images/eyes1.png",
        "Eyes2": "fotorobot/images/eyes2.png",
    },
    "Nina": {
        "Puudub": None,
        "Nose1": "fotorobot/images/nose1.png",
        "Nose2": "fotorobot/images/nose2.png",
    },
    "Suu": {
        "Puudub": None,
        "Mouth1": "fotorobot/images/mouth1.png",
        "Mouth2": "fotorobot/images/mouth2.png",
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

def create_window():
    window = ctk.CTk()
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.resizable(False, False)
    window.title("Näo koostaja nuppudega")
    window.iconbitmap("icon.ico")

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
    pass
      
# -------------------------------------- 
def save_face():
    dialog_filename = ctk.CTkInputDialog(text="Sisesta faili nimi (ilma laiendita):", title="Salvesta pilt")
    filename = dialog_filename.get_input()
    if not filename:
        return
    
    image_result = Image.new("RGBA", (CANVAS_WIDTH, CANVAS_HEIGHT), (255, 255, 255, 255))
    
    for face_part in FACE_PARTS:
        if parts.get(face_part):
            part = Image.open(parts[face_part]).convert("RGBA").resize((CANVAS_WIDTH, CANVAS_HEIGHT), 1)
            image_result.alpha_composite(part)
            
    image_result.save(f"fotorobot/pildid/{filename}.png")
    messagebox.showinfo("Info", f"Pilt {filename}.png salvestatud!")
    
def clear_canvas():
    for face_part in FACE_PARTS:
        update_part(face_part, "Puudub")
       
# --------------------------------------   
bg_rect = None
bg_image = None
            
def choose_color():
    global bg_label, bg_rect
    pick_color = AskColor(title="Valige värv")
    color_code = pick_color.get()

    if bg_rect:
        canvas.delete(bg_rect)
    
    if color_code:
        bg_label.configure(text=f"Valitud värv: {color_code}")
        bg_rect = canvas.create_rectangle(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, fill=color_code)
        canvas.tag_lower(bg_rect)
        
def choose_background_img():
    global bg_label, bg_rect, bg_image
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

dropdowns = []

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
        dropdowns.append(dropdown)
        
    bframe = ctk.CTkFrame(frame)
    bframe.pack(side="right", padx=5)
    
    clear_button = ctk.CTkButton(bframe, text="Puhasta", command=clear_canvas, **button_config)
    clear_button.pack(side="top", pady=5, padx=5)
            
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