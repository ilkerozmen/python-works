import pandas as pd
import numpy as np

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(personeller)
result = df
result = df["Maaş"].sum()
result = df.groupby("Departman").groups
result = df.groupby(["Departman","Semt"]).groups

# for name, group in df.groupby("Semt"):   # Semte göre gruplama
#     print(name)
#     print(group)

# for name, group in df.groupby("Departman"):   # Departmana göre gruplama
#     print(name)
#     print(group)

result = df.groupby("Semt").get_group("Kadıköy")    # Sadece 1 gruba ait verileri çağırma
result = df.groupby("Departman").get_group("Muhasebe")    # Sadece 1 gruba ait varileri çağırma
result = df.groupby("Departman").sum()   # Departmanlardaki kişilere ait verilerin toplamları
result = df.groupby("Departman").mean()   # Departmanlardaki kişilere ait verilerin ortalamaları
result = df.groupby("Departman")["Maaş"].mean()   # Departmanlardaki kişilere ait maaş verilerin ortalamaları
result = df.groupby("Semt")["Yaş"].mean()   # Semtlerdeki kişilere ait yaş verilerin ortalamaları
result = df.groupby("Semt")["Maaş"].mean()   # Semtlerdeki kişilerin maaş ortalamaları
result = df.groupby("Semt")["Çalışan"].count()   # Semtlerdeki çalışan kişi sayısı
result = df.groupby("Departman")["Yaş"].max()   # Departmanlardaki en yaşlı kişilerin yaşı
result = df.groupby("Departman")["Maaş"].max()   # Departmanlardaki en yüksek maaşlı kişilerin maaşı
result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]   # Departmandaki en yüksek maaşlı kişinin maaşını verir.
result = df.groupby("Departman").agg(np.mean)  # Her departmandaki maaş ve yaş ortalamasını numpy ile hesaplar
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min])  # Her departmandaki maaşların toplamını, ortalamasını, en yüksek ve en düşük değerlerini numpy ile hesaplar
result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]  # Muhasebe departmanındaki maaşların toplamını, ortalamasını, en yüksek ve en düşük değerlerini numpy ile hesaplar

print(result)