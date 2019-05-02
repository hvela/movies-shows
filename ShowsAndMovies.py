class Flix:
    #constructor method that has variables
    def __init__(self, showname=None, moviename=None):
        self.showname = showname
        self.moviename = moviename

    def start_program(self):
        print('{}\nThis program will allow you to enter shows and movies and store'
              ' them in a database.\nThen it will print out 1 show and movie randomly'
              ' that you have stored.\n'.format('d*_*b'
                                             '\n  |'
                                              '\n - -\n\n'))

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

    # print(add_show(None))

    # def add_flix(*args, **kwargs):
    #     xList = []
    #     yList = []
    #     x = 0
    #     choice = 'yes'
    #     print('This program will allow you to enter shows and movies \n and then it will pick one of each randomly :)\n\n')
    #
    #     while choice == 'yes':
    #          if choice == 'no':
    #              break
    #          showname = input('What is the name of the show: ')
    #          #showtime = input('What is the length of the show')
    #
    #          moviename = input('What is the name of the movie: ')
    #          #movietime = input('What is the length of the movie: ')
    #
    #
    #          # xList.append(showname,showtime)
    #          # yList.append(moviename, movietime)
    #          choice = input('Enter yes if you would like to continue entering movies and shows or no to quit: ')
    #
    #     # aShow = Shows(showname)
    #     # aMovie = Movies(moviename)
    #     values = Flix(showname, moviename)
    #     print('\n\n---------------------------------------------------------------')

import random
import json

# class Shows:
#     def __init__(self, showname=None):
#         self.showname = showname
#
#
# class Movies(Shows):
#     def __init__(self, moviename=None):
#         self.moviename = moviename
#
#
# class Implementation(Movies):
#     xList = []
#     yList = []
#     x = 0
#     choice = 'yes'
#     print('This program will allow you to enter shows and movies \n and then it will pick one of each randomly :)\n\n')
#
#     while choice == 'yes':
#         if choice == 'no':
#             break
#         showname = input('What is the name of the show: ')
#         #showtime = input('What is the length of the show')
#
#         moviename = input('What is the name of the movie: ')
#         #movietime = input('What is the length of the movie: ')
#
#
#         # xList.append(showname,showtime)
#         # yList.append(moviename, movietime)
#         choice = input('Enter yes if you would like to continue entering movies and shows or no to quit: ')
#
#     aShow = Shows(showname)
#     aMovie = Movies(moviename)
#
#     print('\n\n---------------------------------------------------------------')







