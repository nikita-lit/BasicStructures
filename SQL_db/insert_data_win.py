import sqlite3
import customtkinter as ctk
from tkinter import messagebox, ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

DATABASE_PATH = "SQL_db/movies.db"

window = None
entries = {}

def create_window():
    global window, entries
    window = ctk.CTk()
    window.title("Filmi andmete sisestamine")

    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]

    for i, label in enumerate(labels):
        ctk.CTkLabel(window, text=label).grid(row=i, column=0, padx=10, pady=5)
        entry = ctk.CTkEntry(window, width=350)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[label] = entry

    submit_button = ctk.CTkButton(window, text="Sisesta andmed", command=insert_data)
    submit_button.grid(row=len(labels), column=0, columnspan=2, pady=20)

    window.mainloop()
    
def clear_entries():
    global entries
    for entry in entries.values():
        entry.delete(0, ctk.END)
    
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
    
def insert_data():
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
              
            if conn:
                conn.commit()
                conn.close()
                
        messagebox.showinfo("Edu", "Andmed sisestati edukalt!")
        
create_window()