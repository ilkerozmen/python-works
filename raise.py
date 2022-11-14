# x=10

# if x>5:
#     raise Exception ('x 5 den büyük olamaz!')

"""
def check_password(psw):
     import re
     if len(psw) < 8:
         raise Exception ("parola en az 7 karakter olmalıdır.")
     elif not re.search("[a-z]", psw):
         raise Exception ("parola küçük harf içermelidir.")
     elif not re.search("[A-Z]", psw):
         raise Exception ("parola büyük harf içermelidir.")
     elif not re.search("[0-9]", psw):
         raise Exception ("parola rakam içermelidir.")
     elif not re.search("[_@$]", psw):
         raise Exception ("parola alpha numeric karakter içermelidir.")
     elif re.search("\s", psw):
         raise Exception ("parola boşlık içermemalidir.")
     else:
         print("geçerli parola")

password = "12345678aA_"

try:
     check_password(password)
except Exception as ex:
    print(ex)
else:
     print("parola geçerli")
finally:
     print("Validation tamamlandı")

"""

class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor.")
        if len(year) != 4:
            raise Exception("year alanı fazla karakter içeriyor.")
        else:
            self.name=name
            self.yaer=year

p = Person('Aliiiiiiiiiiiiii', 1989)