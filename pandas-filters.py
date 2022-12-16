import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])

result = df
result = df.columns   # dataframe içindeki kolonları verir.
result = df.head()    # default olarak ilk 5 kaydı getirir.
result = df.head(10)   # ilk 10 kayıt.
result = df.tail(10)    # son 10 kayıt gelir.
result = df["Column1"].head()
result = df[["Column1","Column2"]].head()
result = df[5:15][["Column1","Column2"]].head()

result = df > 50
result = df[df > 50]
result = df[df % 2 == 0]
result = df[df["Column1"]>50][["Column1","Column2"]]  # kolon1 deki 50 den yük değerler için, kolon1 ve kolon2 yi gösterir.
result = df[(df["Column1"]>50) & (df["Column1"]<=70)]   # kolon1 için 50 ve 70 arasındaki kayıtları getirir.
result = df[(df["Column1"]>50) | (df["Column2"]<=70)]
result = df.query("Column1 >= 50 & Column1 % 2 == 0")   # kolon 1 de 50 den büyük ve çift olan satırları getirir.

print(result)