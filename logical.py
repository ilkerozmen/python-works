
x = input("İlk sayıyı giriniz: ")
y = input("İkinci sayıyı giriniz: ")          # Girilen 2 sayıdan hangisinin büyük olduğunu gösterir ve nümerik değer girmenizi ister.
a = x.isnumeric()
b = y.isnumeric()
if a and b == True:
    if x>y:
        print("İlk sayı büyüktür.")
    elif x<y:
        print("İlk sayı küçüktür.")
    else:
        print("İki sayı birbirine eşittir.")
else:
    print("Nümerik değer giriniz !")
