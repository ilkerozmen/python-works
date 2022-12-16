import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])
result = numbers[5]
result = numbers[0:3]
result = numbers[::-1]   # listeyi sondan başa doğru çevirir.

numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numbers2[0]
result = numbers2[0,2] # 0. indeksteki grubun 2. indexteki elemanını verir.
result = numbers2[:,2]  # tüm grupların 2. indeksteki elemanlarını verir.
result = numbers2[:,0:2]  # tüm grupların 0 ve 1. indeksteki elemanlarını verir.
result = numbers2[-1,:]  # son satırdaki tüm değerleri verir.
result = numbers2[:2,:2]  # matirisn içindeki 2x2 lik matris elemanlarını verir.

print(result)

arr1 = np.arange(0,10)
# arr2 = arr1    # referans

arr2 = arr1.copy()  # referans listenin kopyasını oluşturur.
arr2[0] = 20   # yapılan güncelleme iki elemanda da yapılır.


print(arr2)
print(arr1)