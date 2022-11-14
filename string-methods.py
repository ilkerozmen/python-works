message = 'Hello There. My name is İlker ÖZMEN'
# message = message.lower()   # tüm harfler küçük
# message = message.upper()   # tüm harfler büyük
# message = message.title()    # kelimelerin ilk harfleri büyük
# message = message.capitalize()    # cümlenin ilk harfi büyük
# message = message.strip()    # cümlenin başında ve sonunda boşluk karakteri varsa siler / lstrip solunda / rstirp sağında
# message = message.split()    # cümlede bulunan kelimeleri ayrı ayrı tırnak içerisinde yazar
# message = ' '.join(message)  # diziye çevrilen ifadeyi eski haline getirilir. tırnak içine boşiluk yerine istenilen ifade eklenebilir.
# message = message.find('İlker')   # cümledeki İlker kelimesini bulur ve kelimenin ilk harfinin indexini ekrana yazdırır.
# message = message.startswith('H')   # cümlenin ilk karakterinin H olup olmadığını bool olarak ifade eder True/False
# message = message.endswith('N')   # cümlenin son karakterinin H olup olmadığını bool olarak ifade eder True/False
# message = message.replace('İlker', 'Mustafa')  # cümledeki İlker bilgisini bulur ve Mustafa ile değiştirir.
# message = message.center(50,'*')   # verilen cümleyi 50 karakter içinde ortalı bir şekilde yazdırır ve boşluk yerine * ifadesi ekler. / .rjust / .ljust
# message = message.count('a')     # verilen cümledeki a karakter sayısını verir.
# message = message.isalpha()     # verilen cümledeki karakterlerin alfabetik olup olmadığını sorgular.
# message = message.isdigit()     # verilen cümledeki karakterlerin nümerik olup olmadığını sorgular.
print(message)