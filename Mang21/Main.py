# --------------------------------------
# Praktiline iseseisevtöö "Wordle graafilise kujundiga"
# --------------------------------------

import tkinter as tk
from PIL import Image, ImageTk

# --------------------------------------

window = None
main_frame = None
tbl_canvas = None
players = {}

PLAYER_NUM = 5
BOT_COUNT = (PLAYER_NUM-1)
MAN_FACE_SIZE = (128, 128)

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 600
DISTANCE_BETWEEN_PLAYERS = WINDOW_WIDTH / PLAYER_NUM
# --------------------------------------
def on_close():
    window.destroy() 

def create_window():
    global window, main_frame
    
    window = tk.Tk()
    window.title("Mang")
    window.resizable(width=False, height=False)
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.iconbitmap("icon.ico")
    window.grid_columnconfigure(1, weight=1)
    window.protocol("WM_DELETE_WINDOW", on_close)
    
    main_frame = tk.Frame(window)
    main_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    
    create_menu()
    #create_table()
    
    #canvas = tk.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    #canvas.pack()
    
    #image = tk.PhotoImage(file="mang21/images/cat1.png")
    #circle = canvas.create_image(0, 0, anchor=tk.NW, image=image)
    
    window.mainloop()
    
def create_menu():
    frame_menu = tk.Frame(main_frame)
    frame_menu.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    
    width, height = 250, 60

    but_start = tk.Button(frame_menu, text="Alusta", command=create_table)
    but_start.config(bg="green", fg="white")
    but_start.place(x=(WINDOW_WIDTH/2)-(width/2), y=(WINDOW_HEIGHT/2), width=width, height=height)
    
    but_exit = tk.Button(frame_menu, text="Välju", command=on_close)
    but_exit.config(bg="red", fg="white")
    but_exit.place(x=(WINDOW_WIDTH/2)-(width/2), y=(WINDOW_HEIGHT/1.5), width=width, height=height)

def create_table():
    for widget in main_frame.winfo_children():
        widget.destroy()
        
    global tbl_canvas

    tbl_canvas = tk.Canvas(main_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    tbl_canvas.pack()
    tbl_canvas.players_imgs = []
    
    img = Image.open("mang21/images/table.png")
    img = img.resize((WINDOW_WIDTH, WINDOW_HEIGHT), 1)
    tk_image = ImageTk.PhotoImage(img)
    
    tbl_canvas.create_image(0, 0, image=tk_image, anchor=tk.NW)
    tbl_canvas.table_img = tk_image
    
    for num, data in players.items():
        create_player(num, data)
    
    create_dealer()
    
def create_player(num: int, data: dict):
    global tbl_canvas
    
    name = data["name"]
    isbot = data["isbot"]
    
    img = Image.open("mang21/images/man_face.png")
    img = img.resize(MAN_FACE_SIZE, 1)
    tk_image = ImageTk.PhotoImage(img)
    
    player_image = tbl_canvas.create_image((DISTANCE_BETWEEN_PLAYERS*num)+(DISTANCE_BETWEEN_PLAYERS/2)-(MAN_FACE_SIZE[0]/2), WINDOW_HEIGHT-200, image=tk_image, anchor=tk.NW)
    tbl_canvas.players_imgs.insert(num, tk_image)
    
    tbl_canvas.create_text(
        (DISTANCE_BETWEEN_PLAYERS*num)+(DISTANCE_BETWEEN_PLAYERS/2),
        WINDOW_HEIGHT-50, 
        text=name, font=("Arial", 16), fill="white")
    
def create_dealer():
    global tbl_canvas
    
    img = Image.open("mang21/images/man_face.png")
    img = img.resize(MAN_FACE_SIZE, 1)
    tk_image = ImageTk.PhotoImage(img)
    
    dealer_image = tbl_canvas.create_image((WINDOW_WIDTH/2)-(MAN_FACE_SIZE[0]/2), 0, image=tk_image, anchor=tk.NW)
    tbl_canvas.dealer_img = tk_image
    
    tbl_canvas.create_text(
        (WINDOW_WIDTH/2),
        140,
        text="Diiler", font=("Arial", 16), fill="white")

# --------------------------------------
def register_player(num: int, name: str, isBot: bool):
    global players
    
    if len(players) < PLAYER_NUM:
        players[num] = {"isbot": isBot, "name": name}
        return True
    else:
        return False

bot_count = BOT_COUNT
for i in range(PLAYER_NUM):
    bot_count -= 1
    if bot_count >= 0:
        register_player(i, f"Bot {i+1}", True)
    else:
        register_player(i, f"Mängija {i+1}", False)

# --------------------------------------
create_window()