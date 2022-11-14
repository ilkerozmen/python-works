"""
import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")     # json formatında veri barındıran bir siteye get yaparak bağlantı talebinde bulunduk.
result = json.loads(result.text)      # gelen string veriyi json listesi haline çevirdik.

for i in result:              # gelen listedeki userId si 1 olan verilerin title kısmını alt alta yazdırdık.
    if i["userId"] == 1:
        print(i["title"])
"""