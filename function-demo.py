'''                                   # Girilen kelimeyi istenilen kadar ekrana yazdırır.
x = input("İsminizi giriniz: ")
a = int(input("Kaç kez ekrana yazdırmak istediğinizi giriniz: "))
def isim(x,a):
        print(a*x)
isim(x,a)
'''

'''
def listeyeCevir(*params):             # Farklı türden değişkenleri liste şeklinde ekrana yazdırır.
    liste=[]
    for param in params:
        liste.append(param)
    return liste
result = listeyeCevir(10,20,30,'Merhaba') 
print(result)
'''

'''
def asalSayiBul(sayi1,sayi2):                    # girilen iki sayı arasındaki asal sayıları ekrana yazdırır.
    for sayi in range(sayi1, sayi2+1):
        if sayi > 1:
            for i in range (2, sayi):
                if (sayi % i ==0):
                    break
            else:
                print(sayi)

sayi1 = int(input("Bir sayı giriniz: "))                   
sayi2 = int(input("Bir sayı giriniz: ")) 

asalSayiBul(sayi1,sayi2)
'''

'''
def tamBolen(sayi):                    # girilen iki sayı arasındaki asal sayıları ekrana yazdırır.
    tamBolenler = []
    for i in range(1,sayi+1):
        if (sayi % i == 0):
            tamBolenler.append(i)
    return tamBolenler    

sayi = int(input("Bir sayı giriniz: "))                   
print(tamBolen(sayi))
'''