'''
name = 'İlker Özmen'
for x in name:
    if x =='e':
        break                        # break komutu döngüyü verilen eleman döngü içine girene kadar çalıştırır.
    print(x)
'''

'''
name = 'İlker Özmen'
for x in name:
    if x =='e':
        continue                        # contiune komutu döngüyü verilen elemanı es geçerek çalıştırır.
    print(x)
'''

'''
x=0                           
while x<5:
    x +=1
    if x==2:
        continue                        # 2 değerini yazdırmadan döngüyü tamamlar.
    print(x)
'''  

'''
a = 0                                  # 0 ile 100 arasındaki tek sayıların toplamını verir.
x = 0
while x<=100:
    x += 1
    if x%2 == 1:
        a +=x    
print (a)
'''

'''
a = 0                                  # 0 ile 100 arasındaki tek sayıların toplamını verir.
x = 0
while x<=100:
    x += 1
    if x%2 == 1:
        a +=x    
print (a)
'''