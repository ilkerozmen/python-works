import requests

class theMoviedb:
    def __init__(self):
        self.api_url = "https://api.themoviedb.org/3/"
        self.api_key = "c0494affd7049d49833b27d39fee95a8"
        self.options1 = "search/keyword"

    def getPopulars(self):
        response = requests.get(f"{self.api_url}/movie/popular?api_key={self.api_key}&language=en-US&page=1")
        return response.json()

    def getSearch(self,keyword):
        response = requests.get(f"{self.api_url}/{self.options1}?api_key={self.api_key}&query={keyword}&page=1")
        return response.json()

movieApi = theMoviedb()

while True:             # siteye populer filmlerin listesi için get response talebi yapar ,
    secim = input("1- Popular Movies\n2- Search Movies\n3- Exit\nSeçim: ")

    if secim == "3":
        break
    else:
        if secim == "1":        # popular apisinden sonuçların içinden filmlerin adını çekerek ekrana yazdırır.
            movies = movieApi.getPopulars()
            for movie in movies['results']:
                print(movie['title'])
        if secim == "2":      # search apisinden içinde 'wailking' geçen filmleri arar ve sonuçların içinden filmleri çekerek adını ekrana yazdırır.
            keyword = input("keywords: ")
            movies = movieApi.getSearch(keyword)
            for movie in movies['results']:
                print(movie['name'])