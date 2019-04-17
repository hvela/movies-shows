import sqlite3
# from Shows2 import Movies, Implementation
from ShowsAndMovies import Flix
import random

class FlixStorage:

    #step 1 connect the database
    conn = sqlite3.connect('a_dbfile.db')

    #step 2 create the cursor

    c = conn.cursor()

    #step 3 create the table
    c.execute('CREATE TABLE IF NOT EXISTS movies (movie_name TEXT)')

    c.execute("""CREATE TABLE IF NOT EXISTS shows (
              showname name)""")

    Flix.start_program(None)

    # insert data to the shows table here
    c.execute('INSERT INTO shows VALUES (?)', (Flix.add_show(None),))

    # Insert data into the movies table
    c.execute('INSERT INTO movies VALUES (?)', (Flix.add_movie(None),))

    #print all the movies -------
    print("The movies in the pool are: \n")
    c.execute("SELECT * FROM movies")
    print(c.fetchall())

    for row in c.fetchall():
        print(row)


    d = c.execute("SELECT * FROM movies")

    max = c.execute("SELECT max(rowid) FROM movies")
    n = c.fetchone()[0]
    print(n)

    i = random.randrange(1,n-1)

    c.execute("SELECT*FROM movies WHERE rowid={}".format(i))
    pick = c.fetchone()[0]
    print('The movie to watch is: ',pick)



    #print all the shows------
    print("\n\nThe shows in the pool are: \n")
    c.execute("SELECT * FROM shows")
    print(c.fetchall())

    for row in c.fetchall():
        print(row)


    d = c.execute("SELECT * FROM shows")

    max = c.execute("SELECT max(rowid) FROM shows")
    n = c.fetchone()[0]
    print(n)

    i = random.randrange(1,n-1)

    c.execute("SELECT*FROM shows WHERE rowid={}".format(i))
    pick_show = c.fetchone()[0]
    print('The show to watch is: ',pick_show)


    #this commits the changes
    conn.commit()

    #close the connection
    conn.close()






# import sqlite3
# # from Shows2 import Movies, Implementation
# from Shows2 import Implementation
# import random
#
# #step 1 connect the database
# conn = sqlite3.connect('a_dbfile.db')
#
# #step 2 create the cursor
#
# c = conn.cursor()
#
# #step 3 create the table
# c.execute('CREATE TABLE IF NOT EXISTS movies (movie_name TEXT)')
#
# c.execute("""CREATE TABLE IF NOT EXISTS shows (
#           showname name)""")
#
#
# # insert data to the shows table here
# c.execute('INSERT INTO shows VALUES (?)',(Implementation.showname,))
#
#
# # Insert data into the movies table
# c.execute('INSERT INTO movies VALUES (?)',(Implementation.moviename,))
#
#
# #print all the movies -------
# print("The movies in the pool are: \n")
# c.execute("SELECT * FROM movies")
# print(c.fetchall())
#
# for row in c.fetchall():
#     print(row)
#
#
# d = c.execute("SELECT * FROM movies")
#
# max = c.execute("SELECT max(rowid) FROM movies")
# n = c.fetchone()[0]
# print(n)
#
# i = random.randrange(1,n-1)
#
# c.execute("SELECT*FROM movies WHERE rowid={}".format(i))
# pick = c.fetchone()[0]
# print('The movie to watch is: ',pick)
#
#
#
# #print all the shows------
# print("\n\nThe shows in the pool are: \n")
# c.execute("SELECT * FROM shows")
# print(c.fetchall())
#
# for row in c.fetchall():
#     print(row)
#
#
# d = c.execute("SELECT * FROM shows")
#
# max = c.execute("SELECT max(rowid) FROM shows")
# n = c.fetchone()[0]
# print(n)
#
# i = random.randrange(1,n-1)
#
# c.execute("SELECT*FROM shows WHERE rowid={}".format(i))
# pick_show = c.fetchone()[0]
# print('The show to watch is: ',pick_show)
#
#
#
#
# # print(Movies.movietime)
#
# #this commits the changes
# conn.commit()
#
# #close the connection
# conn.close()


