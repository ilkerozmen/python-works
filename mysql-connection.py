import mysql.connector

connection = mysql.connector.connect(             # DB connection bilgileri.
    host = "localhost",   # 192.23.45.56   örnek internet adresi
    user = "root",
    password = "wasd16",
    database = "rowdata"
)

mycursor = connection.cursor()  # DB connection komutu

mycursor.execute("SHOW DATABASES")  # istenilen sql komutunu çalıştırmak için gerekli işlem. (print  için for döngüsü gerekli.)

for i in mycursor:
    print(i)

