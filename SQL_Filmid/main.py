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
        "director_id": 1,
        "release_year": 1994,
        "genre_id": 6,
        "duration": 142,
        "rating": 9.3,
        "language_id": 3,
        "country_id": 2,
        "description": "The In With By On. A In From By The At. On A With By By On To A."
    },
    {
        "title": "The By On To.",
        "director_id": 2,
        "release_year": 2010,
        "genre_id": 2,
        "duration": 148,
        "rating": 8.8,
        "language_id": 2,
        "country_id": 3,
        "description": "The A The On The In. By To A At On The. From The In With At In To A."
    },
    {
        "title": "In The With On.",
        "director_id": 3,
        "release_year": 1972,
        "genre_id": 4,
        "duration": 175,
        "rating": 9.2,
        "language_id": 1,
        "country_id": 4,
        "description": "On From The By At The A. In From By With To On. A The By In With At On To A."
    },
    {
        "title": "The A To From.",
        "director_id": 4,
        "release_year": 1994,
        "genre_id": 3,
        "duration": 154,
        "rating": 8.9,
        "language_id": 1,
        "country_id": 5,
        "description": "With By In The A On. The With To A At The From. On A From With At By The."
    },
    {
        "title": "On The From With.",
        "director_id": 2,
        "release_year": 2008,
        "genre_id": 5,
        "duration": 152,
        "rating": 9.0,
        "language_id": 3,
        "country_id": 1,
        "description": "The A By On In The. At With To A From On The. With On By The A In To From."
    },
    {
        "title": "From The By With.",
        "director_id": 2,
        "release_year": 1960,
        "genre_id": 1,
        "duration": 134,
        "rating": 8.5,
        "language_id": 2,
        "country_id": 2,
        "description": "The A On From The At. With To By In A The On. At The In From With By To A."
    },
    {
        "title": "The By On A.",
        "director_id": 1,
        "release_year": 1999,
        "genre_id": 2,
        "duration": 112,
        "rating": 7.8,
        "language_id": 3,
        "country_id": 3,
        "description": "A The On By In The At. From With A On By To The. In The By With At A From."
    },
    {
        "title": "On A The From.",
        "director_id": 3,
        "release_year": 2015,
        "genre_id": 6,
        "duration": 126,
        "rating": 7.9,
        "language_id": 1,
        "country_id": 4,
        "description": "By With A On In The From. The By At A With On To. At In The By From With A."
    },
    {
        "title": "By The On From.",
        "director_id": 4,
        "release_year": 1975,
        "genre_id": 4,
        "duration": 143,
        "rating": 8.7,
        "language_id": 2,
        "country_id": 5,
        "description": "A With On The By From In. The A At On With To From. By In The A From With At On."
    },
    {
        "title": "From With The By.",
        "director_id": 1,
        "release_year": 1980,
        "genre_id": 3,
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
                
            insert_into_table(cursor, LANGUAGES, {"name": "English"})
            insert_into_table(cursor, LANGUAGES, {"name": "Russian"})
            insert_into_table(cursor, LANGUAGES, {"name": "Estonian"})
            
            insert_into_table(cursor, DIRECTORS, {"name": "Francis Ford Coppola"})
            insert_into_table(cursor, DIRECTORS, {"name": "Christopher Nolan"})
            insert_into_table(cursor, DIRECTORS, {"name": "Quentin Tarantino"})
            insert_into_table(cursor, DIRECTORS, {"name": "Steven Spielberg"})
            
            insert_into_table(cursor, COUNTRIES, {"name": "USA"})
            insert_into_table(cursor, COUNTRIES, {"name": "Italy"})
            insert_into_table(cursor, COUNTRIES, {"name": "Estonia"})
            insert_into_table(cursor, COUNTRIES, {"name": "Germany"})
            insert_into_table(cursor, COUNTRIES, {"name": "Russia"})
            
            insert_into_table(cursor, GENRES, {"name": "Adventure"})
            insert_into_table(cursor, GENRES, {"name": "Action"})
            insert_into_table(cursor, GENRES, {"name": "Drama"})
            insert_into_table(cursor, GENRES, {"name": "Thriller"})
            insert_into_table(cursor, GENRES, {"name": "Comedy"})
            insert_into_table(cursor, GENRES, {"name": "Crime"})
            
                
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

    query = f"""
    CREATE TABLE IF NOT EXISTS {tbl_name} (
        {",".join(column_defs)}
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
    
    create_table(cursor, DIRECTORS, {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT UNIQUE NOT NULL",
    })

    create_table(cursor, LANGUAGES, {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT UNIQUE NOT NULL",
    })
    
    create_table(cursor, COUNTRIES, {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT UNIQUE NOT NULL",
    })
    
    create_table(cursor, GENRES, {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT UNIQUE NOT NULL",
    })
    
    create_table(cursor, COUNTRIES, {
        "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
        "name": "TEXT UNIQUE NOT NULL",
    })
    
def insert_into_table(cursor, table_name: str, data: dict):
    columns = ', '.join(data.keys())
    placeholders = ', '.join(['?'] * len(data))
    values = tuple(data.values())

    query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
    cursor.execute(query, values)
 
# --------------------------------------
def build_select_query(tbl_name: str, where: str = "", do_foreign_keys: bool = True):
    columns = get_tbl_columns(tbl_name)
    foreign_keys = get_tbl_foreign_keys(tbl_name)

    select_fields = []
    join_clauses = []

    for col in columns:
        if do_foreign_keys and col in foreign_keys:
            ref_table = foreign_keys[col].split('(')[0].strip()
            display_col = "name"
            alias = ref_table

            select_fields.append(f"{alias}.{display_col} AS {col}_name")

            join_clauses.append(
                f"LEFT JOIN {ref_table} {alias} ON {tbl_name}.{col} = {alias}.id"
            )
        else:
            select_fields.append(f"{tbl_name}.{col}")

    query = f"""
        SELECT {', '.join(select_fields)}
        FROM {tbl_name} {tbl_name}
        {' '.join(join_clauses)}
    """
    
    if where != "":
        query += f"WHERE {where}"

    return query.strip()


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
        query = build_select_query(tbl_name)
        
        if row_name != "":
            query += f" WHERE {row_name} LIKE ?"
            cursor.execute(query, (f"%{search_query}%",))
        else:
            cursor.execute(query)
            
        rows = cursor.fetchall()   
        columns = list(get_tbl_columns(tbl_name))

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
    
    tables_frame = ctk.CTkFrame(window, height=80)
    tables_frame.pack(pady=(20, 0), padx=20, fill=ctk.X)
    
    for tbl_name in tables:
        search_button = ctk.CTkButton(tables_frame, text=tbl_name, width=50)
        search_button.pack(side=ctk.LEFT, padx=(5, 0), pady=5)
    
    columns = {
        "id": "ID",
        "title": "Pealkiri",
        "director_id": "Režissöör",
        "release_year": "Aasta",
        "genre_id": "Žanr",
        "language_id": "Keel",
        "duration": "Kestus",
        "rating": "Hinnang",
    }
    
    frame = ctk.CTkFrame(window)
    frame.pack(padx=20, pady=20, fill=ctk.BOTH, expand=True)
    create_tree(frame, MOVIES, columns)
    
    window.mainloop()
    
# --------------------------------------
def open_record_window(root, tree, record_id):
    record_window = ctk.CTkToplevel(root)
    record_window.title("Tabel: " + tree.table_name.capitalize())
    record_window.resizable(width=False, height=False)
    
    columns = get_tbl_columns(tree.table_name)
    
    try:
        conn, cursor = connect_db()

        record = cursor.execute(build_select_query(tree.table_name, f"id={record_id}", False))
        record = cursor.fetchone()
        
        entries = {}
        for i, label in enumerate(columns.keys()): 
            frame = ctk.CTkFrame(record_window)
            frame.pack(padx=10, pady=5, expand=True, side=ctk.TOP, fill=ctk.BOTH)
                 
            ctk.CTkLabel(frame, text=label, width=50, anchor="w").pack(padx=10, pady=1, fill=ctk.BOTH, side=ctk.LEFT) 
                    
            entry = ctk.CTkEntry(frame, width=300)
            entry.pack(side=ctk.RIGHT, fill=ctk.BOTH)
            entry.insert(0, record[i])
            entries[label] = entry

        load_data_from_db(tree, MOVIES)
    except sqlite3.Error as e:
        messagebox.showerror("Viga", f"Andmebaasi viga: {e}")
    finally:    
        if conn:
            conn.commit()
            conn.close()

def on_search(tree, row_name):
    load_data_from_db(tree, tree.table_name, row_name, search_entry.get())
    
def on_update(tree):
    global window
    selected_items = tree.selection()
    
    if selected_items:
        record_id = tree.item(selected_items[0], "values")[0]
        open_record_window(window, tree, record_id)
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")
    
def on_delete(tree):
    selected_items = tree.selection()
    
    if selected_items:
        confirm = messagebox.askyesno("Kinnita kustutamine", "Kas oled kindel, et soovid selle rea kustutada?")
        if not confirm:
            return
           
        indexes = []
        for item in selected_items:
            indexes.append(tree.item(item, "values")[0])
            
        try:
            conn, cursor = connect_db()
            for i in indexes:
                cursor.execute(f"DELETE FROM {tree.table_name} WHERE id={i}")
                
            conn.commit()
            conn.close()

            load_data_from_db(tree, MOVIES)
        
            messagebox.showinfo("Edukalt kustutatud", "Rida on edukalt kustutatud!")
        except sqlite3.Error as e:
            messagebox.showerror("Viga", f"Andmebaasi viga: {e}")
        finally:    
            if conn:
                conn.commit()
                conn.close()
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")
    
# --------------------------------------
def create_tree_buttons(root, tree):
    search_frame = ctk.CTkFrame(root, height=80)
    search_frame.pack(pady=(0, 20), padx=20, fill=ctk.X)
    
    global search_entry
    search_entry = ctk.CTkEntry(search_frame, width=250)
    search_entry.pack(side=ctk.LEFT, padx=10)

    search_button = ctk.CTkButton(search_frame, text="Otsi", command=lambda tree=tree: on_search(tree, "title"), width=50)
    search_button.pack(side=ctk.LEFT)
    
    update_button = ctk.CTkButton(search_frame, text="Uuenda", command=lambda tree=tree: on_update(tree))
    update_button.pack(pady=5, padx=5, side=ctk.RIGHT)
    
    delete_button = ctk.CTkButton(search_frame, text="Kustuta", command=lambda tree=tree: on_delete(tree))
    delete_button.pack(pady=5, padx=2, side=ctk.RIGHT)
    
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
    tree.table_name = tbl_name
    
    create_tree_buttons(window, tree)
    load_data_from_db(tree, tbl_name)
    
    return tree
    
# --------------------------------------
if create_db():
    create_window()