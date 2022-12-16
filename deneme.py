import requests, time, datetime, os, sqlite3
from bs4 import BeautifulSoup

global now_date, exist_date

now_date = None
exist_date = None

class DB_PATH:
    exist_path = "D:\ARGE\data_project\data\RowData.db"

def get_exist():
    url = "https://seffaflik.epias.com.tr/transparency/piyasalar/gip/gip-agirlikli-ortalama-fiyat.xhtml"
    html = requests.get(url).content
    soup = BeautifulSoup(html, "html.parser")
    list = soup.find_all("tr",{"class":"ui-widget-content ui-datatable-even"}) + soup.find_all("tr",{"class":"ui-widget-content ui-datatable-odd"})


    with open("exist.txt", "w",encoding="utf-8") as file:
        for tr in list:
            date = tr.text[0:10]
            hour = tr.text[10:15]
            tl = tr.text[15:]
            file.write(date+" "+hour+" "+tl+"\n")

def get_nowdate():
    global now_date, exist_date
    date = datetime.datetime.now()
    now_date = datetime.datetime.strftime(date,'%Y/%m/%d')

    if now_date != exist_date:
        exist_date = now_date
        get_exist()
        save_exist_db()


def save_exist_db():
    AFileName = DB_PATH.exist_path
    global now_date, exist_date

    if (os.path.exists(AFileName) == False): raise Exception(AFileName + " does not exists !")
    exist_db = sqlite3.connect(AFileName, check_same_thread=False)
    exist_db.row_factory = sqlite3.Row
    exist_db.isolation_level = None

    with open("D:\ARGE\data_project\exist.txt", "r", encoding="utf-8") as line:
        content = line.readlines()
        for i in range(24):
            column1 = content[i].split(" ")
            ex_time = column1[1]
            ex_date = now_date +" "+ ex_time
            ex_tl = column1[2]
            # print(f"Time: {ex_date}, TL: {ex_tl}")
            exist_data = exist_db.cursor()
            exist_data.execute(
                #"INSERT INTO Exist (Date, Time, TL) VALUES (?,?,?)",(ex_date,ex_time,ex_tl))
                "UPDATE Exist SET Date=?, Time=?, TL=? WHERE ID=?", (ex_date, ex_time, ex_tl, i+1))

if __name__ == '__main__':
    try:
        get_nowdate()
        while True:
            time.sleep(0.5)

    except Exception as err:
        print(err)