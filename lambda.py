'''
def square(num):                        # map metodu ile listedeki sayıların karelerini alıp ekrana yazdırır.
    return num**2
numbers = [1,3,5,9]
result = list(map(square, numbers))
# for item in map(square, numbers):       # Aynı işi for döngüsü ile yapmaktadır. 
#     print(item)
print(result)
'''

'''
square = lambda num: num ** 2         # numbers listesindeki her bir elemanı num değşkenine atıp square işlemini yapar, ardından map metodu ile liste olarak sonucu ekrana yazdırır.
numbers = [1,3,5,9]
result = list(map(square, numbers))
print(result)
'''

'''
numbers = [1,3,5,9,10,4]                    # Yukarıdaki gibi numbers listesindeki elemanları lambda metodu ile işlem oluşturarak listedeki çift sayıları ekrana yazdırır.
check_even = lambda num: num%2==0
result = list(filter(check_even, numbers))
print(result)
'''
