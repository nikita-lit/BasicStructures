import customtkinter as ctk
from tkinter import simpledialog, Canvas, messagebox, colorchooser
from PIL import Image, ImageTk
import pygame

#pygame.mixer.init()
#pygame.mixer.music.load("music.mp3")

def play_music():
    pygame.mixer.music.play(-1)  
def stop_music():
    pygame.mixer.music.stop()

ctk.set_appearance_mode("dark")

window = ctk.CTk()
window.geometry("800x500")
window.resizable(False, False)
window.title("Näo koostaja nuppudega")
window.iconbitmap("icon.ico")

canvas = Canvas(window, width=400, height=400, bg="white")
canvas.pack(side="right", padx=10, pady=10)

face_parts = ["base", "forehead", "eyes", "nose", "mouth"]
pictures = {}
objects = {}
parts = {}
color_label = None

def toggle_part(name, file, x, y):
    if parts.get(name):
        canvas.delete(objects[name])
        parts[name] = False
    else:
        img = Image.open(file).convert("RGBA").resize((400, 400), 1)
        tk_image = ImageTk.PhotoImage(img)
        pictures[name] = tk_image
        objects[name] = canvas.create_image(x, y, image=tk_image)
        parts[name] = True
        
def save_face():
    filename = simpledialog.askstring("Salvesta pilt", "Sisesta faili nimi (ilma laiendita):")
    if not filename:
        return
    
    image_result = Image.new("RGBA", (400, 400), (255, 255, 255, 255))
    
    for name in face_parts:
        if parts.get(name):
            file_path = {
                "base": "fotorobot/images/base1.png",
                "forehead": "fotorobot/images/forehead1.png",
                "eyes": "fotorobot/images/eyes1.png",
                "nose": "fotorobot/images/nose1.png",
                "mouth": "fotorobot/images/mouth1.png",
            }.get(name)
            if file_path:
                part = Image.open(file_path).convert("RGBA").resize((400, 400), 1)
                image_result.alpha_composite(part)
            
    image_result.save(f"{filename}.png")
    messagebox.showinfo("Info", f"Pilt {filename}.png salvestatud!")
            
bg_rect = None

def choose_color():
    color_code = colorchooser.askcolor(title="Choose a color")[1]
    
    if color_code:
        color_label.configure(text=f"Selected Color: {color_code}", bg=color_code)
        canvas.create_rectangle(0, 0, 400, 400, fill=color_code)
            
toggle_part("base", "fotorobot/images/base1.png", 200, 200)
parts["base"] = True
    
frame = ctk.CTkFrame(window)
frame.pack(side="left", padx=10, pady=10)
button_config = {
    "width": 150, "height": 40,
    "font": ("Segoe UI Emoji", 16),
    "fg_color": "#4CAF50",
    "text_color": "white",
    "corner_radius": 10,
}

ctk.CTkLabel(frame, text="Vali näoosad", bg_color="gray50", font= ("Segoe UI Emoji", 50), corner_radius=10).pack(pady=5)
ctk.CTkButton(frame, text="🧢 Otsmik", command=lambda: toggle_part("forehead", "fotorobot/images/forehead2.png", 200, 200), **button_config).pack(pady=5)
ctk.CTkButton(frame, text="👀 Silmad", command=lambda: toggle_part("eyes", "fotorobot/images/eyes2.png", 200, 200), **button_config).pack(pady=5)
ctk.CTkButton(frame, text="👃 Nose", command=lambda: toggle_part("nose", "fotorobot/images/nose1.png", 200, 200), **button_config).pack(pady=5)
ctk.CTkButton(frame, text="👄 Suu", command=lambda: toggle_part("mouth", "fotorobot/images/mouth2.png", 200, 200), **button_config).pack(pady=5)

color_label = ctk.CTkLabel(frame, text="Selected Color: None", width=30, height=4)
color_label.pack(pady=20)

color_button = ctk.CTkButton(frame, text="Pick a Color", command=choose_color)
color_button.pack(pady=10)

button = ctk.CTkButton(frame, text="Salvesta nägu", command=save_face, **button_config)
button.pack(pady=10)

frame_mus = ctk.CTkFrame(frame)
frame_mus.pack(side="bottom", padx=10, pady=10)

button_mus = ctk.CTkButton(frame_mus, text="Mängi muusikat", command=play_music, fg_color="#4CAF50")
button_mus.pack(side="left", padx=10, pady=10)

button_stop_mus = ctk.CTkButton(frame_mus, text="Peata muusika", command=stop_music, fg_color="#4CAF50")
button_stop_mus.pack(side="left", padx=10, pady=10)

window.mainloop()