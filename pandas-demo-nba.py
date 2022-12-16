import pandas as pd      #BTK uygulama 20.13 NBA uygulaması
import numpy as np

data = pd.read_csv('NBA-1.csv')

df = pd.DataFrame(data)

result = df
result = df.head(10)  # 1
result = len(df.index)   # 2 
result = df["player_height"].mean()  # 3  --> Maaş kolonu olmadığı için boy kolonu kullanıldı.
result = df["player_height"].max()   # 4  --> Maaş kolonu olmadığı için boy kolonu kullanıldı.
result = df[df["player_height"]==df["player_height"].max()][["player_name","player_height"]]   # 5   --> Maaş kolonu olmadığı için boy kolonu kullanıldı.
result = df[(df["age"]>20) & (df["age"]<25)][["player_name","team_abbreviation","age"]].sort_values("age")  # 6
result = df[(df["player_name"]=='John Holland')][["player_name","team_abbreviation"]]   # 7
result = df.groupby("team_abbreviation")["player_height"].agg([np.mean])   # 8
result = df["team_abbreviation"].nunique()  # 9
result = df.groupby("team_abbreviation")["player_name"].nunique()    # 10
df.dropna(inplace=True)
result = df[df.player_name.str.contains('and')]   # 11

print(result)

