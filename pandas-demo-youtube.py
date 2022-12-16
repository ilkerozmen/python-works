import pandas as pd      #BTK uygulama 20.14 Youtube uygulaması
import numpy as np

data = pd.read_csv('youtube-ing.csv')

df = pd.DataFrame(data)

result = df
# result = df.head(10)   # 1
# result = df.columns
# result = df[5:].head()   # 2
# result = len(df.columns)  # 3
# result = df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description"],axis=1)  # 4
# result = df["likes"].mean()   # 5
# result = df["dislikes"].mean()    # 5
# result = df.head(50)[["likes","dislikes"]]   # 6
# result = df[df["views"]==df["views"].max()][["title","views"]]   # 7
# result = df[df["views"]==df["views"].min()][["title","views"]]    # 8
# result = df.sort_values("views",ascending=False).head(10)[["title","views"]]  # 9
# result = df.groupby("category_id")["likes"].agg([np.mean])   # 10
# result = df.groupby("category_id")["comment_count"].agg([np.mean]).sort_values("mean", ascending=False)   # 11
# result = df.groupby("category_id")["title"].count()  # 12

df["title-len"] = df["title"].apply(len)  # 13
df["tags-len"] = df["tags"].apply(lambda x: len(x.split('|')))   # 14

print(result)

def likedislikeoranhesapla(dataset):     # 15
    likesList = list(dataset["likes"])
    dislikesList = list(dataset["dislikes"])

    liste = list(zip(likesList,dislikesList))      # her videonun like ve dislike verisi eşleştirilerek liste haline getirirlir.
    oranlistesi = []
    for like,dislike in liste:
        if (like + dislike) == 0:
            oranlistesi.append(0)
        else:
            oranlistesi.append(100*(like/(like+dislike)))
    return oranlistesi

df["beğeni_orani"] = likedislikeoranhesapla(df)
print(df.sort_values("beğeni_orani",ascending=False)[["title","likes","dislikes","beğeni_orani"]])
