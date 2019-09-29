# this class is a menu where the app should be started
from data_storage import FlixStorage
from shows_movies import Flix
from getData import Api
import logging
from flask import Flask, render_template, url_for, flash, redirect, request
import sqlite3

DATABASE = 'databaseFile.db'
# /home/techturtl3/databaseFile.db

app = Flask(__name__)


@app.route("/")
def hello():
    return "hello there!"


@app.route("/requests", methods=["GET", "POST"])
def request_data():
    return render_template('requests.html')


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
            try:
                all_movies = get_movies()
                all_shows = get_shows()
                random_movie = get_random_movie()
                random_show = get_random_show()
                return render_template('list.html').format(all_movies=all_movies, all_shows=all_shows, random_movie=random_movie, random_show=random_show)
            except:
                return render_template('exception.html')

    return render_template('home.html')


@app.route("/home.html", methods=["GET", "POST"])
def library():
    if request.method == "POST":
        if request.form['clicked'] == 'Empty shows':
            eshows = clear_shws()
            return render_template('home.html')

        if request.form['clicked'] == 'Empty movies':
            emovies = clear_mvs()
            return render_template('home.html')

        if request.form['clicked'] == 'Empty all':
            eall = clear_both()
            return render_template('home.html')


@app.route("/requests.html",  methods=["GET", "POST"])
def request_info():
    if request.method == "POST":
        flix = request.form["motion_picture"]
        motion_picture = get_data(flix)
        if request.form['clicked'] == 'search':
            return render_template('fetch.html').format(motion_picture=motion_picture)
    return render_template('requests.html')


def add_list(moviename, showname):
    FlixStorage.add_movies(moviename)
    FlixStorage.add_shows(showname)
    return moviename, showname


def get_movies():
    return FlixStorage.fetch_movies()


def get_shows():
    return FlixStorage.fetch_shows()


def clear_mvs():
    return FlixStorage.clear_movies()


def clear_shws():
    return FlixStorage.clear_shows()


def clear_both():
    return FlixStorage.clear_all()


def get_data(flix):
    return Api.retrieve(flix)


def get_random_movie():
    return FlixStorage.random_movie()


def get_random_show():
    return FlixStorage.random_show()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)