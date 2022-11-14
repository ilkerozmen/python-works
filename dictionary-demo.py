'''
ogrenciler = {
    '120': {
        'ad': 'Ali',
        'soyad': 'Yılmaz',
        'telefon': '532 000 000 01'
    },
    '125': {
        'ad': 'Can',
        'soyad': 'Korkmaz',
        'telefon': '532 000 000 02'
    },
    '128' : {
        'ad': 'Volkan',
        'soyad': 'Yükselen',
        'telefon': '532 000 000 03'
    }
}
'''
ogrenciler = {}                             # kullanıcıdan alınan öğrenci bilgileri neticesinde sorgulanan öğrenci numarasına göre öğrenci bilgilerini gösterir

number = input('öğrenci no: ')
name = input('öğrenci adı: ')
surname = input('öğrenci soyadı: ')
phone = input('öğrenci telefon: ')

# ogrenciler[number] = {
#    'ad': name,
#    'soyad': surname,
#    'telefon': phone
#}

ogrenciler.update({                  # .update metodu birden fazla veriyi aynı listeye ekleyebilmektedir.
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})

number = input('öğrenci no: ')
name = input('öğrenci adı: ')
surname = input('öğrenci soyadı: ')
phone = input('öğrenci telefon: ')


ogrenciler.update({                  # .update metodu birden fazla veriyi aynı listeye ekleyebilmektedir.
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})
number = input('öğrenci no: ')
name = input('öğrenci adı: ')
surname = input('öğrenci soyadı: ')
phone = input('öğrenci telefon: ')


ogrenciler.update({                  # .update metodu birden fazla veriyi aynı listeye ekleyebilmektedir.
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})
# 100print(ogrenciler)

ogrno = input('öğrenci no: ')
ogrenci = (ogrenciler[ogrno])
print(ogrenci)
print(f"Aradığınız {ogrno} nolu öğrencinin adı: {ogrenci['ad']} soyadı: {ogrenci['soyad']} ve telefonu ise {ogrenci['telefon']} dur.")