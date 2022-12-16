import mysql.connector


def get_student():
    connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "wasd16",
            database = "schooldb"
        )

    mycursor = connection.cursor()
    # mycursor.execute('SELECT * FROM student')   # Tüm kolonlar
    # mycursor.execute('SELECT StudentNumber, Name, Surname FROM student')  # Seçilen kolonlar
    # mycursor.execute('SELECT * FROM student ORDER BY StudentNumber DESC')   # okul numarasına göre azalan sıra ile getirir.
    # mycursor.execute('SELECT * FROM student ORDER BY StudentNumber, Name')   # Önce okul numarasına sonra isme göre artan sıralanır.
    # mycursor.execute('SELECT StudentNumber, Name, Surname FROM student where Id=1')    # where kullanımı.
    mycursor.execute("SELECT * FROM student where Name LIKE '%Ali%'")  # Name kolonunda Ali kelimesi geçen tüm kayıtları getirir.
    result = mycursor.fetchall()   # birden fazla kayıt almak için kullanılan metod.
    # result = mycursor.fetchone()     # sorgu şartından gelecek ilk kayıt.
    # print(f'Number: {result[0]} Name: {result[1]} Surname: {result[2]}')

    for i in result:
        print(f'Number: {i[1]} Name: {i[2]} Surname: {i[3]}')


# get_student()

def get_studentsById(id):      # gönderilen ID bilgisine göre kayıt getirme.
    connection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "wasd16",
            database = "schooldb"
        )

    mycursor = connection.cursor()

    select_sql = "SELECT * FROM student WHERE Id=%s"
    # select_sql = "SELECT COUNT(*) FROM student"   # Count kullanımı.
    # select_sql = "SELECT AVG(StudentNumber) FROM student"   # Average (Ortalama) kullanımı.
    # select_sql = "SELECT SUM(StudentNumber) FROM student"   # SUM (Toplam) kullanımı.
    # select_sql = "SELECT MIN(StudentNumber) FROM student"   # MIN (Minimum) kullanımı.
    # select_sql = "SELECT MAX(StudentNumber) FROM student"   # MAX (Maksimum) kullanımı.
    # select_sql = "SELECT Name FROM student WHERE StudentNumber = (SELECT MAX(StudentNumber) FROM student)"   # numarası en büyük olan öğrencinin adı.
    params = (id,)

    mycursor.execute(select_sql,params)
    result = mycursor.fetchone()
    print(f'Number: {result[0]} Name: {result[1]} Surname: {result[2]}')

get_studentsById(1)