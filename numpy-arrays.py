import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10)   # 1 ile 10 arasındaki sayılardan array oluşturur. (10 dahil değil)
# result = np.arange(10,100,3)  # 10 ile 100 arasındaki sayılardan 3 er artırarak array listesi oluşturur.
# result = np.zeros(10)  # 10 adet 0 dan oluşan array verir.
# result = np.ones(10) # 10 adet 1 den oluşan array verir.
# result = np.linspace(0,100,5) # 0 ile 100 arasını 5 eşit parçaya böler.
# result = np.linspace(0,5,5) # 0 ile 5 arasını 5 eşit parçaya böler.
# result = np.random.randint(0,10) # 0 ile 10 arasında random int sayı verir. (10 dahil değil)
# result = np.random.randint(20) # 0 dan balayıp 20 ye kadar random int sayı verir. (20 dahil değil)
# result = np.random.randint(1,10,3)  # 1 ile 10 arasında 3 adet random int sayı üretir.
# result = np.random.rand(5)  # 0 ile 1 arasında random 5 adet sayı üretir.
# result = np.random.randn(5) # 0 ile 1 arasında random 5 adet negatif sayılar da dahil olmak üzere üretir.
# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10)  # 5 e 10 luk bir matris oluşturur.

# print(np_multi.sum(axis=1))   # matristeki satırların toplamını verir.
# print(np_multi.sum(axis=0))   # matristeki sütunların toplamını verir.

rnd_numbers = np.random.randint(1,100,10)
# result = rnd_numbers.max()  # 1 - 100 arasında 10 adet random üretilen int sayı içerisinden en büyük olanı verir.
# result = rnd_numbers.min()  # 1 - 100 arasında 10 adet random üretilen int sayı içerisinden en küçük olanı verir.
# result = rnd_numbers.mean()  # 1 - 100 arasında 10 adet random üretilen int sayının ortalamasını verir.
# result = rnd_numbers.argmax()  # 1 - 100 arasında 10 adet random üretilen int sayı içerisinden en büyük olanın index numarasını verir.
result = rnd_numbers.argmin()  # 1 - 100 arasında 10 adet random üretilen int sayı içerisinden en küçük olanın index numarasını verir.

print(rnd_numbers)
print(result)