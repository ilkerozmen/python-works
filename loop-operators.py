'''
for item in range(10,100,10):              # range metodu 10 ile 100 arasında olan sayıları 10 ar atlayarak liste olarak yazdırır.
    print(item)
print(list(range(10,100,10)))
'''

'''
greeting = 'Hello There'                        # enumerate metodu verilen string ifadenin elemanlarına otomatik olarak index numarası atar ve yazdırır.
for index,letter in enumerate(greeting):
    print(f"index: {index}, letter: {letter}")
'''

'''
list1 = [1,2,3,4,5]                       # zip metodu index numaralarına göre listelri eşleştirir.
list2 = ['a','b','c','d','e']
list3 = [100,200,300,400,500]

# print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):          # burda oluşturulan liste elemanları tuple listesi olarak yazdırılır.
    print(item)

for a,b,c in zip(list1,list2,list3):         # burada oluşturuluan liste elemanları int değer olarak yazdırılır.
    print(a,b,c)
'''