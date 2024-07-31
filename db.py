from tkinter import *
import sqlite3
from datetime import datetime

root = Tk()
root.title("Hola mundo: todo list")
root.geometry("500x500")

conn = sqlite3.connect('todo.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS todo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    description TEXT NOT NULL,
    completed BOOLEAN NOT NULL
);
""")

conn.commit()

def addTodo():
    todo = e.get()
    created_at = datetime.now()
    c.execute("""
    INSERT INTO todo (created_at, description, completed) 
    VALUES (?, ?, ?)
    """, (created_at, todo, False))
    e.delete(0, END)

l = Label(root, text='Tarea')
l.grid(row=0, column=0)

e = Entry(root, width=40)
e.grid(row=0, column=1)
e.focus()

btn = Button(root, text = 'Agregar', command=addTodo)
btn.grid(row=0, column=2)

frame = LabelFrame(root, text='Mis Tareas', padx=5, pady=5)
frame.grid(row=1, column=0, columnspan=3, sticky='nswe', padx=5)

root.bind('<Return>', lambda x: addTodo())

root.mainloop()