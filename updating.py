"""
with open("newfile.txt","r+",encoding="utf-8") as file:   # r+ hem okuma hem yazma metodunun kullanılması içindir.
    print(file.read())

with open("newfile.txt","r+",encoding="utf-8") as file:
    file.seek(20)
    print(file.write("deneme"))

with open("newfile.txt","r+",encoding="utf-8") as file:   # r+ hem okuma hem yazma metodunun kullanılması içindir.
    print(file.read())
"""
######### sayfa sonunda güncelleme ##########
"""
with open("newfile.txt","a",encoding="utf-8") as file:   #  a (append) metodu dosyonun sonuna cursor u konumlandırır ve ekleme yapar.
    print(file.write("\nİlker ÖZMEN"))

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
"""
########## sayfa başında güncelleme #########
"""
with open("newfile.txt","r+",encoding="utf-8") as file:
    content = file.read()
    content = "Halil ÖZMEN\n" + content
    file.seek(0)
    file.write(content)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
"""
########## sayfa ortasında güncelleme #########

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     list = file.readlines()
#     content = list.insert(1,"Zübeyde ÖZMEN\n")      # string ifade olarak ekleme yöntemi
#     file.seek(0)
#     for i in list:
#         file.write(i)
"""
with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    list.insert(2,"Saliha ÖZMEN\n")
    file.seek(0)
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())
"""