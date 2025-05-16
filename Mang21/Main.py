# --------------------------------------
# Praktiline iseseisevtöö "Wordle graafilise kujundiga"
# --------------------------------------

import tkinter as tk
import random
import time
from PIL import Image, ImageTk

# --------------------------------------
window = None
main_frame = None
tbl_canvas = None

but_start = None

arrow = None
but_get_card = None
but_stay = None

# --------------------------------------
# game
players = {}
game_started = False
cur_player = -1

# --------------------------------------
# consts
PLAYER_NUM = 5
BOT_COUNT = (PLAYER_NUM-1)
MAN_FACE_SIZE = (128, 128)

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 800
DISTANCE_BETWEEN_PLAYERS = WINDOW_WIDTH / PLAYER_NUM

# --------------------------------------
# cards 

CARDS = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": 11,
}

def count_points(cards):
    points = 0
    aces = 0
    for card in cards:
        points += CARDS[card]
        if card == 'A':
            aces += 1
    while points > 21 and aces:
        points -= 10
        aces -= 1
    return points

# --------------------------------------
def on_close():
    window.destroy() 

def create_window():
    global window, main_frame
    
    window = tk.Tk()
    window.title("Mang21")
    window.resizable(width=False, height=False)
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.iconbitmap("icon.ico")
    window.grid_columnconfigure(1, weight=1)
    window.protocol("WM_DELETE_WINDOW", on_close)
    
    main_frame = tk.Frame(window)
    main_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
    
    #create_menu()
    create_table()
    
    window.mainloop()
    
