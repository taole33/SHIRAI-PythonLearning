import sqlite3
from tkinter import messagebox



def insert1(seitxt,meitxt,pn1txt,ad1txt,ad2txt,ad3txt):
    gettxt=(seitxt,meitxt,pn1txt,ad1txt,ad2txt,ad3txt) 
    
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE if not exists users(id INTEGER PRIMARY KEY AUTOINCREMENT, sei TEXT,mei TEXT,pn1 INTEGER,ad1 TEXT,ad2 TEXT,ad3 TEXT)''')
    c.execute('INSERT INTO users(sei,mei,pn1,ad1,ad2,ad3) values(?,?,?,?,?,?)',gettxt)

    conn.commit()
    conn.close()

    messagebox.showinfo('完了','データベースへの登録が完了しました')

