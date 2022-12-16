from matplotlib import pyplot as plt
import numpy as np
"""
x =[1,2,3,4]
y= [1,4,9,16]

# plt.plot(x,y,color="red",linewidth=5)   # x değerlerinin y ekseninde karşılık gelen değerlerini kırmızı renkte ve çizgi kalınlığı 5 birim olarak çizer.
# plt.plot(x,y,"--g")  # matplotlib in internet sitesinden farklı stiller seçilebilir.
plt.plot(x,y,"o--r") # farklı stillerde çizgi grafiği gösterimi.
plt.axis([0,6,0,20])   # x ve y ekseninin min ve maks değerleri.
plt.title("Grafik Başlığı")
plt.xlabel("x ekseni")
plt.ylabel("y ekseni")
"""

"""
x = np.linspace(0,2,100)

plt.plot(x,x,label="linear",color="red")
plt.plot(x,x**2,label="quadratic",color="yellow")
plt.plot(x,x**3,label="cubic",color="green")

plt.xlabel("x label")
plt.xlabel("y label")
plt.title("Simple Plot")

plt.legend()

plt.show()
"""

"""
x = np.linspace(0,2,100)      # tek plot da 3 grafik gösterme.
fig,axs = plt.subplots(3)


axs[0].plot(x,x,color="red")
axs[0].set_title("linear")

axs[1].plot(x,x**2,color="green")
axs[1].set_title("quadratic")

axs[2].plot(x,x**3,color="blue")
axs[2].set_title("cubic")

"""

"""
x = np.linspace(0,2,100)   # grafikleri 2 x 2 formatında gösterme
fig,axs = plt.subplots(2,2)
fig.suptitle("Grafik Başlığı")

axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="green")
axs[1,0].plot(x,x**3,color="yellow")
axs[1,1].plot(x,x**4,color="blue")

"""

import pandas as pd

df = pd.read_csv("NBA-1.csv")
df.dropna()
# df = df.drop(["age","player_name","college","country","draft_year","draft_round","draft_number","season"],axis=1).groupby("team_abbreviation").mean()
df = df[["player_weight","player_height","age","team_abbreviation"]].groupby("team_abbreviation").mean()

df.head().plot(subplots=True)   # ilk 5 veriyi gösterir.
plt.legend()

plt.tight_layout()  # başlıklar birbirine girmesin diye layout değiştirildi.
plt.show()



