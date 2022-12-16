import pandas as pd

data = pd.read_csv("nba.csv")
data.dropna(inplace=True)     # NaN değer varsa , o satırı siler ve orjinal değişkene atar.
# data["Player"] = data["Player"].str.upper()
# data["Player"] = data["Player"].str.lower()
# data["index"] = data["Player"].str.find('a')   # Player kolonundak, karakterlerin içinde 'a' karakterini arar ve kaçıncı karakterde bulursa en sonda "index" adında kolon oluşturarak oraya yazar.
# data = data[data.Player.str.contains('Tony')]   # Adı Tony olan oyunculara ait veri satırlarını ekrana yazar.
# data = data.Player.str.replace(' ','-')   # Player kolonunda bulunan boşluk karakteri yerine '-' ekliyor.
# data[['FirstName','LastName']] = data['Player'].loc[data['Player'].str.split().str.len()==2].str.split(expand=True) # Player kolonundaki isimler first name ve last name adlı kolonlara ad ve soyad şeklinde parçalama yapar.

print(data.head(10))