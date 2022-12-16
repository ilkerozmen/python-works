import pymongo
from bson.objectid import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://ilkerozmenn:asdf16@cluster0.uncesom.mongodb.net/rowdata?retryWrites=true&w=majority")  # uzak server bağlantı linki.
# myclient = pymongo.MongoClient("mongodb://localhost:27017")  # localhost bilgileri
mydb = myclient["rowdata"]   #  oluşturduğumuz db ye bağlantı.
mycollection = mydb["exist"]

# print(myclient.list_database_names())  #  database lerin isimlerini gösterir.
# print(mydb.list_collection_names())  #  collection (tablo) ların isimlerini gösterir.

"""
with open("D:\ARGE\data_project\exist.txt", "r", encoding="utf-8") as line:
        content = line.readlines()
        for i in range(24):
            column1 = content[i].split(" ")
            ex_date = column1[0]
            ex_time = column1[1]
            ex_tl = column1[2]
            # print(f"Date: {ex_date}, Time: {ex_time}, TL: {ex_tl}")
            exist = {"Date":ex_date, "Time":ex_time, "TL":ex_tl}
            result = mycollection.insert_one(exist)
            # print(type(result))
            # print(result.inserted_id)   # kaydın kimliğini obje id sini verir.
"""


"""
list = [     # id bilgisini kendimiz de verebiliyoruz, vermezsek otomatik oluşuyor.
    {'_id':1, 'Date':'02.12.2022', 'Time':'00:00', 'TL':'3.811,03'},
    {'_id':2, 'Date':'02.12.2022', 'Time':'02:00', 'TL':'3.388,02'},
    {'_id':3, 'Date':'02.12.2022', 'Time':'04:00', 'TL':'3.236,49'},
    {'_id':4, 'Date':'02.12.2022', 'Time':'04:00', 'TL':'3.236,49', "Shift":["A","B","C"]}    
]

result = mycollection.insert_many(list)
print(result.inserted_ids)
"""


# result = mycollection.find_one()   # collection daki ilk kaydı getirir.
# result = mycollection.find()   # collection daki tüm kayıtları getirir. (for ile yazdırılır.)

# for i in mycollection.find({},{"_id":0,"Date":1, "Time":1, "TL":1}):  # {},{"_id":0}  aynı şeyi verir.
#     print(i)

# print(result)

# result = mycollection.find_one({"Time":"10:00"})  # Tek kayıt geleceği için find one kullanıldı.
# result = mycollection.find_one({"_id": ObjectId("638cfee27abcf4f708966577")})  # obje id filtre olarak kullanılması için 2. satırdaki kütüphane kullanılır ve strig ID ifadesi objeye dönüştürülür.

# result = mycollection.find({   # eşit olan değerleri getirir.
#     "Time": {
#         "$in" : ["00:00","01:00","02:00"]
#     }
# })

# result = mycollection.find({   # Büyük olan değerleri getirir.
#     "TL": {
#         "$gte" : 3.516   # Alandaki değerlerin sayısal (int) değer olması gerekmektedir!!!  
#     }
# })

# result = mycollection.find({   # eşit olan değerleri getirir.
#     "TL": {
#         "$eq" : 3.516   # Alandaki değerlerin sayısal (int) değer olması gerekmektedir!!!  
#     }
# })

# result = mycollection.find({   # küçük olan değerleri getirir.
#     "TL": {
#         "$lte" : 3.516   # Alandaki değerlerin sayısal (int) değer olması gerekmektedir!!!  
#     }
# })

# result = mycollection.find({   # TL alanı '4' ile başlayan kayıtları getirir.
#     "TL": {"$regex": "^4"}
# })


# result = mycollection.find().sort("Time",1)  # artan şekilde sıralama
# result = mycollection.find().sort("Time",-1)  # azalan şekilde sıralama
# result = mycollection.find().sort([('Time',1),('TL',-1)])  # 2 parametreye göre sıralama

# result = mycollection.update_one({'Time':'00:01'},{'$set':{'Time':'00:00'}})   # Time: 00:00 olan satırı bulup Time: 00:01 olarak günceller.(Tek kayıt için)
# result = mycollection.update_many({'Time':'00:01'},{'$set':{'Time':'00:00'}})   # çoklu kayıt güncelleme için.
# print(f'{result.modified_count} adet satır güncellendi.')

# result = mycollection.delete_one({'Time':'00:00'})  # koşula uyan ilk kaydı siler.
# result = mycollection.delete_many({'Time':'00:00'})  # koşula uyan tüm kayıtları siler.
# result = mycollection.delete_many({'Time': {'$regex':'^00'}})  # Time verisi 00 ile başlayan tüm kayıtları siler.
# print(f'{result.deleted_count} adet kayıt silindi.')

for i in mycollection.find():
    print(i)