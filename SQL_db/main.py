import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

movies_data = [
    {
        "title": "The From In With.",
        "director": "Francis Ford Coppola",
        "release_year": 1994,
        "genre": "Drama",
        "duration": 142,
        "rating": 9.3,
        "language": "English",
        "country": "USA",
        "description": "The In With By On. A In From By The At. On A With By By On To A."
    },
    {
        "title": "The By On To.",
        "director": "Christopher Nolan",
        "release_year": 2010,
        "genre": "Sci-Fi",
        "duration": 148,
        "rating": 8.8,
        "language": "English",
        "country": "UK",
        "description": "The A The On The In. By To A At On The. From The In With At In To A."
    },
    {
        "title": "In The With On.",
        "director": "Quentin Tarantino",
        "release_year": 1972,
        "genre": "Crime",
        "duration": 175,
        "rating": 9.2,
        "language": "English",
        "country": "USA",
        "description": "On From The By At The A. In From By With To On. A The By In With At On To A."
    },
    {
        "title": "The A To From.",
        "director": "Steven Spielberg",
        "release_year": 1994,
        "genre": "Adventure",
        "duration": 154,
        "rating": 8.9,
        "language": "English",
        "country": "France",
        "description": "With By In The A On. The With To A At The From. On A From With At By The."
    },
    {
        "title": "On The From With.",
        "director": "Martin Scorsese",
        "release_year": 2008,
        "genre": "Action",
        "duration": 152,
        "rating": 9.0,
        "language": "English",
        "country": "Germany",
        "description": "The A By On In The. At With To A From On The. With On By The A In To From."
    },
    {
        "title": "From The By With.",
        "director": "Christopher Nolan",
        "release_year": 1960,
        "genre": "Drama",
        "duration": 134,
        "rating": 8.5,
        "language": "English",
        "country": "UK",
        "description": "The A On From The At. With To By In A The On. At The In From With By To A."
    },
    {
        "title": "The By On A.",
        "director": "Francis Ford Coppola",
        "release_year": 1999,
        "genre": "Thriller",
        "duration": 112,
        "rating": 7.8,
        "language": "English",
        "country": "USA",
        "description": "A The On By In The At. From With A On By To The. In The By With At A From."
    },
    {
        "title": "On A The From.",
        "director": "Quentin Tarantino",
        "release_year": 2015,
        "genre": "Comedy",
        "duration": 126,
        "rating": 7.9,
        "language": "English",
        "country": "Italy",
        "description": "By With A On In The From. The By At A With On To. At In The By From With A."
    },
    {
        "title": "By The On From.",
        "director": "Steven Spielberg",
        "release_year": 1975,
        "genre": "Action",
        "duration": 143,
        "rating": 8.7,
        "language": "English",
        "country": "France",
        "description": "A With On The By From In. The A At On With To From. By In The A From With At On."
    },
    {
        "title": "From With The By.",
        "director": "Martin Scorsese",
        "release_year": 1980,
        "genre": "Crime",
        "duration": 163,
        "rating": 9.1,
        "language": "English",
        "country": "Germany",
        "description": "On The A By In The From. With By On A The In From. To The In At By With On A."
    }
]

DATABASE_PATH = "SQL_db/movies.db"

def read_table(cursor, name, options):
    cursor.execute(f"SELECT * FROM {name} {options}")
    return cursor.fetchall()

def create_db():
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        print("Ühendus loodud")
        
        create_table(cursor)
        
        cursor.execute("SELECT count(*) FROM movies")
        count = cursor.fetchone()[0]

        if count <= 0:
            for data in movies_data:
                insert_into_table(cursor, data)
                
    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel:", error)
    finally:      
        if conn:
            conn.commit()
            conn.close()
            print("Ühendus suleti")

