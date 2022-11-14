'''
x = 0             # 0 dan 100 e kadar olan sayıları yazdırır.
while x<=100:
    print(x)
    x = x+1
print("Bitti.")
'''

'''
x = 0              # 0 den 100 e kadar olan çift ve tek sayıları belirterek yazdırır.
while x<=100:
    if x%2==0:
        print(f'Çift sayı: {x}')
    else:
        print(f"Tek sayı: {x}")
    x = x+1
print("Bitti.")
'''

'''
name = ''                                 # kullanıcıdan isim girişi alana kadar giriiş bilgisi ister.
while not name.strip():                   # .strip komutu kullanıcının sadece boşluk karakteri girmesini engeller.
    name = input("İsminizi giriniz: ")
print(f"Merhaba {name}")
'''