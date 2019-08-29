# this class is a menu where the app should be started
from data_storage import FlixStorage
from shows_movies import Flix
from getData import Api
import logging
from flask import Flask, render_template, url_for, flash, redirect, request
import sqlite3
from flask import g

app = Flask(__name__)


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
        if request.form['clicked'] == 'add':
            result = add_list(moviename, showname)
            return render_template('list.html').format(result=result)

        if request.form['clicked'] == 'show it':
            theList = get_movies()
            return '''
                       <html>
                        <body>
                            <p>The result is </p>
                            <p>the list of movies {theList}</p>
                            <p><a href="/">Click here to try again</a>
                        </body>
                       </html>
                  '''.format(theList=theList)

    return render_template('home.html')


def add_list(moviename, showname):
    FlixStorage.add_movies(moviename)
    FlixStorage.add_shows(showname)
    return moviename, showname


def get_movies():
    return FlixStorage.get_movies()


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
    app.run(debug=True)