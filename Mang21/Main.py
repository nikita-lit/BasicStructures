# --------------------------------------
# Praktiline iseseisevtöö "Wordle graafilise kujundiga"
# --------------------------------------

import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

from PIL import Image, ImageTk
from conts import *
import random
import json

ctk.set_appearance_mode("dark")

# --------------------------------------
window = None
main_frame = None
tbl_canvas = None
money_text = None

but_start = None
but_back = None

arrow = None
but_get_card = None
but_stay = None

# --------------------------------------
def on_close():
    cancel_bet()
    save_data()
    window.destroy() 

def create_window():
    global window, main_frame
    
    window = ctk.CTk()
    window.title("Mang21")
    window.resizable(width=False, height=False)
    window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    window.iconbitmap("icon.ico")
    window.grid_columnconfigure(1, weight=1)
    window.protocol("WM_DELETE_WINDOW", on_close)
    
    main_frame = ctk.CTkFrame(window)
    main_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    load_data()
    
    create_menu()
    #create_table()
    
    window.mainloop()
    
# --------------------------------------
def create_menu():
    for widget in main_frame.winfo_children():
        widget.destroy()

    reset_game()

    global tbl_canvas
    tbl_canvas = ctk.CTkCanvas(main_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    tbl_canvas.configure(highlightthickness=0)
    tbl_canvas.pack()

    img = Image.open("mang21/images/wallpaper.png")
    img = img.resize((WINDOW_WIDTH, WINDOW_HEIGHT), 1)
    tk_image = ImageTk.PhotoImage(img)

    tbl_canvas.create_image(0, 0, image=tk_image, anchor=tk.NW)
    tbl_canvas.table_img = tk_image

    button_config = {
        "width": 250, "height": 60,
        "font": ("Arial", 22),
        "text_color": "white",
        "corner_radius": 0,
    }
    
    but_start = ctk.CTkButton(tbl_canvas, text="Alusta", command=create_table, **button_config)
    but_start.configure(fg_color="green")
    but_start.place(x=(WINDOW_WIDTH/2)-(250/2), y=250)

    but_history = ctk.CTkButton(tbl_canvas, text="Ajalugu", command=show_history, **button_config)
    but_history.configure(fg_color="green")
    but_history.place(x=(WINDOW_WIDTH/2)-(250/2), y=340)
    
    but_exit = ctk.CTkButton(tbl_canvas, text="Välju", command=on_close, **button_config)
    but_exit.configure(fg_color="red")
    but_exit.place(x=(WINDOW_WIDTH/2)-(250/2), y=430)

    title = tbl_canvas.create_text(
        (WINDOW_WIDTH/2),
        150, 
        text="Blackjack", font=("Arial", 36), fill="white")
    
    create_money_count()
    
# --------------------------------------
money_text = None
money_text2 = None

def create_money_count():
    global money_text, money_text2
    if money_text:
        tbl_canvas.delete(money_text)
    if money_text2:
        tbl_canvas.delete(money_text2)

    money_text = tbl_canvas.create_text(
        120,
        25, 
        text="Raha: "+"${:,.2f}".format(money), font=("Arial", 22), fill="white")
    
    if bet > 0:
        money_text2 = tbl_canvas.create_text(
            120,
            65, 
            text="Panus: "+"${:,.2f}".format(bet), font=("Arial", 22), fill="white")

def create_table():
    for widget in main_frame.winfo_children():
        widget.destroy()
        
    register_players()
        
    global tbl_canvas, money_text
    tbl_canvas = ctk.CTkCanvas(main_frame, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    tbl_canvas.configure(highlightthickness=0)
    tbl_canvas.pack()
    tbl_canvas.players_imgs = []
    
    img = Image.open("mang21/images/table.png")
    img = img.resize((WINDOW_WIDTH, WINDOW_HEIGHT), 1)
    tk_image = ImageTk.PhotoImage(img)
    
    tbl_canvas.create_image(0, 0, image=tk_image, anchor=tk.NW)
    tbl_canvas.table_img = tk_image

    create_money_count()
    
    for num in players:
        create_player(num, "mang21/images/man_face.png")
    
    ask_bet()

# --------------------------------------
def ask_bet():
    button_config = {
        "width": 120, "height": 40,
        "font": ("Arial", 20),
        "fg_color": "white",
        "text_color": "black",
        "hover": False,
        "corner_radius": 0,
    }

    dialog = ctk.CTkInputDialog(text="Sisestage panus:", title="Panus")
    dialog_bet = dialog.get_input()
    if dialog_bet:
        try:
            if int(dialog_bet) < 100:
                messagebox.showinfo("Info", "Panus on liiga väike, miinimum on 100$.")
                back_to_menu()
                return
            
            if money <= 0:
                messagebox.showinfo("Info", "Teil ei ole piisavalt raha.")
                back_to_menu()
                return
            
            global bet
            bet = int(dialog_bet)
            print(f"Panus: {bet}")
            make_bet(bet)

            create_money_count()

            global but_start
            but_start = ctk.CTkButton(tbl_canvas, text="Alusta", command=lambda: start_game(), **button_config)
            but_start.place(x=(WINDOW_WIDTH/2)-(120/2), y=WINDOW_HEIGHT-50)

            create_back_to_menu()
            update_score()
        except ValueError:
            if messagebox.showinfo("Info", "Vale sisend, panus peab olema number."):
                ask_bet()
    else:
        back_to_menu()

# --------------------------------------
button1_config = {
    "width": 150, "height": 40,
    "font": ("Arial", 25),
    "fg_color": "white",
    "text_color": "black",
    "hover": False,
    "corner_radius": 0,
}

def create_start_new_game():
    but_new_game = ctk.CTkButton(tbl_canvas, text="Uus mäng", command=start_new_game, **button1_config)
    but_new_game.place(x=(WINDOW_WIDTH)-185, y=80)

def create_back_to_menu():
    global but_back
    but_back = ctk.CTkButton(tbl_canvas, text="Tagasi menüüsse", command=back_to_menu, **button1_config)
    but_back.place(x=(WINDOW_WIDTH)-240, y=25)

# --------------------------------------
def create_player(num: int, face: str):
    global tbl_canvas     
    
    data = players[num]
    name = data["name"]
    type = data["type"]
    
    if data["player_p"]["player_image"]:
        tbl_canvas.delete(data["player_p"]["player_image"])

    img = Image.open(face)
    img = img.resize(MAN_FACE_SIZE, 1)
    tk_image = ImageTk.PhotoImage(img)

    face_pos = ((DISTANCE_BETWEEN_PLAYERS*num)+(DISTANCE_BETWEEN_PLAYERS/2)-(MAN_FACE_SIZE[0]/2), WINDOW_HEIGHT-240)
    data["pos"] = ((DISTANCE_BETWEEN_PLAYERS*num)+(DISTANCE_BETWEEN_PLAYERS/2), WINDOW_HEIGHT-100)

    if type == DEALER:
        face_pos = ((WINDOW_WIDTH/2)-(MAN_FACE_SIZE[0]/2), 10)
        data["pos"] = ((WINDOW_WIDTH/2), 140)

    pos = data["pos"]
    
    player_image = tbl_canvas.create_image(face_pos[0], face_pos[1], image=tk_image, anchor=tk.NW)
    player_name = tbl_canvas.create_text(
        pos[0],
        pos[1], 
        text=name, font=("Arial", 16), fill="white")
    
    panel_d = {
        "img": tk_image,
        "player_image": player_image,
        "player_name": player_name,
    }
    
    players[num]["player_p"] = panel_d
    
# --------------------------------------
def create_buttons():
    global tbl_canvas, but_get_card, but_stay
    delete_buttons()

    button_config = {
        "width": 120, "height": 30,
        "font": ("Arial", 18),
        "fg_color": "white",
        "text_color": "black",
        "hover": False,
        "corner_radius": 0,
    }

    but_get_card = ctk.CTkButton(tbl_canvas, text="Võta kaart", command=lambda: get_card(), **button_config)
    but_get_card.place(x=(WINDOW_WIDTH/2)-(120/2), y=get_dealer()["pos"][1]+140)

    but_stay = ctk.CTkButton(tbl_canvas, text="Ära võta", command=lambda: stay(), **button_config)
    but_stay.place(x=(WINDOW_WIDTH/2)-(120/2), y=WINDOW_HEIGHT-40)
    
def delete_buttons():
    global but_get_card, but_stay

    if but_get_card:
        but_get_card.destroy()
        but_stay.destroy()
        
def create_arrow():
    global arrow, cur_player
    
    pos = players[cur_player]["pos"]
    if players[cur_player]["type"] == DEALER:
        pos = (pos[0], pos[1]+100)

    delete_arrow()
    
    arrow = tbl_canvas.create_text(
        pos[0],
        pos[1]+50,
        text="↑", font=("Arial", 30), fill="red")
    
def delete_arrow():
    global arrow
    if arrow:
        tbl_canvas.delete(arrow)
    
# --------------------------------------
def create_card(visible_cards: list, player_num: int):
    global tbl_canvas

    player = players[player_num]

    for card_p in player["cards_p"]:
        card_p["panel"].destroy()
    
    player["cards_p"].clear()
    
    vertical_offset = 0
    horizontal_offset = 0
    card_width = 45
    card_height = 50
    gap = 35
    cards_in_row = 0
    max_cards_per_row = 2
    
    for key, card in enumerate(player["cards"]):
        is_visible = (key in visible_cards) or is_end_game

        if is_visible:
            img = Image.open(f"mang21/images/cards/{card}.png")
        else:
            img = Image.open(f"mang21/images/cards/unknown.png")

        img = img.resize((card_width, card_height), 1)
        tk_image = ImageTk.PhotoImage(img)

        player_pos = player["pos"]
        pos = (player_pos[0] + 50 + horizontal_offset, player_pos[1] - 220 - vertical_offset)

        if player["type"] == DEALER:
            pos = (player_pos[0] + 60 + horizontal_offset, player_pos[1] + 50 - vertical_offset)

        card_panel = tk.Frame(tbl_canvas, bg="white", bd=2, relief=tk.RAISED)
        card_panel.place(x=pos[0], y=pos[1])

        card_image = tk.Label(card_panel, image=tk_image, bg="white")
        card_image.pack()

        if is_visible:
            card_name = tk.Label(card_panel, text=card, bg="white", font=("Arial", 10))
        else:
            card_name = tk.Label(card_panel, text="?", bg="white", font=("Arial", 12))

        card_name.pack()

        card_p = {
            "card": card,
            "pos": (pos[0], pos[1]),
            "panel": card_panel,
            "img": tk_image,
        }

        players[player_num]["cards_p"].append(card_p)

        cards_in_row += 1

        if player["type"] == DEALER:
            horizontal_offset -= card_width + gap
        else:
            if cards_in_row >= max_cards_per_row:
                vertical_offset = 0
                horizontal_offset -= card_width + gap
                cards_in_row = 0
            else:
                vertical_offset += card_height + gap

    update_score()
         
# -------------------------------------- 
scores_texts = []

def update_score():
    global scores_texts, tbl_canvas, is_dealer_turn
    
    for text in scores_texts:
        tbl_canvas.delete(text)
    
    for key, data in players.items():
        score = count_score(data["cards"])
        if data["type"] == DEALER and not is_dealer_turn:
            if len(data["cards"]) == 2:
                second_card = data["cards"][1]
                score -= CARDS[second_card]

        pos = data["pos"]
        text = tbl_canvas.create_text(
            pos[0],
            pos[1] + 20,
            text=f"Skoor: {score}", font=("Arial", 12), fill="white")
        
        scores_texts.append(text)
        
        if is_end_game:
            text2 = tbl_canvas.create_text(
                pos[0],
                pos[1] + 50,
                text=data["result"], font=("Arial", 16), fill="white")
            
            scores_texts.append(text2)

def show_history():
    for widget in main_frame.winfo_children():
        widget.destroy()

    history_frame = ctk.CTkFrame(main_frame)
    history_frame.configure(fg_color="#0c5202")
    history_frame.pack(fill=tk.BOTH, expand=True)

    ctk.CTkLabel(history_frame, text="Mängu ajalugu", font=("Arial", 36)).pack(pady=10)

    global history
    load_history()
    if not history:
        ctk.CTkLabel(history_frame, text="Ajalugu on tühi.", font=("Arial", 25)).pack(pady=20)
    else:
        for idx, entry in enumerate(reversed(history[-4:])):
            text = f"\n  Mäng #{len(history)-idx} - Diileri skoor: {entry['dealer_score']} | Võit: {entry['winnigs']}  \n"

            for pname, result in entry["player_results"].items():
                text += f"  {pname}: {result['score']} ({result['result']}) - {result['cards']}\n"

            label = ctk.CTkLabel(history_frame, text=text, font=("Arial", 20), justify="left", anchor="w")
            label.configure(fg_color="green")
            label.pack(pady=5)

    button_config = {
        "width": 250, "height": 60,
        "font": ("Arial", 22),
        "text_color": "white",
        "corner_radius": 0,
        "fg_color": "green",
    }

    ctk.CTkButton(history_frame, text="Tagasi", command=create_menu, **button_config).pack(pady=10)
        
# --------------------------------------
# game
# --------------------------------------
players = {}
cur_player = -1
is_end_game = False
is_dealer_turn = False

money_on_start = 0
money = 1000
bet = 0
JSON_SAVE_DATA = "mang21/save.json"
JSON_HISTORY_FILE = "mang21/history.json"

def count_score(cards: dict):
    score = 0
    aces = 0
    for card in cards:
        score += CARDS[card]
        if card == "A":
            aces += 1
    while score > 21 and aces:
        score -= 10
        aces -= 1

    return score

def start_game():
    but_start.destroy()
    but_back.destroy()
    global money_on_start
    money_on_start = money

    cards = list(CARDS.keys())
    for id, player in players.items():
        if player["type"] != DEALER:
            window.after(1000 * id, give_start_cards, id)

    get_dealer()["cards"] = [random.choice(cards), random.choice(cards)]
    create_card([0], PLAYER_NUM)
    
    window.after((1000 * PLAYER_NUM)+1000, next_player)

def give_card(player_id: int):
    player = players[player_id]

    cards = list(CARDS.keys())
    player["cards"].append(random.choice(cards))
    create_card(get_visible_cards(player_id), player_id)

def give_start_cards(player_id: int):
    window.after(100 * PLAYER_NUM, give_card, player_id)
    window.after(200 * PLAYER_NUM, give_card, player_id)
    
# --------------------------------------
def next_player():
    global cur_player

    if cur_player < PLAYER_NUM-1:
        cur_player += 1
    else:
        cur_player = 0

    delete_buttons()
    ask_player()
    
def ask_player():
    create_arrow()
    
    if players[cur_player]["type"] == BOT:
        window.after(1000, bot_turn)
    else:
        if is_bust(cur_player):
            stay()
        else:
            create_buttons()

def bot_turn():
    bot_cards = players[cur_player]["cards"]
    bot_score = count_score(bot_cards)

    if random.randint(0, 100) < 10:
        stay()
    else:
        if bot_score < 17:
            get_card()
        elif bot_score >= 18 and bot_score < 21:
            if random.randint(0, 100) < 20:
                get_card()
            else:
                stay()
        else:
            stay()

def dealer_turn():
    global is_dealer_turn
    is_dealer_turn = True

    delete_buttons()
    create_arrow()
    create_card(get_visible_cards(PLAYER_NUM), PLAYER_NUM)
    
    if count_score(get_dealer()["cards"]) < 17:
        window.after(1000, give_dealer_card)
    else:
        window.after(1000, end_game)

def give_dealer_card():
    cards = get_dealer()["cards"]
    cards.append(random.choice(list(CARDS.keys())))
    create_card(get_visible_cards(PLAYER_NUM), PLAYER_NUM)

    if not (count_score(cards) < 17):
        window.after(1000, end_game)
    else:
        window.after(1500, give_dealer_card)

def get_card():
    player = players[cur_player]
    cards = list(CARDS.keys())
    
    player["cards"].append(random.choice(cards))
    create_card(get_visible_cards(cur_player), cur_player)
        
    check_cards(cur_player)
    next_player()

def check_cards(player_id: int):
    if is_bust(player_id):
        if players[player_id]["player_p"]["player_image"]:
            tbl_canvas.delete(players[player_id]["player_p"]["player_image"])
        
        window.after(200, create_player, cur_player, "mang21/images/man_face_not_smile.png")

def stay():
    if cur_player == PLAYER_NUM - 1:
        dealer_turn()
    else:
        next_player()

def end_game():
    global is_end_game, money, bet
    is_end_game = True
    dealer_score = count_score(get_dealer()["cards"])
    delete_arrow()
    
    for id, player in players.items():
        if player["player_p"]["player_image"]:
            tbl_canvas.delete(player["player_p"]["player_image"])
    
    for id, player in players.items():
        create_card(get_visible_cards(id), id)
        if player["type"] == DEALER:
            continue

        name = player["name"]     
        score = count_score(player["cards"])

        if is_bust(id):
            print(f"{name} busts! Kaotus.")
            window.after(500, create_player, id, "mang21/images/man_face_not_smile.png")
            player["result"] = "Kaotus"
        elif dealer_score > 21 or score > dealer_score:
            print(f"{name} võitis!")
            window.after(300, create_player, id, "mang21/images/man_face_smile.png")
            player["result"] = "Võitis"
            
            if player["type"] == HUMAN:
                money += bet * 2
        elif score == dealer_score:
            print(f"{name} viik.")
            window.after(300, create_player, id, "mang21/images/man_face.png")
            player["result"] = "Viik"

            if player["type"] == HUMAN:
                cancel_bet()
        else:
            print(f"{name} kaotas.")
            window.after(300, create_player, id, "mang21/images/man_face_not_smile.png")
            player["result"] = "Kaotas"
            
    window.after(300, create_player, PLAYER_NUM, "mang21/images/man_face.png")

    bet = 0
    save_data()
    log_game()
    
    create_start_new_game()
    create_back_to_menu()
    create_money_count()

def reset_game():
    global is_end_game, is_dealer_turn, cur_player

    is_end_game = False
    is_dealer_turn = False
    cur_player = -1

    players.clear()
        
def make_bet(sum: int):
    global money, bet
    sum = min(money, sum)
    money -= sum
    bet = sum

def cancel_bet():
    global money, bet
    money += bet
    bet = 0

def start_new_game():
    cancel_bet()
    reset_game()
    create_table()

def back_to_menu():
    cancel_bet()
    create_menu()

# --------------------------------------
def register_player(player_id, name, player_type):
    players[player_id] = {
        "name": name,
        "type": player_type,
        "score": 0,
        "cards": [],
        "cards_p": [],
        "player_p": {
            "player_image": None
        },
        "pos": None,
        "result": "",
    }

def register_players():
    for i in range(PLAYER_NUM):
        if i < (PLAYER_NUM-1):
            register_player(i, f"Bot {i+1}", BOT)
        else:
            register_player(i, f"Sina", HUMAN)
            
    register_player(PLAYER_NUM, f"Diiler", DEALER)

# --------------------------------------
def get_dealer():
    for id, player in players.items():
        if player["type"] == DEALER:
            return player
        
def is_bust(player_id: int):
    return count_score(players[player_id]["cards"]) > 21

def get_visible_cards(player_id: int):
    return list(range(len(players[player_id]["cards"])))

# --------------------------------------
# save
# --------------------------------------
def save_data():
    data = {
        "money": money,
    }

    with open(JSON_SAVE_DATA, "w", encoding="utf-8") as file:
        json.dump(data, file)

def load_data():
    global money

    try:
        with open(JSON_SAVE_DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
            money = int(data["money"])
    except:
        money = 1000

# --------------------------------------
# history
# --------------------------------------
history = []

def load_history():
    global history
    try:
        with open(JSON_HISTORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)
    except:
        pass

def save_history(new_entry):
    global history
    load_history()
    history.append(new_entry)

    with open(JSON_HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)

def log_game():
    game_log = {
        "player_results": {},
        "winnigs": money-money_on_start,
        "dealer_score": count_score(get_dealer()["cards"]),
    }

    for id, player in players.items():
        if player["type"] == DEALER:
            continue

        game_log["player_results"][player["name"]] = {
            "cards": player["cards"],
            "score": count_score(player["cards"]),
            "result": player["result"]
        }

    save_history(game_log)
    

# --------------------------------------
create_window()