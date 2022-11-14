from datetime import datetime
from datetime import timedelta

# result = dir(datetime.datetime)

simdi = datetime.now()
result = simdi.year
result = simdi.month
result = simdi.day
result = simdi.hour
result = simdi.minute
result = simdi.second
result = datetime.ctime(simdi)
result = datetime.strftime(simdi,'%Y')  # Yıl bilgisini verir.   # string olarak.
result = datetime.strftime(simdi,'%X')  # Saat bilgisini verir.
result = datetime.strftime(simdi,'%d')  # Gün bilgisini verir.
result = datetime.strftime(simdi,'%A')  # Gün bilgisini verir. salı vs.
result = datetime.strftime(simdi,'%B')  # Ay bilgisini verir. ekim vs.

# print(result)

t = '15 April 2019 hour 10:12:30'
dt = datetime.strptime(t,'%d %B %Y hour %H:%M:%S')

print(dt)

birthday = datetime(1995,10,25,12,30,10)

# print(birthday)

x = datetime.timestamp(birthday) # saniye bilgisi
x = datetime.fromtimestamp(x) # saniye to datetime bilgisi
# print(x)

x = simdi - birthday  # timedelta 
# print(x)

# x = simdi + timedelta(days=10)   # 10 gün ileri tarihi bulmak için
x = simdi + timedelta(days=730, minutes=10) 

# print(x)