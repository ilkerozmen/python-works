# value types => string, number            #  değişkenlerde yapılan değişiklik birbirini etkilemez
x = 5
y = 25
x=y

y = 10

# print(x,y)

# reference types  => list               # değişkenlerde yapılan değişkilik birbirini etkiler

a = ["apple", "banana"]
b = ["apple", "banana"]

a = b
b[0] = "grape"
print(a,b)

