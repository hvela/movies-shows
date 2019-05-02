import sqlite3
# from Shows2 import Movies, Implementation
from ShowsAndMovies import Flix
import random

class FlixStorage:
    # step 1 connect the database
    conn = sqlite3.connect('databaseFile.db')

    # step 2 create the cursor
    c = conn.cursor()

    # step 3 create the table
    c.execute('CREATE TABLE IF NOT EXISTS movies (movie_name TEXT)')

    c.execute("""CREATE TABLE IF NOT EXISTS shows (showname TEXT)""")

    # prompt start of program
    Flix.start_program(None)

    # insert data to the shows table here
    c.execute('INSERT INTO shows VALUES (?)', (Flix.add_show(None),))

    # Insert data into the movies table
    c.execute('INSERT INTO movies VALUES (?)', (Flix.add_movie(None),))

    # get and print all the movies -------
    print("The movies in the pool are: ")
    c.execute("SELECT * FROM movies")
    print(c.fetchall())

    # get all the movies
    d = c.execute("SELECT * FROM movies")

    max = c.execute("SELECT max(rowid) FROM movies")
    # get and print number of movies
    n = c.fetchone()[0]
    print(n)

    # variable to randomize movie
    i = random.randrange(0, n)

    c.execute("SELECT*FROM movies WHERE rowid={}".format(i))
    # set variable to what has been chosen
    pick = c.fetchone()
    # print the random pick
    print('The movie to watch is: ', pick)

    # print all the shows --------
    print("\nThe shows in the pool are: ")
    c.execute("SELECT * FROM shows")
    print(c.fetchall())

    for row in c.fetchall():
        print(row)

    # get all the shows
    d = c.execute("SELECT * FROM shows")

    # get all shows and print
    max = c.execute("SELECT max(rowid) FROM shows")
    n = c.fetchone()[0]
    print(n)

    # get random show and store in variable
    i = random.randrange(1,n-1)

    # print the random show
    c.execute("SELECT*FROM shows WHERE rowid={}".format(i))
    pick_show = c.fetchone()[0]
    print('The show to watch is: ',pick_show)



