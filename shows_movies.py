

class Flix:
    #constructor method that has variables
    def __init__(self, showname=None, moviename=None):
        self.showname = showname
        self.moviename = moviename

    def start_program(self):
        print('\nThis program will allow you to enter shows and movies and store '
              'them in a database.\nThen it will print out 1 show and 1 movie randomly\n')

    def add_show(self):
        try:
            showname = input('What is the name of the show: ')
            if not showname:
                raise ValueError
        except ValueError:
            print('You did not enter a show name')

        return showname

    def add_movie(self):
        try:
            moviename = input('What is the name of the movie: ')
            if not moviename:
                raise ValueError
        except ValueError:
            print("You did not enter a movie name")
        return moviename







