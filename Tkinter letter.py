import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="kunal",
        database="letter"
    )

def insert_note():
    note_text = note_entry.get("1.0", tk.END).strip()
    if note_text:
        db = connect_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO notes (note_text) VALUES (%s)", (note_text,))
        db.commit()
        cursor.close()
        db.close()
        note_entry.delete("1.0", tk.END)
        load_notes()
    else:
        messagebox.showwarning("Warning", "Please enter a note.")

def load_notes():
    notes_list.delete(0, tk.END)
    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM notes")
    for note in cursor.fetchall():
        notes_list.insert(tk.END, f"{note[1]} (Created at: {note[2]})")
    cursor.close()
    db.close()

# GUI Setup
root = tk.Tk()
root.title("Notes App")

note_entry = tk.Text(root, height=5, width=40)
note_entry.pack(pady=10)

save_button = tk.Button(root, text="Save Note", command=insert_note)
save_button.pack(pady=5)

notes_list = tk.Listbox(root, width=50)
notes_list.pack(pady=10)

load_notes()

root.mainloop()
