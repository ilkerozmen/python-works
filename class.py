# class                  >>>>>>       yapısı oluşturumu ve kullanımı
class Person:
    # class attributes
    address = 'no information'
    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print('init  metodu çalıştı')
        # methods
# object (instance) 
p1 = Person(name = 'Ilker', year = 1995)
p2 = Person(name = 'Musemma', year = 1997)
# updating
p1.name = 'Halil'
p1.address = 'Bursa'
# accessing object attributes
print(f"name: {p1.name} year: {p1.year} address: {p1.address}")  
print(f"name: {p2.name} year: {p2.year} address: {p2.address}")  