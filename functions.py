'''
x = input("Adınızı giriniz: ")          # kullanıcıdan isim bilgisini alıp ekrana hello 'name' yazdıran foksiyon.
def sayHello(name):
    return 'Hello ' + name
msg = sayHello(x)
print(msg)
'''

'''
def total(num1, num2):                   # 2 sayıyı toplayan fonksiyon
    return num1 + num2
result = total(10,20)
print(result)
'''

'''
x = int(input("Doğum yılınızı giriniz: "))                      # Girilen doğum yılına ve isim bilgilerine göre emekliliğe kalan yılı hesaplar.
isim = input("Adınızı giriniz: ")

def yasHesapla(dogumYili):
    return 2021-dogumYili

def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f"{isim} emekliliğine {emeklilik} yıl kaldı.")
    else:
        print("Yanlış değer girdiniz.")

emekliligeKacYilKaldi(x,isim)
'''