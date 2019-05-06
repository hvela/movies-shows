#this class is a menu where the app should be started
from data_storage import FlixStorage
from shows_movies import Flix

class Menu(FlixStorage):
    def __init__(self, choice=None):
        self.choice = choice
        FlixStorage.__init__(self)

    def start_program():
        choice = int(input("Enter one of the following to continue\n\n"
                       "1 - to add a movie\n"
                       "2 - to add a show\n"
                       "3 - to quit\n\n"
                       "input: "))

        if choice is 1:
              FlixStorage.add_movies(self=None)
        if choice is 2:
              FlixStorage.add_shows(self=None)
        else:
              print("hello world")
    start_program()
    # if __name__=="main":
    #     start_program(self)

#   issue of getting program to recall it self from other class