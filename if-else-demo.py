'''
ad = input("Lütfen adınızı giriniz: ")                       # Kullanıcının eğitim durumu ve yaşına göre ehliyet alma durumunu gösterir.
egitim = input("Lütfen eğitim seviyenizi giriniz: ")
yas = int(input("Lütfen yaşınızı giriniz: "))
seviye = ['lise','üniversite']
if (egitim == seviye[0] or egitim==seviye[1]):
    if yas>=18:   
        print(f"{ad} ehliyet alabilirsin.")
    else:
        print(f"{ad} yaşın 18 den büyük olmadığı için ehliyet alamazsın.")
else:
    print(f"{ad} eğitim seviyen lise veya üniversite olmadığı için ehliyet alamazsın.")
'''

'''
exam1 = input("Birinci yazılı notunuzu giriniz: ")                     # 2 yazılı ve 1 sözlü notuna göre ağırlıklı not ortalamasını ve notu hesaplar.
exam2 = input("İkinci yazılı notunuzu giriniz: ")
quiz = input("Sözlü notunuzu giriniz: ")
e1 = exam1.isnumeric()
e2 = exam2.isnumeric()
q = quiz.isnumeric()
if (e1==True and e2==True and q==True):
    exam1 =float(exam1)
    exam2 = float(exam2)
    quiz = float(quiz)
    if 0<=exam1<=100 and 0<=exam2<=100 and 0<=quiz<=100:
        ortalama = ((exam1+exam2+quiz)/3)
        if 0<=ortalama<=24:
            print(f"Ağırlıklı not ortalamanız: {ortalama} ve notunuz: 0")
        elif 25<=ortalama<=44:
            print(f"Ağırlıklı not ortalamanız: {ortalama} ve notunuz: 1")
        elif 45<=ortalama<=54:
            print(f"Ağırlıklı not ortalamanız: {ortalama} ve notunuz: 2")
        elif 55<=ortalama<=69:
            print(f"Ağırlıklı not ortalamanız: {ortalama} ve notunuz: 3")
        elif 70<=ortalama<=84:
            print(f"Ağırlıklı not ortalamanız: {ortalama} ve notunuz: 4")
        elif 85<=ortalama<=100:
            print(f"Ağırlıklı not ortalamanız: {ortalama} ve notunuz: 5")
    else:
        print("Gridiğiniz değerler 0 ile 100 arasında olmalıdır.")
else:
    print("Lütfen sayı değerleri giriniz.")
'''

'''
from datetime import datetime                                   # Girilen aracın trafiğe çıkış tarihi ile bakım aralığını gösterir.
bugun = datetime.today()
# bugun = datetime.strftime(tarih, '%d %B %Y')
# print(bugun)
arac = input("Aracınızın trafiğe çıkış tarihini yıl.ay.gün (XX.XX.XXXX) formatında giriniz: ")
arac = arac.split('.')
yıl = int(arac[2])
ay = int(arac[1])
gun = int(arac[0])
aractarih = datetime(yıl, ay, gun)
aracfark = bugun - aractarih
fark = aracfark.days
if fark<=365:
    print("1. servis aralığı")
elif fark>365 and fark<=365*2:
    print("2. servis aralığı")
elif fark>365*2 and fark<=365*3:
    print("3. servis aralığı")
else:
    print("Hatalı tarih girdiniz.")
'''