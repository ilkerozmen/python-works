import pandas as pd    # BTK 20.7 uygulama

df = pd.read_csv("imdb.csv")

result = df
result = df.info()    # 1
result = df.columns   #  tüm kolonları gösterir.
result = df.head()   # 2
result = df.head(10)   # 3
result = df.tail()    # 4
result = df.tail(10)   # 5
result = df["movie_title"]   # 6
result = df["movie_title"].head()   # 7
result = df[["movie_title","imdb_score"]].head()  # 8
result = df[["movie_title","imdb_score"]].tail(7)  # 9
result = df[5:][["movie_title","imdb_score"]].head()  # 10
# result = df[df["imdb_score"]>=8.0][["movie_title","imdb_score"]].head(50)   # 11
# result = df[(df["title_year"]>=2014) & (df["title_year"]<=2015)][["movie_title","title_year"]]  # 12
# result = df[(df["num_voted_users"] >= 100000) | ((df["imdb_score"] >=8) & (df["imdb_score"] <=9))][["movie_title","num_voted_users","imdb_score"]]    # 13

print(result)