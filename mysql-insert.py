import mysql.connector    # nesne tabanlı kayıt işlemi için 22.12 izle
import datetime

connection = mysql.connector.connect(             # DB connection bilgileri.
        host = "localhost",   # 192.23.45.56   örnek internet adresi
        user = "root",
        password = "wasd16",
        database = "schooldb"
    )

sql_insert = "INSERT INTO student (StudentNumber, Name, Surname, Birthdate, Gender) VALUES (%s,%s,%s,%s,%s)"
ogrenciler = [
    ("101", "Ahmet", "Yılmaz", datetime.datetime(2005, 5, 17), "E"),
    ("102", "Ali", "Can", datetime.datetime(2005, 6, 17), "E"),
    ("103", "Canan", "Tan", datetime.datetime(2005, 7, 7), "K"),
    ("104", "Ayşe", "Taner", datetime.datetime(2005, 9, 23), "K"),
    ("105", "Bahadır", "Toksöz", datetime.datetime(2004, 7, 27), "E"),
    ("106", "Ali", "Cenk", datetime.datetime(2003, 8, 25), "E")
]

mycursor = connection.cursor()
mycursor.executemany(sql_insert,ogrenciler)   # liste şeklinde çoklu veri gönderimi için executemany kullanılır.

try:
    connection.commit()
    print(f'{mycursor.rowcount} tane kayıt eklendi.')
except mysql.connector.Error as err:
    print("Hata: ", err)
finally:
    connection.close()