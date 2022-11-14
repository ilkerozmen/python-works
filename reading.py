"""
try:
    file = open ("newfile.txt","r")
    print(file)
except FileNotFoundError:
    print("Dosya okuma hatası")
finally
    file.close()
    print("Dosya kapandı")
"""
file = open ("newfile.txt","r", encoding = "utf-8")

# for döngüsü
#for i in file:
#    print(i, end="")

#read() fonksiyonu

# content = file.read()
# content = file.readline()

content1 = (file.readline())
#print(content1)


content = (file.readlines())
liste = (content[6])
#print(liste)

#file.close()