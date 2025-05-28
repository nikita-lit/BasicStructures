# --------------------------------------
# Filmide projekti edasiareng
# --------------------------------------

import sqlite3
import customtkinter as ctk
from tkinter import messagebox, ttk

# --------------------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

DATABASE_PATH = "SQL_Filmid/movies.db"

MOVIES = "movies"
LANGUAGES = "languages"
COUNTRIES = "countries"
GENRES = "genres"
DIRECTORS = "directors"

tables = {}

movies_data = [
    {
        "title": "The From In With.",
        "director_id": "Francis Ford Coppola",
        "release_year": 1994,
        "genre_id": 1,
        "duration": 142,
        "rating": 9.3,
        "language_id": 1,
        "country_id": 1,
        "description": "The In With By On. A In From By The At. On A With By By On To A."
    },
    {
        "title": "The By On To.",
        "director_id": "Christopher Nolan",
        "release_year": 2010,
        "genre_id": 1,
        "duration": 148,
        "rating": 8.8,
        "language_id": 1,
        "country_id": 1,
        "description": "The A The On The In. By To A At On The. From The In With At In To A."
    },
    {
        "title": "In The With On.",
        "director_id": "Quentin Tarantino",
        "release_year": 1972,
        "genre_id": 1,
        "duration": 175,
        "rating": 9.2,
        "language_id": 1,
        "country_id": 1,
        "description": "On From The By At The A. In From By With To On. A The By In With At On To A."
    },
    {
        "title": "The A To From.",
        "director_id": "Steven Spielberg",
        "release_year": 1994,
        "genre_id": 1,
        "duration": 154,
        "rating": 8.9,
        "language_id": 1,
        "country_id": 1,
        "description": "With By In The A On. The With To A At The From. On A From With At By The."
    },
    {
        "title": "On The From With.",
        "director_id": "Martin Scorsese",
        "release_year": 2008,
        "genre_id": 1,
        "duration": 152,
        "rating": 9.0,
        "language_id": 1,
        "country_id": 1,
        "description": "The A By On In The. At With To A From On The. With On By The A In To From."
    },
    {
        "title": "From The By With.",
        "director_id": "Christopher Nolan",
        "release_year": 1960,
        "genre_id": 1,
        "duration": 134,
        "rating": 8.5,
        "language_id": 1,
        "country_id": 1,
        "description": "The A On From The At. With To By In A The On. At The In From With By To A."
    },
    {
        "title": "The By On A.",
        "director_id": "Francis Ford Coppola",
        "release_year": 1999,
        "genre_id": 1,
        "duration": 112,
        "rating": 7.8,
        "language_id": 1,
        "country_id": 1,
        "description": "A The On By In The At. From With A On By To The. In The By With At A From."
    },
    {
        "title": "On A The From.",
        "director_id": "Quentin Tarantino",
        "release_year": 2015,
        "genre_id": 1,
        "duration": 126,
        "rating": 7.9,
        "language_id": 1,
        "country_id": 1,
        "description": "By With A On In The From. The By At A With On To. At In The By From With A."
    },
    {
        "title": "By The On From.",
        "director_id": "Steven Spielberg",
        "release_year": 1975,
        "genre_id": 1,
        "duration": 143,
        "rating": 8.7,
        "language_id": 1,
        "country_id": 1,
        "description": "A With On The By From In. The A At On With To From. By In The A From With At On."
    },
    {
        "title": "From With The By.",
        "director_id": "Martin Scorsese",
        "release_year": 1980,
        "genre_id": 1,
        "duration": 163,
        "rating": 9.1,
        "language_id": 1,
        "country_id": 1,
        "description": "On The A By In The From. With By On A The In From. To The In At By With On A."
    }
]

# --------------------------------------
def connect_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    return (conn, cursor)

def create_db():
    isError = False
    try:
        conn, cursor = connect_db()
        print("Ühendus loodud")
        
        init_tables(cursor)
        
        cursor.execute("SELECT count(*) FROM movies")
        count = cursor.fetchone()[0]

        if count <= 0:
            for data in movies_data:
                insert_into_table(cursor, MOVIES, data)
                
            insert_into_table(cursor, LANGUAGES, {"name": "Inglise"})
            insert_into_table(cursor, LANGUAGES, {"name": "Vene"})
            insert_into_table(cursor, LANGUAGES, {"name": "Eesti"})
                
    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel:", error)
        messagebox.showerror("Viga", error)
        isError = True
    finally:      
        if conn:
            conn.commit()
            conn.close()
            print("Ühendus suleti")
            
    return not isError

