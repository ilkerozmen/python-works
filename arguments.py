'''
def change(n):
    n[0] = 'istanbul'
sehirler = ['ankara', 'izmir']
change(sehirler[:])                      # slicing (parçalayıp) n değişkenine atar. Bu işlem listedeki değerlerin ojinal kalması için yapılır.
print(sehirler)
'''

'''
def add(*params):
    return sum((params))                                     # sum toplama metodudur.
print(add(10,20,30,40,50,60,70,80,90,100))                   # hesaplamak için sınırsız parametre girilebilir.
'''

'''
def displayUser(**args):                         # ** koyarak dictionary türünde işlem yapılmak sağlanmaktadır.
    for key, value in args.items():
        print("{} is {}".format(key,value))
displayUser(name='İlker', age=2, city='Bursa')
displayUser(name='Ayşe', age=10, city='İstanbul', phone='12316454')
displayUser(name='Ali', age=89, city='Ankara', phone='8979465', mail='ali@gmail.com')
'''