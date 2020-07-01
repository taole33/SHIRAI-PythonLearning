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


N = 2


tki = tkinter.Tk()
tki.geometry(f'500x{200*N}') 
tki.title('対象の飲食チェーンを選択')
months = ['1','2','3','4','5','6','7','8','9','10','11','12']


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


def food_chain_graph(combo_get, fig):
    sales = get_sales(combo_get)
    ax = fig.add_subplot(111)
    ax.plot(months,sales,label=combo_get,marker='o')

    
def plot_graph():
    fig = plt.figure(figsize=(12,8))
    ax = fig.add_subplot(111)
    ax.plot(months, [100] * 12)
    for i in range(0, N):
        combo_get = combos[i].get()
        food_chain_graph(combo_get, fig)
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
        
combos = []
for i in range(0, N):
    lbl = tkinter.Label(tki,text=f'飲食チェーンを選んでください({i+1})')
    lbl.place(x=40, y=100 + i * 90)
    combos.append(ttk.Combobox(tki, state='readonly'))
    combos[i]['values']=food_chain
    combos[i].current(0)
    combos[i].pack()
    combos[i].place(x=40, y=120 + 100 * i) 
    
    
lbl = tkinter.Label(tki,text=f'{N}個の飲食チェーンの対前年比売上高を比較します')
lbl.place(x=40, y=130*N)
btn = tkinter.Button(tki, text='実行',command=plot_graph) 
btn.place(x=300, y=300) 
tki.mainloop()
