# key - value
# 41 => kocaeli, 34 => istanbul
'''
sehirler = ['kocaeli', 'istanbul']                     # şehir bilgisine göre plaka kodu yazdırılmak isteniyor. Bu kod satırları uzun yöntemdir.
plakalar = [41, 34]                                    # ve şehirler ile plaka kodlarının aynı index numarasına sahip olması gerekmektedir.

print(plakalar[sehirler.index('kocaeli')])
print(plakalar[sehirler.index('istanbul')])
'''

'''
plakalar = {'kocaeli' : 41, 'istanbul': 34}            # 2. yöntem kısa olandır ve şehir bilgisini seçmek yeterlidir.

# plakalar['ankara'] = 6                               # bu kod satırı ile sonradan eleman eklenebilmektedir.

# print(plakalar['kocaeli'])
# print(plakalar['istanbul'])

print(plakalar)
'''

users = {                                          # farklı kişilerin bilgilerini girip elde etmek ve üzerilerinde değişiklik yapabilmek için
    'sadikturan' : {                               # dictionary liste yöntemleri kullanılmaktadır.
        'age' : 36,
        'roles' : ['user', 'admin'],
        'email' : 'sadikturan@gmail.com',
        'address' : 'kocaeli',
        'phone' : '123456789'
    },
    'cinarturan' : {
        'age' : 2,
        'roles' : ['user'],
        'email' : 'cinarturan@gmail.com',
        'address' : 'kocaeli',
        'phone' : '123456789'
    }
}
print(users['sadikturan'])
# print(users['sadikturan']['age'])
# print(users['sadikturan']['roles'][0])
