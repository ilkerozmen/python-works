import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,45,25],
    "Column3": ["abc","bca","ade","cba","dea"]
}

df = pd.DataFrame(data)

def kareal(x):
    return x*x

kareal2 = lambda x: x*x

result = df
result = df["Column2"].unique()   # kolon2 içindeki tekrarlayan değerleri 1 kez alır.
result = df["Column2"].nunique()   # kolon2 içindeki tekrarlayan değerleri 1 kez alarak toplam kaç farklı eleman olduğunu söyler.
result = df["Column2"].value_counts()   # kolon2 de hangi elemandan kaç adet olduğunu söyler.
result = df["Column1"].apply(kareal)   # kolon1 deki elemanları kareal fonksiyonuna gönderir ve dönen sonucu yazdırır.
result = df["Column1"].apply(kareal2)   # yukarıdaki işlemin aynısı. 

df["Column4"] = df["Column3"].apply(len)    # Kolon3 deki verilerin kaç karakterden oluştuğunu söyler ve kolon 4 e yazar.

result = df.columns
result = len(df.columns)
result = df.index
result = len(df.index)
result = df.info

result = df.sort_values("Column2")   # Kolon2 ye göre artan sıralayarak getirir. => SQL order by gibi.  # default ascending=True
result = df.sort_values("Column3")   # kolon3 de alfabetik sıraya göre sıralanır.
result = df.sort_values("Column2", ascending=False)   # Kolon2 ye göre azalan sıralayarak getirir.

print(result)

data2 = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

dff =pd.DataFrame(data2)
print(dff.pivot_table(index="Ay", columns="Kategori", values="Gelir"))   # Kategori bazında aylık satış verilerini listeler.
