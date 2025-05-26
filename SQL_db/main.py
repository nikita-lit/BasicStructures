import sqlite3
import customtkinter as ctk
from tkinter import messagebox, ttk
import subprocess

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

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

search_entry = None
    
def create_window_table():
    root = ctk.CTk()
    root.title("Filmid")

    frame = ctk.CTkFrame(root)
    frame.pack(pady=20, fill=ctk.BOTH, expand=True)
    scrollbar = ctk.CTkScrollbar(frame)
    scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
    
    tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=("id", "title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), show="headings")
    tree.pack(fill=ctk.BOTH, expand=True)

    scrollbar.configure(command=tree.yview)

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
    
    search_frame = ctk.CTkFrame(root)
    search_frame.pack(pady=10)

    search_label = ctk.CTkLabel(search_frame, text="Otsi filmi pealkirja järgi:")
    search_label.pack(side=ctk.LEFT, padx=10)

    global search_entry
    search_entry = ctk.CTkEntry(search_frame)
    search_entry.pack(side=ctk.LEFT, padx=10)

    search_button = ctk.CTkButton(search_frame, text="Otsi", command=lambda tree=tree: on_search(tree), width=100)
    search_button.pack(side=ctk.LEFT)
    
    open_button = ctk.CTkButton(search_frame, text="Lisa andmeid", command=add_data, width=25)
    open_button.pack(pady=20, padx=20)

    root.mainloop()
    
def add_data():
    subprocess.run(["python", "SQL_db/insert_data_win.py"])
    
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
  
create_window_table()