def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        director TEXT,
        release_year INTEGER,
        genre TEXT,
        duration INTEGER,
        rating REAL,
        language TEXT,
        country TEXT,
        description TEXT
    );
    """)
    
    print("Tabel loodud")

def insert_into_table(cursor, data: dict):
    cursor.execute(f"""   
        INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data["title"], 
        data["director"], 
        data["release_year"], 
        data["genre"], 
        data["duration"], 
        data["rating"], 
        data["language"], 
        data["country"], 
        data["description"]))
    
create_db()

# --------------------------------------
search_entry = None
root = None

def create_window_table():
    global root
    root = tk.Tk()
    root.title("Filmid")
    root.geometry("1200x500")

    frame = tk.Frame(root)
    frame.pack(pady=20, fill=tk.BOTH, expand=True, padx=20)
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("id", "title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    scrollbar.config(command=tree.yview)

    tree.heading("id", text="ID")
    tree.heading("title", text="Pealkiri")
    tree.heading("director", text="Režissöör")
    tree.heading("year", text="Aasta")
    tree.heading("genre", text="Žanr")
    tree.heading("duration", text="Kestus")
    tree.heading("rating", text="Reiting")
    tree.heading("language", text="Keel")
    tree.heading("country", text="Riik")
    tree.heading("description", text="Kirjeldus")

    tree.column("id", width=40)
    tree.column("title", width=150)
    tree.column("director", width=100)
    tree.column("year", width=60)
    tree.column("genre", width=100)
    tree.column("duration", width=60)
    tree.column("rating", width=60)
    tree.column("language", width=80)
    tree.column("country", width=80)
    tree.column("description", width=200)
    
    load_data_from_db(tree)
    
    search_frame = tk.Frame(root)
    search_frame.pack(pady=5, expand=True, fill=tk.BOTH)

    search_label = tk.Label(search_frame, text="Otsi filmi pealkirja järgi:")
    search_label.pack(side=tk.LEFT, padx=10)

    global search_entry
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=10)

    search_button = tk.Button(search_frame, text="Otsi", command=lambda tree=tree: on_search(tree), width=20)
    search_button.pack(side=tk.LEFT)
    
    update_button = tk.Button(search_frame, text="Uuenda", command=lambda tree=tree: on_update(tree))
    update_button.pack(pady=5, padx=(5, 20), side=tk.RIGHT)
    
    delete_button = tk.Button(search_frame, text="Kustuta", command=lambda tree=tree: on_delete(tree))
    delete_button.pack(pady=5, padx=5, side=tk.RIGHT)
    
    open_button = tk.Button(search_frame, text="Lisa andmeid", command=lambda tree=tree: add_data(tree), width=25)
    open_button.pack(pady=5, padx=5, side=tk.RIGHT)
    
    root.mainloop()
    
# --------------------------------------
def open_update_window(tree, record_id):
    update_window = tk.Toplevel(root)
    update_window.title("Muuda filmi andmeid")

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT title, director, release_year, genre, duration, rating, language, country, description FROM movies WHERE id=?", (record_id,))
    record = cursor.fetchone()
    conn.close()

    if not record:
        messagebox.showerror("Viga", f"Record IDga {record_id} ei leitud.")
        return

    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(update_window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entry = tk.Entry(update_window, width=80)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, record[i])
        entries[label] = entry

    save_button = tk.Button(update_window, text="Salvesta", command=lambda: update_record(tree, record_id, entries, update_window))
    save_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

# --------------------------------------
entries = {}
window = None
def add_data(tree):
    global window
    window = tk.Toplevel(root)
    window.title("Filmi andmete sisestamine")

    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]

    for i, label in enumerate(labels):
        tk.Label(window, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = tk.Entry(window, width=80)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry

    submit_button = tk.Button(window, text="Sisesta andmed", command=lambda tree=tree: insert_data(tree))
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)
    
def clear_entries():
    global entries
    for entry in entries.values():
        entry.delete(0, tk.END)
    
