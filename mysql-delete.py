import mysql.connector

def del_student(id):
    connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "wasd16",
            database = "schooldb"
        )

    mycursor = connection.cursor()
    del_sql = "DELETE FROM student WHERE Id=%s"
    params = (id,)
    mycursor.execute(del_sql,params)
    
    try:
        connection.commit()
        print(f'{mycursor.rowcount} tane kayıt silindi.')
    except mysql.connector.Error as err:
        print("Hata: ", err)
    finally:
        connection.close()

del_student(1)