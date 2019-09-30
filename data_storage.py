import sqlite3
from shows_movies import Flix
import random


# /home/techturtl3/databaseFile.db
class FlixStorage:
    # method here for adding movies to the database
    @staticmethod
    def add_movies(movie):
        # step 1 connect the database
        conn = sqlite3.connect('/home/techturtl3/databaseFile.db')

        # step 2 create the cursor
        c = conn.cursor()

        # step 3 create the table
        c.execute('CREATE TABLE IF NOT EXISTS myMovies (movie_name TEXT)')

        # prompt start of program
        # Flix.start_program(None)

        # # insert data to the shows table here
        # c.execute('INSERT INTO shows VALUES (?)', (Flix.add_show(None),))

        # Insert data into the movies table
        c.execute('INSERT INTO myMovies(movie_name) VALUES(?)', (movie,))

        conn.commit()
        conn.close()

    @staticmethod
    def fetch_movies():
        # step 1 connect the database
        conn = sqlite3.connect('/home/techturtl3/databaseFile.db')

        # step 2 create the cursor
        c = conn.cursor()

        c = c.execute("SELECT * FROM myMovies")

        # print all movies
        a = c.fetchall()

        result = []
        # print(a)
        for movies in a:
            for items in movies:
                result.append(items)

        conditioned = ''
        for items in result:
            conditioned += items+' , '

        conn.commit()

        conn.close()
        # print(a)
        return conditioned

        # print(conditioned)

    @staticmethod
    def random_movie():
        # step 1 connect the database
        conn = sqlite3.connect('/home/techturtl3/databaseFile.db')

        # step 2 create the cursor
        c = conn.cursor()
        # get all the movies
        d = c.execute("SELECT * FROM myMovies")

        # gets the amount of movies - by getting the last value from c
        # gets the maximum number of rows/movies
        max = c.execute("SELECT max(rowid) FROM myMovies")
        n = c.fetchone()[0]
        print(n)
        # issue of randomizing from 0 movies need to do it only when more than 1 movie present
        if n > 1:
            i = random.randrange(1, n)

            # pick the random movie using variable from list
            c = c.execute("SELECT*FROM myMovies WHERE rowid={}".format(i))

            # set pick to the last item fetched
            pick = c.fetchone()[0]

            # print the random pick
            #  print('The movie to watch is: ', pick)

            conn.commit()

            conn.close()
            return pick

    # get random shows
    @staticmethod
    def random_show():
        # step 1 connect the database
        conn = sqlite3.connect('/home/techturtl3/databaseFile.db')

        # step 2 create the cursor
        c = conn.cursor()
        # get all the movies
        d = c.execute("SELECT * FROM shows")

        # gets the amount of movies - by getting the last value from c
        # gets the maximum number of rows/movies
        max = c.execute("SELECT max(rowid) FROM shows")
        n = c.fetchone()[0]
        print(n)
        # issue of randomizing from 0 movies need to do it only when more than 1 movie present
        if n > 1:
            i = random.randrange(1, n)

            # pick the random movie using variable from list
            c = c.execute("SELECT*FROM shows WHERE rowid={}".format(i))

            # set pick to the last item fetched
            pick = c.fetchone()[0]

            conn.commit()
            conn.close()
            return pick

    @staticmethod
    def add_shows(showname):
        conn = sqlite3.connect('/home/techturtl3/databaseFile.db')

        # step 2 create the cursor
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS shows (showname TEXT)""")

        # Insert data into the movies table
        c.execute('INSERT INTO shows VALUES (?)', (showname,))

        conn.commit()

        conn.close()

    @staticmethod
    def fetch_shows():
        # step 1 connect the database
        conn = sqlite3.connect('/home/techturtl3/databaseFile.db')

        # step 2 create the cursor
        c = conn.cursor()

        c = c.execute("SELECT * FROM shows")

        fetched_shows = c.fetchall()

        result = []
        # print(a)
        for shows in fetched_shows:
            for items in shows:
                result.append(items)

        conditioned = ''
        for items in result:
            conditioned += items + ' , '

        conn.commit()
        conn.close()
        return conditioned

    @staticmethod
    def clear_movies():
        conn = sqlite3.connect('/home/techturtl3/databaseFile.db')
        c = conn.cursor()

        c = c.execute("DROP table myMovies")

        conn.close()
        return 2

    @staticmethod
    def clear_shows():
        conn = sqlite3.connect('/home/techturtl3/databaseFile.db')
        c = conn.cursor()

        c = c.execute("DROP table shows")

        conn.close()

    @staticmethod
    def clear_all():
        conn = sqlite3.connect('/home/techturtl3/databaseFile.db')
        c = conn.cursor()

        c = c.execute("DROP table myMovies")
        c = c.execute("DROP table shows")

        conn.close()
        return 2
