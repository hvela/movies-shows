# this class is a menu where the app should be started
from data_storage import FlixStorage
from shows_movies import Flix
from getData import api

class Menu(FlixStorage):
    def __init__(self, choice=None):
        self.choice = choice
        FlixStorage.__init__(self)

    def start_program():
        while True:

           choice = input("\nEnter one of the following to continue\n\n"
                               "1 - to add a movie\n"
                               "2 - to add a show\n"
                               "3 - to get information about any movie\n"
                               "4 - to quit\n\n"
                               "input: ")
           try:
               chosen = int(choice)
           except ValueError:
               print("errrorr")

           if chosen is 1:
               FlixStorage.add_movies(self=None)
           elif chosen is 2:
               FlixStorage.add_shows(self=None)
           elif chosen is 3:
               api.retrieve(self=None)
           elif chosen is 4:
               print("thanks for using")
               break
           else:
               print("You eneter and invalid value")

    start_program()
