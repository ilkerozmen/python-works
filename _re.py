import re
# result = dir(re)

# re module

str = "Python Kursu: Python Programlama Rehberiniz | 40 Saat"

# result = re.findall("Python",str)      # karakter dizisinin içinde belirtilen ifadeyi arar.
# result=len(result)

# result = re.split(" ",str)      # ifade de boşluk işareti olan yerleri böler ve liste elemanları oluşturur.

# result = re.sub(" ","-",str)       # boşluk karakterleri yerine - karakteri koyar.

result = re.search("Python",str)       # belirtilen ifadeyi hangi karakter arasında bulduğunu match objesi olarak söyler.
# result = result.span()           # bulunan karakter aralığını verir.
# reslut = result.start()   # ilk karakterin sırasını (index numarası) verir.
# result = result.end()     # son karakterin sırasını  verir.
# result = result.group()    # bulunan karakter dizinini verir.

print(result)


# tüm regular expression modüllerinin kullanımı için : https://www.w3schools.com/python/python_regex.asp  bak !