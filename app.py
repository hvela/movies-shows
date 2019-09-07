# this class is a menu where the app should be started
from data_storage import FlixStorage
from shows_movies import Flix
from getData import Api
import logging
from flask import Flask, render_template, url_for, flash, redirect, request

DATABASE = '/home/techturtl3/mysite/databaseFile.db'

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello there!"


@app.route("/index.html", methods=["GET", "POST"])
def home():
    errors = ""
    if request.method == "POST":
        moviename = None
        showname = None

        moviename = request.form["moviename"]
        showname = request.form["showname"]

        # validation
        # if moviename is not None and showname is not None:

        # if the user adds movies render the movies added
        if request.form['clicked'] == 'add':
            result = add_list(moviename, showname)
            return render_template('added.html').format(result=result)

        # if the user wants to see the movies in the pool show them
        if request.form['clicked'] == 'show library':
            all_movies = get_movies()
            all_shows = get_shows()

                       # <html>
                       #  <body>
                       #      <p>The result is </p>
                       #      <p>the list of movies {theList}</p>
                       #      <p><a href="index.html">Click here to try again</a>
                       #  </body>
                       # </html>
            return render_template('list.html').format(all_movies=all_movies, all_shows=all_shows)

    return render_template('home.html')
# test comment for commit 1
# test comment for commit 2
# test comment for commit 3


def add_list(moviename, showname):
    FlixStorage.add_movies(moviename)
    FlixStorage.add_shows(showname)
    return moviename, showname


def get_movies():
    return FlixStorage.fetch_movies()


def get_shows():
    return FlixStorage.fetch_shows()


# class Menu(FlixStorage):
#     def __init__(self, choice=None):
#         self.choice = choice
#         FlixStorage.__init__(self)
#
#     def start_program(self=None):
#         name = input("Enter your name: ")
#         while True:
#             choice = input("\n"+name+", enter one of the following to continue:\n\n"
#                            "1 - to add a movie\n"
#                            "2 - to add a show\n"
#                            "3 - to get information about any movie or show\n"
#                            "4 - to quit\n\n"
#                            "input: ")
#
#         # convert to int if it's an actual number
#             if choice.isdigit():
#                 choice = int(choice)
#                 if choice is 1:
#                     FlixStorage.add_movies(self=None)
#                 elif choice is 2:
#                     FlixStorage.add_shows(self=None)
#                 elif choice is 3:
#                     Api.retrieve(self=None)
#                 elif choice is 4:
#                     print("Thanks for using", name+"!")
#                     break
#                 else:
#                     print("You entered an invalid value, please try again.")
#             else:
#                 print('Something went wrong, try again!')
    # start_program()
    # logging.debug('App currently running!')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)