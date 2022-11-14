import os
import datetime

result = dir(os)
result = os.name

# os.chdir('C:\\') # bu dizine gider.
# os.chdir('..') # bir üst dizine gider.
# os.chdir('../..') # iki üst dizine gider.

result = os.getcwd()  # etkin dizin öğrenme
# os.mkdir("newdirectory") # bulunduğumuz dizinde yeni bir klasör oluşturur. # C dizinine
# os.rename("newdirectory","yeniklasör")   # istenilen dosyanın adını değiştirir.
# os.rmdir("newdirectory")  # alt dizini yoksa dosyayı siler.
# os.removedirs("newdirectory/yeniklasör")  # alt dizini varsa dizinler ile birlikte dosyayı siler.

# os.makedirs("newdirectory/yeniklasör")  # iç içe klasör oluşturabilir.

# for dosya in os.listdir():
#     if dosya.endswith('.py'):
#         print(dosya)

# print(result)

# result = os.stat("date.py") # belirtien dosya hakkında bilgileri gösterir.
# result = result.st_size/1024 # dosyanın boyutunu verir.
# result = datetime.datetime.fromtimestamp(result.st_ctime) # dosyanın oluşturulma zamanını verir.
# result = datetime.datetime.fromtimestamp(result.st_atime) # dosyanın son erişilme zamanını verir.
# result = datetime.datetime.fromtimestamp(result.st_mtime) # dosyanın değiştirilme zamanını verir.

# os.system("notepad.exe")  # notepad uygulamasını açar.

result = os.path.abspath("_os.py")
result = os.path.dirname("D:/ILKER OZMEN/python/python_temelleri/_os.py")
result = os.path.dirname(os.path.abspath("_os.py"))
result = os.path.exists("D:/ILKER OZMEN/python/python_temelleri/_os.py")  # belirtilen dosya var mı yok mu sonucunu verir.
result = os.path.isdir("D:/ILKER OZMEN/python/python_temelleri/_os.py")  # belirtilen dizin klasör mü değil mi sonucunu verir.
result = os.path.isfile("D:/ILKER OZMEN/python/python_temelleri/_os.py")  # belirtilen dizin dosya mı değil mi sonucunu verir.
result = os.path.join("C:\\","deneme","deneme1")
result = os.path.split("C:\\deneme")
result = os.path.splitext("_os.py")
a = result[0]
b = result[1]

# print(result)
# print(a)
# print(b)