def create_table(cursor, tbl_name: str, columns: dict, foreign_keys: dict = {}):
    column_defs = []

    for column_name, column_type in columns.items():
        column_defs.append(f"{column_name} {column_type}")

    for fk_column, ref in foreign_keys.items():
        column_defs.append(f"FOREIGN KEY ({fk_column}) REFERENCES {ref}")

    column_defs_str = ",\n".join(column_defs)
    query = f"""
    CREATE TABLE IF NOT EXISTS {tbl_name} (
        {column_defs_str}
    );
    """
    
    global tables
    tables[tbl_name] = {
        "columns": columns,
        "foreign_keys": foreign_keys,
    }
    
    cursor.execute(query)

def init_tables(cursor):
    create_table(cursor, MOVIES, {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "title": "TEXT NOT NULL",
        "director_id": "INTEGER",
        "release_year": "INTEGER",
        "genre_id": "INTEGER",
        "duration": "INTEGER",
        "rating": "REAL",
        "language_id": "INTEGER",
        "country_id": "INTEGER",
        "description": "TEXT",
    },
    {
        "director_id": "directors(id)",
        "genre_id": "genres(id)",
        "language_id": "languages(id)",
        "country_id": "countries(id)",
    })
    
    create_table(cursor, LANGUAGES, {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "description": "TEXT UNIQUE NOT NULL",
    })
    
    create_table(cursor, COUNTRIES, {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "description": "TEXT UNIQUE NOT NULL",
    })
    
    create_table(cursor, GENRES, {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "description": "TEXT UNIQUE NOT NULL",
    })
    
    create_table(cursor, COUNTRIES, {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "description": "TEXT UNIQUE NOT NULL",
    })
    
def insert_into_table(cursor, table_name: str, data: dict):
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['?'] * len(data))
    values = tuple(data.values())

    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(query, values)
 
# --------------------------------------
def read_table(cursor, tbl_name, options):
    cursor.execute(f"SELECT * FROM {tbl_name} {options}")
    return cursor.fetchall()

def get_tbl_columns(tbl_name: str):
    return tables[tbl_name]["columns"]

def get_tbl_foreign_keys(tbl_name: str):
    return tables[tbl_name]["foreign_keys"]
    
def load_data_from_db(tree, tbl_name, row_name="", search_query=""):
    try:
        for item in tree.get_children():
            tree.delete(item)
        
        conn, cursor = connect_db()
        
        search = ""
        if len(row_name) > 0:
            search = f"WHERE {row_name} LIKE '%{search_query}%'"
            
        rows = read_table(cursor, tbl_name, search)    
        columns = list(get_tbl_columns(tbl_name))
        foreign_keys = get_tbl_foreign_keys(tbl_name)
        print(foreign_keys)

        for row in rows:
            values = []
            for col in tree.columns:
                if col in columns:
                    idx = columns.index(col)
                    values.append(row[idx])
                else:
                    values.append("")
            tree.insert("", "end", values=values)
    except sqlite3.Error as error:
        print("Tekkis viga andmebaasiga ühendamisel:", error)
    finally:    
        if conn:
            conn.commit()
            conn.close()
    
# --------------------------------------
window = None

def create_window():
    global window
    window = ctk.CTk()
    window.title("Filmid")
    window.geometry("1200x500")
    
    columns = {
        "id": "ID",
        "title": "Pealkiri",
        "director_id": "Režissöör",
        "release_year": "Aasta",
        "genre_id": "Žanr",
        "language_id": "Keel",
    }
    
    frame = ctk.CTkFrame(window)
    frame.pack(padx=20, pady=20, fill=ctk.BOTH, expand=True)
    create_tree(frame, MOVIES, columns)
    
    # columns2 = {
    #     "id": "ID",
    #     "name": "Nimi",
    # }
    
    # frame2 = ctk.CTkFrame(window)
    # frame2.configure(width=25, height=25)
    # frame2.pack(padx=20, pady=20)
    # create_tree(frame2, LANGUAGES, columns2)
    
    window.mainloop()
    
def create_tree(parent, tbl_name: str, columns: dict):
    frame = ctk.CTkFrame(parent)
    frame.pack(fill=ctk.BOTH, expand=True)
    
    scrollbar = ctk.CTkScrollbar(frame)
    scrollbar.pack(side=ctk.RIGHT, fill=ctk.Y)
    
    tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=list(columns), show="headings")
    tree.pack(fill=ctk.BOTH, expand=True)

    scrollbar.configure(command=tree.yview)
    
    for key, name in columns.items():
        tree.heading(key, text=name)
        tree.column(key, width=100)
    
    tree.columns = columns
    
    load_data_from_db(tree, tbl_name)
    
    return tree
    
# --------------------------------------
if create_db():
    create_window()