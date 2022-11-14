import requests                    # exist şeffaflık platformuna bağlanarak o gün kü gip değerini çekerek ekrana yazdırır.
from bs4 import BeautifulSoup

url = "https://seffaflik.epias.com.tr/transparency/piyasalar/gip/gip-agirlikli-ortalama-fiyat.xhtml"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

#list = soup.find_all("tr",{"role":"row"})
list = soup.find_all("tr",{"class":"ui-widget-content ui-datatable-even"}) + soup.find_all("tr",{"class":"ui-widget-content ui-datatable-odd"})

for tr in list:
    date = tr.text[0:10]
    hour = tr.text[10:15]
    tl = tr.text[15:]
    print(f"Tarih: {date} Saat: {hour} TL: {tl}")
