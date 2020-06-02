import tkinter
from tkinter import messagebox

tki = tkinter.Tk()
tki.geometry('500x400') 
tki.title('調べたい株価のコード入力')


def soukankeisu():
    import requests
    from bs4 import BeautifulSoup as BS
    import pandas
    import urllib.parse
    import numpy
    from tkinter import messagebox
    
    shinyoubairitsu=[]
    kabuka=[]
    code=txt.get()

    print(type(code))
    #if not type(code) == 'int':
    # messagebox.showinfo('エラー','数字４桁を入力してください')
    #else:
    #code = str(code)   
    #if not code == (len(4)):
    #  messagebox.showinfo('エラー','数字４桁を入力してください')

    #else:
 
    html = requests.get('https://kabutan.jp/stock/kabuka?code='+code+'&ashi=shin')
    kaiseki = BS(html.content,'html.parser')

    table = kaiseki.find('table',class_='stock_kabuka3')
    rows = table.find_all("tr")

    for i in range(28):
        hiritsurow  = rows[2+i]
        column = hiritsurow.find_all("td")
        owarine = column[2].text
        owarinefloat=float(owarine.replace(',',''))
        kabuka.append(owarinefloat)
        hiritsu = column[6].text
        hiritsufloat= float(hiritsu.replace(',',''))
        shinyoubairitsu.append(hiritsufloat)

    a3 = numpy.corrcoef(kabuka,shinyoubairitsu)[0]


    
    messagebox.showinfo('結果','相関係数は'+str(a3)+'です')

lbl = tkinter.Label(text='株価コード')
lbl.place(x=40, y=70)
txt = tkinter.Entry(width=20)
txt.place(x=120, y=70)
lbl2 = tkinter.Label(text='信用倍率と株価の相関係数を調べます')
lbl2.place(x=40, y=120)

btn = tkinter.Button(tki, text='実行' ,command=soukankeisu) 
btn.place(x=300, y=300) 


tki.mainloop()

soukankeisu()
