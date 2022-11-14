sayilar = [1,3,5,7,9,12,19,21]
sonuc = []

'''
for x in sayilar:                     # 3 ebölünebilen sayıları yazdırır.
    if  x%3==0:
        sonuc.append(x)
    else:
        print("None")
print(sonuc)
'''

'''
a=0
for x in sayilar:                    # sayıların toplamını yazdırır.
    a += x 
print(a)
'''

'''
for x in sayilar:                     # tek sayıların karesini yazdırır.
    if  x%2==1:
        sonuc.append(x**2)
    else:
        print("None")
print(sonuc)
'''

'''
sehirler = ['kocaeli','istanbul','ankara','izmir','rize']          # verilen şehirlerden en fazla 5 karakterli olanları ekrara yazdırır.

for x in sehirler:
    if (len(x)<=5):
        print(x)
'''

urunler = [
    {'name':'samsung S6', 'price': '3000' },
    {'name':'samsung S7', 'price': '4000' },
    {'name':'samsung S8', 'price': '5000' },
    {'name':'samsung S9', 'price': '6000' },
    {'name':'samsung S10', 'price': '7000' }
]

'''
a =0                             # verilen telefonların fiyatlarının toplamını verir.
for x in urunler:
    b = int(x['price'])
    a += b
print(a)
'''

'''                    
for x in urunler:                     # verilen telefonların fiyatlarının en fazla 5000 olan ürünleri gösterir.
    b = int(x['price'])
    if b<=5000:
        sonuc.append(x)
        print(x)
'''

