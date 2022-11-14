import requests        # istenilen miktarda parayı, istenilen para biriminde yine istenilen para birimine çevirir.
import json


def get_url():
    
    headers = {"apikey": "Y8e78YK3nStIg0K3xJwkGZ0wvDuPvPMP"}
    url = 'https://api.apilayer.com/exchangerates_data/latest?base='+str(b_doviz)     # b_doviz

    response = requests.request("GET", url, headers=headers)
    status_code = response.status_code
    result = json.loads(response.text)
    a = result["rates"]
    birim = a[a_doviz]
    print(birim)
    sonuc = int(how_much)*float(birim)
    print('1 '+ b_doviz + ' = ' + str(birim)+ ' '+ str(a_doviz))
    print(str(how_much)+' '+ b_doviz + ' = '+ str(sonuc)+ ' '+ a_doviz)


while True:
    b_doviz = input("bozulan döviz türü (çıkmak için q giriniz.): ")
    if b_doviz == 'q':
        break
    a_doviz = input("alınan döviz türü: ")
    how_much = input("Ne kadar USD bozdurmak istiyorsunuz?: ")
    get_url()
