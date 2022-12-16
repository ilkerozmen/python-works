mylist = [1,2,3]

class Movie():
    def __init__(self,title,director,duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie objesi oluşturuldu.')
    def __str__(self):
        return f"{self.title} by {self.director} time {self.duration}"
    def __len__(self):
        return self.duration
    def __del__(self):
        print('Film objesi silindi.')

m = Movie('film adı','yönetmen', 120)
# print(len(mylist))
# print(len(m))
print (str(m))