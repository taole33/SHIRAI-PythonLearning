import tkinter
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup as BS
import pandas
import urllib.parse
import numpy


tki = tkinter.Tk()
tki.geometry('500x400') 
tki.title('調べたい株価のコード入力')


def soukankeisu():

    margin_ratio=[]
    stock_price=[]
    code=txt.get()

    html = requests.get('https://kabutan.jp/stock/kabuka?code='+code+'&ashi=shin')
    if not html.status_code == 200:
        messagebox.showinfo('エラー','webページに問題が発生しました')
        return
    
    analyse = BS(html.content,'html.parser')
    stock_name = analyse.find('div',class_='si_i1_1')

    if not stock_name:
        messagebox.showinfo('エラー','銘柄が見つかりませんでした')
        return
           
    table = analyse.find('table',class_='stock_kabuka3')
    rows = table.find_all("tr")

    for i in range(28):
        ratiorow  = rows[2+i]
        column = ratiorow.find_all("td")
        price = column[2].text
        pricefloat=float(price.replace(',',''))
        stock_price.append(pricefloat)
        ratio = column[6].text
        if ratio == "－":
            messagebox.showinfo('エラー','信用倍率が存在しないため計算できません')
            break
        else:
            ratiofloat= float(ratio.replace(',',''))
            margin_ratio.append(ratiofloat)
    
                    
    result = numpy.corrcoef(stock_price,margin_ratio)[0]
    result = str(result).replace('1.         ','')
    stock_name = stock_name.find("h2")
    stock_name = stock_name.text
    messagebox.showinfo('結果',stock_name+'\n\n相関係数は'+str(result)+'です')




lbl = tkinter.Label(text='株価コード')
lbl.place(x=40, y=70)
txt = tkinter.Entry(width=20)
txt.place(x=120, y=70)
lbl2 = tkinter.Label(text='信用倍率と株価の相関係数を調べます。\n4ケタの株価コードを入力してください。')
lbl2.place(x=40, y=120)

btn = tkinter.Button(tki, text='実行' ,command=soukankeisu) 
btn.place(x=300, y=300) 


tki.mainloop()
