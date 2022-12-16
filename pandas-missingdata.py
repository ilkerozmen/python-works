import pandas as pd
import numpy as np

data = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(data, index=['a','c','e','f','h'], columns=['column1','column2','column3'])
df = df.reindex(['a','b','c','d','e','f','g','h'])
newColumn = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df['column4'] = newColumn

result = df
result = df.drop("column1",axis=1)  # kolon1 i siler
result = df.drop(["column1","column2"],axis=1)  # kolon1 ve kolon2 yi siler
result = df.drop("a",axis=0)  # a index satırını siler
result = df.isnull()   # değerleri NaN olan verileri True veya False olarak söyler
result = df.notnull()    # değerleri NaN olmayan verileri True veya False olarak söyler
result = df.isnull().sum()   # kolonlarda kaç adet NaN değerin olduğunu gösterir.
result = df["column1"].isnull().sum()   # kolon1 deki NaN değerlerin adedi
result = df[df["column1"].isnull()]["column1"]   # kolon1 de NaN olan satırları gösterir.
result = df[df["column1"].notnull()]["column1"]   # kolon1 de NaN olmayan satırları gösterir.
result = df.dropna()   # axis = 0 =>  verilerinde NaN olan satırları otomatik olarak siler. !!!!!!!!!!
result = df.dropna(axis=1)   # sütuna göre siler.
result = df.dropna(how = "any")    # herhangibir NaN değer olan satırı komple siler.
result = df.dropna(how = "all")    # tüm satır NaN ise o satırları siler.
result = df.dropna(subset = ["column1","column2"], how = "all")  # kolon1 ve kolon2 nin ikisinde de NaN değeri olan satırları siler.
result = df.dropna(subset = ["column1","column2"], how = "all")   # kolon1 ve kolon2 nin herhangibirinde NaN değeri olan satırları siler.
result = df.dropna(thresh=2)   # satırlarda en az 2 adetten fazla veri varsa o satırları gösterir.
result = df.dropna(thresh=4)   # satırlarda en az 4 adetten fazla veri varsa o satırları gösterir.
result = df.fillna(value='no input')     # NaN değerlerin yerine 'no input' yazar.
result = df.fillna(value=0)     # NaN değerlerin yerine '0' yazar.

def ortalama(df):      # tablodaki tüm değerlerin ortalamasını alır.
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet

result = df.fillna(value=ortalama(df))   # NaN değerler yerine hesaplanan tüm değerlerin ortalaması yazdırıldı.

print(result)