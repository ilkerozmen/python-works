import pandas as pd

# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])
# data = dict(apples = s1, oranges = s2)
# df = pd.DataFrame(data)

data = [["Ahmet",50],["Ali",60],["Yağmur",70],["Çınar",80]]
dict = {"Name":["Ahmet","Ali","Yağmur","Çınar"],"Grade":[50,60,70,80]}
dict_list = [
    {"Name":"Ahmet","Grade":50},
    {"Name":"Ali","Grade":60},
    {"Name":"Yağmur","Grade":70},
    {"Name":"Çınar","Grade":80},
]

# df = pd.DataFrame(data, columns=['Name','Grade'], index=[1,2,3,4], dtype=float)
# df = pd.DataFrame(dict, index=["212","232","236","242"])
df = pd.DataFrame(dict_list, index=["212","232","236","242"])

print(df)