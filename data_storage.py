import sqlite3
# from Shows2 import Movies, Implementation
from shows_movies import Flix
import random


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

        # cur.execute("insert into test(d, ts) values (?, ?)", (today, now))

        # data = "INSERT INTO myMovies VALUES(movie)"
        #
        # c.execute(data)
        # get and print all the movies -------
        # print("The movies in the pool are: ")
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


        print(conditioned)

        # print(result)
        counter = 0
        # alist = list(a)
        #
        # print(alist)

        # mu = (5,8,9,4)
        # theList = list(mu)
        # print(theList)

        # get all the movies
        # d = c.execute("SELECT * FROM movies")
        #
        # # print all movies
        # print(d.fetchall())
        #
        # # gets the maximum number of rows/movies
        # max = c.execute("SELECT max(rowid) FROM movies")
        #
        # # gets the amount of movies - by getting the last value from c
        # n = c.fetchone()[0]
        # print("There are a total of",n,"movies in the database")
        #
        # # issue of randomizing from 0 movies need to do it only when more than 1 movie present
        # if n>1:
        #     print('\n--------radomizing movie--------')
        #
        #     # generate random value
        #     i = random.randrange(1, n)
        #
        #     # print("the random value to get is: ",i)
        #
        #     # pick the random movie using variable from list
        #     c.execute("SELECT*FROM movies WHERE rowid={}".format(i))
        #
        #     # set pick to the last item fetched
        #     pick = c.fetchone()
        #
        #     # print the random pick
        #     print('The movie to watch is: ', pick)

        conn.commit()

        conn.close()
        # print(a)
        return conditioned

    #   method here to add shows
    @staticmethod
    def add_shows(showname):
        # add shows if user wants to add shows --------------------
        # print("____________________________________________________________\n")
        # step 1 connect the database
        conn = sqlite3.connect('/home/techturtl3/databaseFile.db')

        # step 2 create the cursor
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS shows (showname TEXT)""")

        # Insert data into the movies table
        c.execute('INSERT INTO shows VALUES (?)', (showname,))

        # get and print all the shows -------
        # print("The shows in the pool are: ")
        #
        # c.execute("SELECT * FROM shows")
        #
        # # get all the movies
        # d = c.execute("SELECT * FROM shows")
        #
        # print(d.fetchall())
        #
        # # gets the maximum number of rows/movies
        # max = c.execute("SELECT max(rowid) FROM shows")
        #
        # # gets the amount of movies - by getting the last value from c
        # s = c.fetchone()[0]
        # print("There are a total of", s, "shows in the database")
        #
        # # issue of randomizing from 0 shows need to do it only when more than 1 shows present
        # if s > 1:
        #     print('\n--------radomizing show--------')
        #
        #     # generate random value
        #     j = random.randrange(1, s)
        #
        #     # print("the random value to get is: ",j)
        #
        #     # pick the random movie using variable from list
        #     c.execute("SELECT*FROM shows WHERE rowid={}".format(j))
        #
        #     # set pick to the last item fetched
        #     show_pick = c.fetchone()
        #
        #     # print the random pick
        #     print('The show to watch is: ', show_pick)

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
