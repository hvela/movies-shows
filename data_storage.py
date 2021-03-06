import sqlite3
# from Shows2 import Movies, Implementation
from shows_movies import Flix
import random

class FlixStorage:

    # method here for adding movies to the database
    def add_movies(self):
        # step 1 connect the database
        conn = sqlite3.connect('databaseFile.db')

        # step 2 create the cursor
        c = conn.cursor()

        # step 3 create the table
        c.execute('CREATE TABLE IF NOT EXISTS movies (movie_name TEXT)')

        # prompt start of program
        Flix.start_program(None)

        # # insert data to the shows table here
        # c.execute('INSERT INTO shows VALUES (?)', (Flix.add_show(None),))

        # Insert data into the movies table
        c.execute('INSERT INTO movies VALUES (?)', (Flix.add_movie(None),))

        # get and print all the movies -------
        print("The movies in the pool are: ")

        # get all the movies
        d = c.execute("SELECT * FROM movies")

        # print all movies
        print(d.fetchall())

        # gets the maximum number of rows/movies
        max = c.execute("SELECT max(rowid) FROM movies")

        # gets the amount of movies - by getting the last value from c
        n = c.fetchone()[0]
        print("There are a total of",n,"movies in the database")

        # issue of randomizing from 0 movies need to do it only when more than 1 movie present
        if n>1:
            print('\n--------radomizing movie--------')

            # generate random value
            i = random.randrange(1, n)

            # print("the random value to get is: ",i)

            # pick the random movie using variable from list
            c.execute("SELECT*FROM movies WHERE rowid={}".format(i))

            # set pick to the last item fetched
            pick = c.fetchone()

            # print the random pick
            print('The movie to watch is: ', pick)

        conn.commit()

        conn.close()

    #   method here to add shows
    def add_shows(self):
        # add shows if user wants to add shows --------------------
        print("____________________________________________________________\n")
        # step 1 connect the database
        conn = sqlite3.connect('databaseFile.db')

        # step 2 create the cursor
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS shows (showname TEXT)""")

        # Insert data into the movies table
        c.execute('INSERT INTO shows VALUES (?)', (Flix.add_show(None),))

        # get and print all the shows -------
        print("The shows in the pool are: ")

        c.execute("SELECT * FROM shows")

        # get all the movies
        d = c.execute("SELECT * FROM shows")

        print(d.fetchall())

        # gets the maximum number of rows/movies
        max = c.execute("SELECT max(rowid) FROM shows")

        # gets the amount of movies - by getting the last value from c
        s = c.fetchone()[0]
        print("There are a total of", s, "shows in the database")

        # issue of randomizing from 0 shows need to do it only when more than 1 shows present
        if s > 1:
            print('\n--------radomizing show--------')

            # generate random value
            j = random.randrange(1, s)

            # print("the random value to get is: ",j)

            # pick the random movie using variable from list
            c.execute("SELECT*FROM shows WHERE rowid={}".format(j))

            # set pick to the last item fetched
            show_pick = c.fetchone()

            # print the random pick
            print('The show to watch is: ', show_pick)

        conn.commit()

        conn.close()

