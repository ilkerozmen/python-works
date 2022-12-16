import pandas as pd
"""
customers = {
    'CustomerID': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

orders = {
    'OrderID': [10,11,12,13],
    'CustomerID': [1,2,5,7],
    'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
}

df_customers = pd.DataFrame(customers, columns=["CustomerID","FirstName","LastName"])
df_orders = pd.DataFrame(orders, columns=["OrderID","CustomerID","OrderDate"])

print(df_customers)
print(df_orders)

result = pd.merge(df_customers, df_orders,how="inner")   # inner join olarak 2 tabloyu birleştirir. Yani siparişi olan mişteriler gelir.
result = pd.merge(df_customers, df_orders,how="left")    # left join olarak 2 tabloyu birleştirir. Müşterilerin hepsi gelir fakat siparişi olmayanların sipariş değerleri NaN gelir.
result = pd.merge(df_customers, df_orders,how="right")    # left join olarak 2 tabloyu birleştirir. Çok bir mantığı yok.
result = pd.merge(df_customers, df_orders,how="outer")    # Ortak kayıt olsun olmasın tüm kolonlar birleştirirlir.
"""

customerA = {
    'CustomerID': [1,2,3,4],
    'FirstName': ["Ahmet","Ali","Hasan","Canan"],
    'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customerB = {
    'CustomerID': [4,5,6,7],
    'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
    'LastName': ["Bilge","Turan","Yılmaz","Taşçı"]
}

df_customerA = pd.DataFrame(customerA, columns=["CustomerID","FirstName","LastName"])
df_customerB = pd.DataFrame(customerB, columns=["CustomerID","FirstName","LastName"])

result = pd.concat([df_customerA,df_customerB])  # default axis = 0  => Yani alt alta ekleme yapar. Yanyana için axis=1

print(result)