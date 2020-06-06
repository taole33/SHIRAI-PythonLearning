import tkinter
from tkinter import messagebox
from tkinter import ttk
import requests
from bs4 import BeautifulSoup as BS
import pandas
import urllib.parse
import numpy
import matplotlib.pyplot as plt
import japanize_matplotlib



tki = tkinter.Tk()
tki.geometry('500x400') 
tki.title('対象の飲食チェーンを選択')


def get_sales(combo_get):
    selected_number = chain_dict[combo_get]
    sales = []
    td = tr[selected_number].find_all('td')
    td_length = len(td)
    for i in range(0,td_length,1):
        sales_independ = td[0+i]
        sales_independ = sales_independ.text
        if not sales_independ == '\xa0':
            sales_independ = float(sales_independ) 
        else:
            sales_independ = None
        sales.append(sales_independ)
    if not td_length ==12:
        td_length = 12 - td_length
        for i in range(0,td_length,1):
            sales.append(None)
    return sales


def food_chain_graph():
    combo_get = combo.get()
    combo_get2 = combo2.get()
    sales = get_sales(combo_get)
    sales2 = get_sales(combo_get2)
    print(sales)
    months = ['1','2','3','4','5','6','7','8','9','10','11','12']
    fig = plt.figure(figsize=(8,4))
    ax1 = fig.add_subplot(111)
    ax2 = fig.add_subplot(111)
    ax3 = fig.add_subplot(111)
    ax1.plot(months,sales,label=combo_get,marker='o')
    ax2.plot(months,sales2,label=combo_get2,marker='o')
    ax3.plot(months,[100,100,100,100,100,100,100,100,100,100,100,100])
    
    plt.title('チェーン店　対前年同月比推移')
    plt.xlabel('月')
    plt.ylabel('売上対前年比（％）')
    plt.legend()

    plt.legend()
    plt.show()


food_chain = []
chain_dict = {}
html = requests.get('https://www.fb-soken.com/monthly_sales.html')
html2 = BS(html.content,'html.parser') 
if not html.status_code == 200:
    messagebox.showinfo('エラー','webページに問題が発生しました')
else:
    tr = html2.find_all('tr')
    tr_length = len(tr)
    
    for i in range(0,tr_length-2,3):
        chain_name = tr[1+i]
        chain_name = chain_name.find('th')
        chain_name = chain_name.text
        food_chain.append(chain_name)
        chain_dict[chain_name] = 1+i 


lbl = tkinter.Label(tki,text='飲食チェーンを選んでください(1)')
lbl.place(x=40, y=100)

combo = ttk.Combobox(tki, state='readonly')
combo['values']=food_chain
combo.current(0)
combo.pack()
combo.place(x=40, y=120) 

lbl2 = tkinter.Label(tki,text='飲食チェーンを選んでください(2)')
lbl2.place(x=40, y=190)

combo2 = ttk.Combobox(tki, state='readonly')
combo2['values']=food_chain
combo2.current(0)
combo2.pack()
combo2.place(x=40, y=220) 

lbl = tkinter.Label(tki,text='２つの飲食チェーンの対前年比売上高を比較します')
lbl.place(x=40, y=270)

btn = tkinter.Button(tki, text='実行',command=food_chain_graph) 
btn.place(x=300, y=300) 


tki.mainloop()
