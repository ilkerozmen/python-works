import mysql.connector   # Mysql de Foreign key oluşturmak için 22.21 izle !

connection = mysql.connector.connect(
        host = "localhost",   
        user = "root",
        password = "wasd16",
        database = "schooldb"
    )

# sql = "Select * From student"
# sql = "Select * From school"
# sql_join = "Select * From student inner join school on school.Id=student.schoolId"
# sql_join = "Select student.Name, student.Surname, school.Name From student inner join school on school.Id=student.schoolId"
sql_join = "Select st.Name, st.Surname, sc.Name From student as st inner join school as sc on sc.Id=st.schoolId"

mycursor = connection.cursor()
mycursor.execute(sql_join)

try:
    result = mycursor.fetchall()
    for i in result:
        print(i)
except mysql.connector.Error as err:
    print("Hata: ", err)
finally:
    connection.close()