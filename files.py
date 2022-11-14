"""
file = open("newfile.txt","w")
file.close()
"""

"""
file = open("C:/Users/ilker.ozmen/Desktop/newfile.txt","w")
print(file)
"""

# "w" : (write) yazma metodu
# dosyayı konumda oluşturur ve eğer içerisinde bilgi varsa siler yeniden ekleme yapar.

"""
file = open("C:/Users/ilker.ozmen/Desktop/newfile.txt","w",encoding='utf-8')
file.write("İlker ÖZMEN")
file.close()
"""

"""     # dosyanın içerisine metin ekleme
file = open("C:/Users/ilker.ozmen/Desktop/newfile.txt","a",encoding='utf-8')
file.write("\nBursa")
file.close()
"""

"""       # yeni bir dosyayı içerisine metin eklemeden oluşturma
file = open("C:/Users/ilker.ozmen/Desktop/file.txt","x",encoding='utf-8')
file.close()
"""