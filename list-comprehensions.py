'''
numbers = [x for x in range(10)]         # 0 dan 10 a kadar olan sayıları dizi olarak ekrana yazdırır.
print(numbers)
'''

'''
numbers = [x*x for x in range(10) if x%3==0]     # 0 ile 10 arasındaki sayılardan 3 e bölünebilen sayıların karesini alır.
print(numbers)
'''

'''
mystirng = 'Hello'
mylist = []
for letter in mystirng:
    mylist.append(letter)
print(mylist)
'''

'''
mylist = [letter for letter in mystirng]          # üstteki kod satırı ile aynı işi yapar.
print(mylist)
'''

'''
years = [1983, 1999, 2008, 1956, 1986]           # verilen doğum yıllarına göre yaş hesabını liste olarak ekrana yazdırır.
ages = [2021-year for year in years]
print(f"doğum yılı: {years}, yaş: {ages}")
'''

'''
results = [x if x%2==0 else 'TEK' for x in range(1,10)]       # 0 ile 10 arasındaki tek sayıları 'tek' olarak, çift sayıların ise sayı değerlerini yazdırır.
print(results)
'''

'''                                                          # iç içe for döngüsünü daha basit bir yolla yazarak 0 ile 3 arasındaki sayılar ile matris oluşturur.
result = []
for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

# numbers = [(x,y) for x in range(3) for y in range(3)]
# print(numbers)
'''

'''
a = int(input("Kare matris oluşturmak için bir sayı giriniz: "))       # kullanıcıdan alınan sayı değerine göre kare matris oluşturur.
x,y = 0,0

matris = [(x,y) for x in range(1,a+1) for y in range(1,a+1)]
print(matris) 
'''