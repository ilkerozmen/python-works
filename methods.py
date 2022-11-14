'''
# class
class Person:
    # class attributes
    address = 'no information'
    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
    # instance methods
    def intro(self):
        print('Hello There. I am '+ self.name)
    # instance methods
    def calculateAge(self):
        return 2021 - self.year
# object (instance) 
p1 = Person(name = 'Ilker', year = 1995)
p2 = Person(name = 'Musemma', year = 1997)

p1.intro()
p2.intro()
print(f"Adım: {p1.name} Yaşım: {p1.calculateAge()} Adresim: {p1.address}")  
print(f"Adım: {p2.name} Yaşım: {p2.calculateAge()} Adresim: {p2.address}")  
'''

class Circle:
    # class object attributes
    pi = 3.14
    def __init__(self, yaricap=1):
        self.r = yaricap
    # methods
    def cevre_hesapla(self):
        return 2 * self.pi * self.r
    def alan_hesapla(self):
        return self.pi * (self.r**2)
c1 = Circle()   # yaricap = 1
c2 = Circle(5)

print(f"c1 : alan = {c1.alan_hesapla()} çevre: {c1.cevre_hesapla()}")
print(f"c2 : alan = {c2.alan_hesapla()} çevre: {c2.cevre_hesapla()}")