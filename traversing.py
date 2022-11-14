with open ("newfile.txt","r", encoding = "utf-8") as line:
    content = line.readline()
    line.seek(0)   # seek metodu okuma yaparken cursor u en başa atar
    liste = content.strip()  # strip metodu değişkenin başındaki ve sonundaki boşlukları siler
    print(line.tell())  # tell metodu cursor un konumunu verir, içine değer atarsak o index e kadar olan değerleri okur.
    print(liste)
    line.seek(0)