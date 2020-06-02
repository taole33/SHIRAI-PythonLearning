def download():
    import requests
    from bs4 import BeautifulSoup
    import zipfile
    from shutil import move
    import os
    image_page=0
    from tkinter import messagebox
    


    #対象URLからHTMLを入手
    HTML = requests.get('https://shopping.yahoo.co.jp/')
    #HMTLからimgだけ抜き出し
    soup = BeautifulSoup(HTML.text,'html.parser')
    IMG = soup.find_all('img')

    #zipの空ファイル作成
    filepath='./'+'TEST'+'.zip'
    zp = zipfile.ZipFile(filepath,'w')

    #forで一つ一つ画像を取得していく
    for i in range(len(IMG)):
        name='TEST'+str(i+1)+".jpg"
        #画像ファイルのURLを取得
        URL=IMG[i].get("src")
        image_page=requests.get(URL)
        if image_page.status_code==200:
            #画像を取得
            image = image_page.content
            with open(name,"wb") as A:
                A.write(image)
            #zipファイルへ
            zp.write(name)
            os.remove(name)
            #zipを指定の場所に移動（未実装）
 
        else:
            print('webサイトに何か問題があり停止しました')
    messagebox.showinfo('結果','完了しました')

download()

