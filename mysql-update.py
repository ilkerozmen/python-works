import mysql.connector

def update_student(id):
    connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "wasd16",
            database = "schooldb"
        )

    mycursor = connection.cursor()
    update_sql = "UPDATE student SET Name='İlker' WHERE Id=%s"
    params = (id,)
    mycursor.execute(update_sql,params)
    
    try:
        connection.commit()
        print(f'{mycursor.rowcount} tane kayıt güncellendi.')
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()

update_student(1)