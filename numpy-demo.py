import numpy as np    # video 19.5 uygulaması

result = np.array([10,15,30,45,60])  # 1

result = np.arange(5,15)  # 2

result = np.arange(50,100,5)  # 3

result = np.zeros(10)  # 4

result = np.ones(10)  # 5

result = np.linspace(0,100,5)   # 6

result = np.random.randint(10,30,5)   # 7

result = np.random.randn(10)  # 8

result = np.random.randint(10,50,15).reshape(3,5)  # 9

matris = np.random.randint(-50,50,15).reshape(3,5)
# rowTotal = matris.sum(axis=1)   # 10
# colTotal = matris.sum(axis=0)
# print(rowTotal," ", colTotal)

# result = matris.max()    # 11
# result = matris.min()
# result = matris.mean()

# result = matris.argmax()   # 12
# result = matris.argmin()

arr = np.arange(10,20)      # 13
result = arr[0:3]

result = arr[::-1]    # 14

result = matris[0]    # 15

result = matris[1,3]    # 16

result = matris[:,0]   # 17

result = matris ** 2    # 18

ciftler = matris[matris % 2 == 0]       # 19
result = ciftler[ciftler>0]

print(result)