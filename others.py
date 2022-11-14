'''
x = [1,2,3]                  # x listesi ve listesinin elemanlarında değişiklik yapılıp elemanlar birbirine eş belirlense bile 
y = [2,4]                    # in komutu ile de listedeki veya değişkendeki bir elemanın olup olmadığını sorgulayabiliyoruz.

del x[2]
y[1] = 1
y.reverse()
print(x,y)
print(x==y)                  # elemanların eşitliği sorgulandığında true değeri gelir.
print(x is y)                # fakat tanımlama adresleri farklı oldukları için is komutu sorgusunda false değeri gelir. / is not operatörü de kullanılabilir.
'''

