"""   # oluşturulan fonksiyona iç fonksiyonu değişken olarak atama 
def my_decorator(func):
    def wrapper(name):
        print("fonksiyondan önce işlemler")
        func(name)
        print("Fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator    # ana fonksiyona atıf
def sayHello(name):
    print("hello",name)

sayHello("ali")
"""

""" # üs alma, faktörüyel, toplama gibi istenilen fonksiyonlar eklenerek bu işlemlerin hesaplanma sürelerini gösterir.
import math, time
from tracemalloc import start

def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon "+func.__name__+" "+ str((finish-start)-1)+ " sn sürdü.")
    return inner

@calculate_time
def usalma(a,b):
    print("sonuç: ", math.pow(a,b))
   
@calculate_time
def faktoriyel(num):
    print("sonuç: ", math.factorial(num))

@calculate_time
def toplama(a,b):
    print(a+b)

usalma(2,3)
faktoriyel(5)
toplama(10,20)
"""