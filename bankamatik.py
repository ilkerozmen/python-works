ilkerHesap = {                             # Basit bankamatik uygulaması
    'ad': 'İlker ÖZMEN',
    'hesapNo': '123456789',
    'bakiye': 3000,
    'ekHesap': 2000
}
aliHesap = {
    'ad': 'Ali TAŞ',
    'hesapNo': '789456123',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paracek(hesap,miktar):
    print(f"Merhaba {hesap['ad']}")
    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']
        if (toplam >= miktar):
            ekHesapKullanimi = input('Ek Hesap kullanılsın mı ? (E/H)')
            if (ekHesapKullanimi == 'E'):
                ekhesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekhesapKullanilacakMiktar 
                print("Paranızı alabilirsiniz.")
            else:
                print(f"{hesap['hesapNo']} numaralı hesabınızın bakiyesi {hesap['bakiye']} TL dir.")
        else:
            print("Üzgünüz, bakiyeniz yetersiz.")

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır.\nEk hesap limitiniz {hesap['ekHesap']} TL dir.")
    print("*************************************************")


i=3
while i > 0:
    i-=1
    x = int(input(f"{ilkerHesap['ad']} çekmek istediğiniz miktarı giriniz: "))
    paracek(ilkerHesap,x)
    bakiyeSorgula(ilkerHesap)
