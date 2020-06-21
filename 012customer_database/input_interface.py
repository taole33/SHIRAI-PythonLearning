import tkinter
from main import insert1
import tkinter.ttk as ttk
import sqlite3

tki = tkinter.Tk()
tki.geometry('700x700') 



def view_database():
    tki2 = tkinter.Toplevel()
    view_db = ttk.Treeview(tki2,padding=20)
    view_db['columns'] = (1,2,3,4,5,6,7)
    view_db['show'] = 'headings'


    view_db.column(1,width=20)
    view_db.column(2,width=60)
    view_db.column(3,width=60)
    view_db.column(4,width=100)
    view_db.column(5,width=500)
    view_db.column(6,width=110)
    view_db.column(7,width=60)


    view_db.heading(1,text='ID')
    view_db.heading(2,text='姓')
    view_db.heading(3,text='名')
    view_db.heading(4,text='〒')
    view_db.heading(5,text='住所1')
    view_db.heading(6,text='住所2')
    view_db.heading(7,text='住所3')

    style = ttk.Style()
    style.configure('Treeview',font=('',9))
    style.configure('Treeview.Heading',font=('',9,'bold'),foreground = 'blue')



    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    sql = 'SELECT * from users'

    for i in c.execute(sql):
        view_db.insert("","end",values=i)

    conn.close()

    view_db.pack()





seilbl = tkinter.Label(text='姓：')
seilbl.place(x=50, y=50)
seitxt = tkinter.Entry(width=15)
seitxt.place(x=80, y=50)

meilbl = tkinter.Label(text='名：')
meilbl.place(x=250, y=50)
meitxt = tkinter.Entry(width=15)
meitxt.place(x=280, y=50)


pn1lbl = tkinter.Label(text='〒：')
pn1lbl.place(x=50, y=120)
pn1txt = tkinter.Entry(width=10)
pn1txt.place(x=80, y=120)

pn2lbl = tkinter.Label(text='-')
pn2lbl.place(x=180, y=120)
pn2txt = tkinter.Entry(width=10)
pn2txt.place(x=200, y=120)


ad1lbl = tkinter.Label(text='住所：')
ad1lbl.place(x=50, y=150)
ad1txt = tkinter.Entry(width=50)
ad1txt.place(x=80, y=150)

ad2lbl = tkinter.Label(text='マンション名：')
ad2lbl.place(x=50, y=180)
ad2txt = tkinter.Entry(width=30)
ad2txt.place(x=150, y=180)

ad3lbl = tkinter.Label(text='　　　　号室：')
ad3lbl.place(x=50, y=210)
ad3txt = tkinter.Entry(width=30)
ad3txt.place(x=150, y=210)

btn = tkinter.Button(tki, text='登録' ,command=lambda:insert1(seitxt.get(),meitxt.get(),pn1txt.get()+pn2txt.get(),ad1txt.get(),ad2txt.get(),ad3txt.get()))
btn.place(x=500, y=500) 

btn = tkinter.Button(tki, text='データベース参照',command=view_database)
btn.place(x=100, y=500) 

tki.mainloop()