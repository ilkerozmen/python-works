from typing import final
from unittest import result


liste = ["1","2","5a","10b","abcç","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
"""
for x in liste:
    try:
        result=int (x)
        print(result)
    except ValueError:
        print("Sayısal olmayan değer: ", x)
        continue
"""
# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.
"""
while True:
    sayi=input('sayi giriniz: ')
    if sayi == 'q':
        break
    
    try:
        result=float(sayi)
    except ValueError as e:
            print('Geçersiz değer!')
            print(e)
            continue
"""
# 3: Girilen parola içinde türkçe karakter hatası veriniz.
"""
def checkPassword(psw):
    
    turkce_karakterler = 'şçğüöıİ'

    for x in psw:
        if x in turkce_karakterler:
            raise TypeError ("Parola Türkçe karakter içermemelidir!")
        else:
            pass
    print('geçerli parola')

psw = input('Şifre giriniz: ')

try:
    checkPassword(psw)
except TypeError as error:
    print(error)
"""

# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.

def faktoriyel(x):
    x = int(x)

    if x<0:
        raise ValueError('Negatif değer!')
    result=1

    for i in range(1, x+1):
        result*=i
    return result

for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)
    except ValueError as err:
        print(err)
        continue
    print(y)