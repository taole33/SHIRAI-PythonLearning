import tkinter
from tkinter import messagebox

tki = tkinter.Tk()
tki.geometry('500x400') 
tki.title('調べたい素数の範囲を入力')

def sosu():
 if not starttxt.get().isdigit() :
       messagebox.showinfo('エラー','整数のみ入力可能です')
 else:
  if not endtxt.get().isdigit() :
        messagebox.showinfo('エラー','整数のみ入力可能です')
  else:     
    kekka = []
    startnumber = int(starttxt.get())
    finishnumber= int(endtxt.get())

    startnumber = startnumber - 1

    for kazu in range(startnumber,finishnumber,1):
        startnumber = startnumber + 1
        if startnumber % 2 == 1:
            for warukazu in range(3,startnumber-1,2):
                if startnumber % warukazu == 0:
                    break   
            else:
             kekka.append(startnumber)
    if not kekka:
        messagebox.showinfo('結果','該当ありません')
    else:
        messagebox.showinfo('結果',kekka)
    startnumber=int(starttxt.get())

startlbl = tkinter.Label(text='開始値')
startlbl.place(x=30, y=70)
starttxt = tkinter.Entry(width=20)
starttxt.place(x=90, y=70)


endlbl = tkinter.Label(text='終了値')
endlbl.place(x=30, y=150)
endtxt = tkinter.Entry(width=20)
endtxt.place(x=90, y=150)

btn = tkinter.Button(tki, text='実行' ,command=sosu) 
btn.place(x=300, y=300) 


tki.mainloop()




