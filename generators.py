"""   # hafızada değer tutmadan yield komutu ile uzun sürecek işlemleri kısa sürede hesaplar.
def cube():
    for i in range(5):
       yield i**3

for i in cube():
    print(i)
"""

generator = (i**3 for i in range(5))
for i in generator:
    print(i)