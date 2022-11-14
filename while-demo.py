'''
sayilar = [1,3,5,7,9,12,19,21]                    # ekrandaki sayıları yazdırır.
x=0
while x<=(len(sayilar)-1):
    print(sayilar[x])
    x = x+1
print('Bitti.')  
'''

'''
a = int(input("Bir sayı giriniz: "))                                 # girilen 2 sayı arasındaki tek sayıları yazdırır.
b = int(input("İlk sayıdan daha büyük bir sayı giriniz: "))

while a<=b:
    if a%2==1:
        print(a)
    a = a+1
print("Bitti.") 
'''

'''
x = 100                      # 100 den 0 a kadar olan sayıları azalarak yazdırır.
while 0<=x<=100:
    print(x)
    x = x-1
print("Bitti.")
'''

'''                                                   # girilen 5 sayıyı büyükten küçüğe doğru sıralar.
sayı=0
a=1
x=[]
while a<=5:                   
    sayı = int(input(f"{a}. sayıyı giriniz: "))
    x.append(sayı)
    a= a+1
x.sort()
print(x)
'''

'''                                  # adedi kullanıcı tarafından belirlenen ürünlerin adını ve fiyat bilgilerini ekrana yazdırır.
urun = ''
fiyat = ''
sayi = int(input("Gireceğiniz ürün adedini belirleyiniz: "))
x = 1  
urunler = []                    
while x<=sayi:                                                            
    urun = input("Ürün adını giriniz: ")
    price = input("Fiyatını giriniz: ")
    urunler.append({
        'urun': urun,
        'fiyat': price
    })
    x = x+1
for urun in urunler:
    print(f"Ürün adı: {urun['urun']}, ürün fiyatı: {urun['fiyat']}")
'''