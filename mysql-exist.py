import mysql.connector   # insert metodu liste yöntemi için 22.11 izle

# sql_insert = "INSERT INTO Exist (Date, Time, TL) VALUES (%s,%s,%s)"
# values = ("ali", "veli", "49")

# exist_data = connection.cursor()
# exist_data.execute(sql_insert,values)

def save_exist_db():

    connection = mysql.connector.connect(             # DB connection bilgileri.
        host = "localhost",   # 192.23.45.56   örnek internet adresi
        user = "root",
        password = "wasd16",
        database = "rowdata"
    )

    with open("D:\ARGE\data_project\exist.txt", "r", encoding="utf-8") as line:
        content = line.readlines()
        for i in range(24):
            column1 = content[i].split(" ")
            ex_date = column1[0]
            ex_time = column1[1]
            ex_tl = column1[2]
            # print(f"Date: {ex_date}, Time: {ex_time}, TL: {ex_tl}")
            exist_data = connection.cursor()  # DB connection komutu
            exist_data.execute(
                "INSERT INTO exist (Date, Time, TL) VALUES (%s,%s,%s)",(ex_date,ex_time,ex_tl))
            
    try:
        connection.commit()   # sorgu sql e gönderirlir.
    except mysql.connector.Error as err:
        print('Hata: ', err)
    finally:
        connection.close()
    print('Database bağlantısı kapandı.')

save_exist_db()