def create_menu():
    global tbl_canvas
    tbl_canvas = tk.Canvas(main_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    tbl_canvas.pack()

    img = Image.open("mang21/images/wallpaper.png")
    img = img.resize((WINDOW_WIDTH, WINDOW_HEIGHT), 1)
    tk_image = ImageTk.PhotoImage(img)

    tbl_canvas.create_image(0, 0, image=tk_image, anchor=tk.NW)
    tbl_canvas.table_img = tk_image
    
    width, height = 250, 60
    but_start = tk.Button(tbl_canvas, text="Alusta", command=create_table)
    but_start.config(bg="green", fg="white")
    but_start.place(x=(WINDOW_WIDTH/2)-(width/2), y=(WINDOW_HEIGHT/2), width=width, height=height)
    
    but_exit = tk.Button(tbl_canvas, text="Välju", command=on_close)
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
    
    for num in players:
        create_player(num)
    
    create_dealer()
    update_score()

    global but_start
    but_start = tk.Button(tbl_canvas, text="Alusta", command=lambda: start_game())
    but_start.config(bg="white", fg="black", font=("Arial", 14))
    but_start.place(x=(WINDOW_WIDTH/2)-(100/2), y=WINDOW_HEIGHT-50, width=100, height=40)

    
def create_player(num: int):
    global tbl_canvas, players
    
    data = players[num]
    name = data["name"]
    isbot = data["isbot"]
    
    img = Image.open("mang21/images/man_face.png")
    img = img.resize(MAN_FACE_SIZE, 1)
    tk_image = ImageTk.PhotoImage(img)
    
    player_image = tbl_canvas.create_image((DISTANCE_BETWEEN_PLAYERS*num)+(DISTANCE_BETWEEN_PLAYERS/2)-(MAN_FACE_SIZE[0]/2), WINDOW_HEIGHT-240, image=tk_image, anchor=tk.NW)
    tbl_canvas.players_imgs.insert(num, tk_image)
    
    players[num]["pos"] = ((DISTANCE_BETWEEN_PLAYERS*num)+(DISTANCE_BETWEEN_PLAYERS/2), WINDOW_HEIGHT-100)
    pos = players[num]["pos"]

    tbl_canvas.create_text(
        pos[0],
        pos[1], 
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
    
def create_buttons():
    global tbl_canvas, players, cur_player, but_get_card, but_stay
    
    delete_buttons()

    pos = players[cur_player]["pos"]

    but_get_card = tk.Button(tbl_canvas, text="Võta kaart", command=lambda: get_card())
    but_get_card.config(bg="white", fg="black", font=("Arial", 14))
    but_get_card.place(x=(WINDOW_WIDTH/2)-(120/2), y=170, width=120, height=30)

    but_stay = tk.Button(tbl_canvas, text="Ära võta", command=lambda: stay())
    but_stay.config(bg="white", fg="black", font=("Arial", 14))
    but_stay.place(x=(WINDOW_WIDTH/2)-(120/2), y=WINDOW_HEIGHT-40, width=120, height=30)
    
def delete_buttons():
    global tbl_canvas, arrow, but_get_card, but_stay

    if but_get_card:
        but_get_card.destroy()
        but_stay.destroy()
        
def create_arrow():
    global tbl_canvas, players, cur_player, arrow
    
    pos = players[cur_player]["pos"]
    
    if arrow:
        tbl_canvas.delete(arrow)
    
    arrow = tbl_canvas.create_text(
        pos[0],
        pos[1]+40,
        text="↑", font=("Arial", 26), fill="white")
    
def create_card(cards: dict, player_num: int):
    global tbl_canvas, players
    
    for card_p in players[player_num]["cards_p"]:
        card_p["panel"].destroy()
    
    players[player_num]["cards_p"].clear()
    
    vertical_offset = 0
    horizontal_offset = 0
    card_width = 40
    card_height = 50
    spacing = 35
    cards_in_row = 0
    max_cards_per_row = 6
    
    for key, card in enumerate(cards):
        img = Image.open(f"mang21/images/cards/{card}.png")
        img = img.resize((card_width, card_height), 1)
        tk_image = ImageTk.PhotoImage(img)

        player_pos = players[player_num]["pos"]
        pos = (player_pos[0] + 50 + horizontal_offset, player_pos[1] - 220 - vertical_offset)
        
        card_panel = tk.Frame(tbl_canvas, bg="white", bd=2, relief=tk.RAISED)
        card_panel.place(x=pos[0], y=pos[1])

        card_image = tk.Label(card_panel, image=tk_image, bg="white")
        card_image.pack()

        card_name = tk.Label(card_panel, text=card, bg="white", font=("Arial", 10))
        card_name.pack()

        card_p = {
            "card": card,
            "pos": (pos[0], pos[1]),
            "panel": card_panel,
            "img": tk_image,
        }

        players[player_num]["cards_p"].append(card_p)

        cards_in_row += 1

        if cards_in_row >= max_cards_per_row:
            vertical_offset = 0
            horizontal_offset -= card_width + spacing
            cards_in_row = 0
        else:
            vertical_offset += card_height + spacing

scores_texts = []

def update_score():
    global players, scores_texts, tbl_canvas
    
    for text in scores_texts:
        tbl_canvas.delete(text)
    
    for key, data in players.items():
        score = count_points(data["cards"])
        players[key]["score"] = score
        
        if data["isbot"]:
            score = "?"
        
        pos = data["pos"]
        text = tbl_canvas.create_text(
            pos[0],
            pos[1] + 20,
            text=f"Skoor: {score}", font=("Arial", 12), fill="white")
        
        scores_texts.append(text)
    

# --------------------------------------
# game

def start_game():
    global game_started, cur_player, but_start, players
    
    if not game_started:
        game_started = True

    but_start.destroy()
    next_player()
    
def ask_player():
    if players[cur_player]["isbot"]:
        window.after(2000, bot_turn)
    else:
        create_buttons()


def bot_turn():
    bot_cards = players[cur_player]["cards"]
    bot_score = count_points(bot_cards)

    if bot_score < 17:
        get_card()
    elif bot_score >= 17 and bot_score < 21:
        if random.randint(0, 100) < 30:
            get_card()
        else:
            stay()
    else:
        stay()

def get_card():
    global cur_player, players
    
    player = players[cur_player]
    cards = list(CARDS.keys())
    
    if player["isbot"]:
        player["cards"].append(random.choice(cards))
        create_card(player["cards"], cur_player)
        update_score()
    else:
        player["cards"].append(random.choice(cards))
        create_card(player["cards"], cur_player)
        update_score()
        
    delete_buttons()
    next_player()

def stay():
    delete_buttons()
    next_player()

def next_player():
    global cur_player
    
    if cur_player < PLAYER_NUM-1:
        cur_player += 1
    else:
        cur_player = 0

    create_arrow()
    ask_player()

# --------------------------------------
def register_player(num: int, name: str, isBot: bool):
    global players
    
    if len(players) < PLAYER_NUM:
        players[num] = {"isbot": isBot, "name": name, "score": 0, "cards": [], "cards_p": []}
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