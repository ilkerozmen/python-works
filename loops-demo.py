import random                                    # sayı tahmin oyunu
sayi = random.randint(0,10)
can = int(input("Kaç denemede bilmek istersiniz?: "))
hak = can
sayac = 0
while hak>0:
    hak-=1
    sayac +=1
    tahmin = int(input("0 ile 10 arasında seçilen sayıyı tahmin ediniz: "))
    if sayi == tahmin:
        print(f"Tebrikler {sayac}. denemede bildiniz. Tutulan sayı: {sayi}, Toplam puanınız: {100-((100/can)*(sayac-1))}")
        break
    elif sayi > tahmin:
        print("yukarı")
    else:
        print("aşağı")
    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {sayi}")
