# x = float(input("Bir sayı giriniz: "))                                     # Bir sayının 0 ile 100 arasında olup olmadığını gösterir.
# result = (x>0) and (x<100)
# print(f"Sayı 0 ile 100 arasında mı ? : {result}")
'''
if 0<x<100:
    print("Girdiğiniz sayı sıfır ile 100 arsındadır.")                   # Alternatif yol
else:
    print("Girdiğiniz sayı sıfır ile 100 arasında değildir.")
'''

'''
x = float(input("Bir sayı giriniz: "))                         # Bir sayının pozitif çift sayı olup olmadığını gösterir.
y = (x%2)
result = (y==0) and (x>0)
print(f"Sayı pozitif çift sayı mı ? : {result}")
'''

'''
x = input("Lütfen e-mail adresinizi giriniz: ")               # Girilen e-mail ve parolanın doğruluğunu sorgular.
y = input("Lütfen parolanızı giriniz: ")
email = "ilkerozmenn@gmail.com"
parola = "123456"
result = (x==email) and (y==parola)
print(f"E-mail adresi ve parola doğru mu ? : {result}")
'''

'''
x = float(input("Bir sayı giriniz: ")) 
y = float(input("İkinci sayıyı giriniz: "))                     # Girilen üç sayının en büyük olanını sorgular.
z = float(input("Üçüncü sayıyı giriniz: ")) 
result = (x>y) and (x>z)
print(f"İlk sayı en büyüktür. {result} ")
result = (y>x) and (y>z)
print(f"İkinci sayı en büyüktür. {result} ")
result = (z>x) and (z>y)
print(f"Üçüncü sayı en büyüktür. {result} ")
'''

'''
vize1 = float(input("Lütfen 1. vize notunuzu giriniz: "))               # Girilen vize ve final notunun ortalamasını heaplar.
vize2 = float(input("Lütfen 2. vize notunuzu giriniz: "))
final = float(input("Lütfen final notunuzu giriniz: "))

ortalama = (((vize1+vize2)/2)*0.6)+(final*0.4)
print("Öğrenci ortlaması: ", ortalama)
result = (ortalama>=50 and final>=50) or (final>=70)       # ortalama 50 olsa bile final notu en az 50 olmalı / eğer finalden 70 aldıysa ortalama önemli değil
print(f"Derten geçer not aldı mı ? {result}")
'''

'''
ad = input("Lütfen adınızı giriniz: ")             # Kişi bilgilerini alıp kilo endeksi hesaplar.
kg = float(input("Lütfen ağırlığınızı kilogram giriniz: "))
boy = float(input("Lütfen boy uzunluğunuzu metre cinsinden giriniz: "))

index = (kg) / (boy**2)
zayif = (index>=0) and (index<=18.4)
normal = (index>=18.5) and (index<=24.9)
fazla_kilolu = (index>=25) and (index<=29.9)
obez = (index>=30) and (index<=34.9)
print(f"{ad} kilo endeksiniz: {index} ve kilo değerlendirmeniz: zayıf {zayif}")
print(f"{ad} kilo endeksiniz: {index} ve kilo değerlendirmeniz: normal {normal}")
print(f"{ad} kilo endeksiniz: {index} ve kilo değerlendirmeniz: fazla kilolu {fazla_kilolu}")
print(f"{ad} kilo endeksiniz: {index} ve kilo değerlendirmeniz: şişman {obez}")
'''