'''
name = 'Çınar'                # fonksiyon içindeki print ifadesi local olarak çalışır ve kendi içerisindeki işlemi yapar
def changeName(new_name):
    # local name
    name = new_name
    print(name)
changeName('İlker')
print(name)                  # fonksiyon dışındaki print ise global olarak yani fonksiyondan bağımsız çalışır ve değişkenin orjinal değerini yazdırır.
'''

'''
name = 'global string'           # iç içe fonksiyonlarda kullanımı
def greeting():
    name = 'İlker'
    def hello():
        print('Hello ' + name)
    hello()
greeting()
'''

'''
x = 50                            # global metodu fonksiyonda x üzerinde yapılan işlemleri fonksiyon dışındaki x üzerinde de yapılmasını sağlar.
def test():
    global x                      # local x ve global x eşitleniyor.
    print('x:',x)                 # global x
    x = 100
    print('Changed x to:',x)      # local x
test()
print(f"Global x: {x}")           # local x = global x işlemi yapıldığı için local x değeri global olarak ekrana yazdırılıyor.
'''