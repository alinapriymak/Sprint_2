# В этом задании тебе нужно создать иерархию разных видов фильмов: драму и комедию, 
# которые наследуются от суперкласса Movies

class Movies:
    def __init__(self, movie=None):
        self.movies = []
        if movie:
            self.movies.append(movie)

    
    def add_movie(self, movie):
        self.movies.append(movie)
        return self.movies


class Comedy(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f"Комедии: '{self.movies}'"



class Drama(Movies):
    def add_movie(self, movie):
        self.movies.append(movie)
        return f"Драмы: '{self.movies}'"
    

comedy = Comedy()
drama = Drama()

print(comedy.add_movie('Большой куш'))
print(drama.add_movie('Оружейный барон'))
