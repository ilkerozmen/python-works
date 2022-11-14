"""   # for döngüsü kullanmadan liste elemanlarını ekrana yazdırma
liste = [1,2,3,4,5]

iterator = iter(liste)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
"""

"""  # while döngüsü ve iteratör kullanarak liste elemanlarını ekrana yazdırma
liste = [1,2,3,4,5]
iterator = iter(liste)

while True:
    try:
        element = next(iterator)
        print(element)
    except StopIteration:
        break
"""

class MyNumbers:
    def __init__(self,start,stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

list = MyNumbers(10,20)

# myiter = iter(list)          # While döngüsü ile ekrana yazma
# while True:
#     try:
#         element = next(myiter)
#         print(element)
#     except StopIteration:
#         break


# myiter = iter(list)    # print ile istenilen sayıda elemanı ekrana yazma
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# for x in list:      # for döngüsü ile ekrana yazma
#     print(x)