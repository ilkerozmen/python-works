'''
x = int(input("İlk sayıyı giriniz: "))
y = int(input("İkinci sayıyı giriniz: "))          # Girilen 2 sayıdan hangisinin büyük olduğunu gösterir.
if x>y:
    print("İlk sayı büyüktür.")
elif x<y:
    print("İkinci sayı büyüktür.")
else:
    print("x ve y birbirine eşittir.")
'''

'''
vize = int(input("Vize notunu giriniz: "))                  # Vize ve final notunun ortalamasını hesaplar.
final = int(input("Final notunu giriniz: "))
ortalama = (vize*0.6)+(final*0.4)
print("Ortalamanız: ", ortalama)
if ortalama>50:
    print("Dersi geçtiniz.")
else:
    print("Dersten kaldınız.")
'''

'''
x = input("Bir sayı giriniz: ")                # Girilen sayının tek mi çift mi olduğunu söyler.
islem = (float(x))%2
if islem == 0:
     print("Girdiğiniz sayı çifttir.")
elif islem == 1:
     print("Girdiğiniz sayı tektir.")
else:
    print("İstenmeyen değer girdiniz.")
'''

'''
x = float(input("Bir sayı giriniz: "))                 # Girilen sayının negatif veya pozitif olduğunu gösterir.
if x>0:
    print("Girdiğiniz sayı pozitiftir.")
elif x<0:
    print("Girdiğiniz sayı negatiftir.")
else:
    print("Girdiğiniz sayı 0' dır.")
'''

'''
x = input("Lütfen e-mail adresinizi giriniz: ")                Girilen e-mail ve parolanın doğruluğunu sorgular.
y = input("Lütfen parolanızı giriniz: ")
if x == "ilkerozmenn@gmail.com" and y== "123456789":
    print("Girmiş olduğunuz e-mail adresi ve parolanız doğru.")
else:
    print("Girmiş olduğunuz e-mail adresi ve parolanız yanlış.")
'''