def validate_data():
    title = entries["Pealkiri"].get()
    release_year = entries["Aasta"].get()
    rating = entries["Reiting"].get()

    if not title:
        messagebox.showerror("Viga", "Pealkiri on kohustuslik!")
        return False
    if not release_year.isdigit():
        messagebox.showerror("Viga", "Aasta peab olema arv!")
        return False
    if rating and (not rating.replace('.', '', 1).isdigit() or not (0 <= float(rating) <= 10)):
        messagebox.showerror("Viga", "Reiting peab olema vahemikus 0 kuni 10!")
        return False

    return True
    
def insert_data(tree):
    if validate_data():
        try:
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                entries["Pealkiri"].get(),
                entries["Režissöör"].get(),
                entries["Aasta"].get(),
                entries["Žanr"].get(),
                entries["Kestus"].get(),
                entries["Reiting"].get(),
                entries["Keel"].get(),
                entries["Riik"].get(),
                entries["Kirjeldus"].get()
            ))
        except sqlite3.Error as error:
            print("Tekkis viga andmebaasiga ühendamisel:", error)
        finally:    
            load_data_from_db(tree)
            if conn:
                conn.commit()
                conn.close()
                
        messagebox.showinfo("Edu", "Andmed sisestati edukalt!")
    
# --------------------------------------
def on_search(tree):
    search_query = search_entry.get()
    load_data_from_db(tree, search_query)
    
def load_data_from_db(tree, search_query=""):
        try:
            for item in tree.get_children():
                tree.delete(item)
            
            conn = sqlite3.connect(DATABASE_PATH)
            cursor = conn.cursor()
            rows = read_table(cursor, "movies", f"WHERE title LIKE '%{search_query}%'")
            
            for row in rows:
                tree.insert("", "end", values=row)
        except sqlite3.Error as error:
            print("Tekkis viga andmebaasiga ühendamisel:", error)
        finally:    
            if conn:
                conn.commit()
                conn.close()

# --------------------------------------
def on_update(tree):
    selected_item = tree.selection()
    if selected_item:
        record_id = tree.item(selected_item[0], 'values')[0]
        try:
            record_id = int(record_id)
            open_update_window(tree, record_id)
        except ValueError:
            messagebox.showerror("Error", "Valitud sobimatu ID!")
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")
  
def on_delete(tree):
    selected_item = tree.selection()
    
    if selected_item:
        record_id = tree.item(selected_item[0], 'values')[0]
        confirm = messagebox.askyesno("Kinnita kustutamine", "Kas oled kindel, et soovid selle rea kustutada?")
        if confirm:
            try:
                conn = sqlite3.connect(DATABASE_PATH)
                cursor = conn.cursor()

                cursor.execute("DELETE FROM movies WHERE id=?", (record_id,))
                conn.commit()
                conn.close()

                load_data_from_db(tree)
               
                messagebox.showinfo("Edukalt kustutatud", "Rida on edukalt kustutatud!")
            except sqlite3.Error as e:
                messagebox.showerror("Viga", f"Andmebaasi viga: {e}")
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")
  
def update_record(tree, record_id, entries, window):
    title = entries["Pealkiri"].get()
    director = entries["Režissöör"].get()
    release_year = entries["Aasta"].get()
    genre = entries["Žanr"].get()
    duration = entries["Kestus"].get()
    rating = entries["Reiting"].get()
    language = entries["Keel"].get()
    country = entries["Riik"].get()
    description = entries["Kirjeldus"].get()

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE movies
        SET title=?, director=?, release_year=?, genre=?, duration=?, rating=?, language=?, country=?, description=?
        WHERE id=?
    """, (title, director, release_year, genre, duration, rating, language, country, description, record_id))
    conn.commit()
    conn.close()

    load_data_from_db(tree)
    window.destroy()

    messagebox.showinfo("Salvestamine", "Andmed on edukalt uuendatud!")
  
create_window_table()