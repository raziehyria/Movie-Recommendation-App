import pandas as pd
import csv

import mysql.connector as mysql
from mysql.connector import Error


moviedata = pd.read_csv('dataset.csv', index_col=False, delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL)

# creates connection to the machine and creates there a Database called movie_rec
try:
    mydb = mysql.connect(
        host="localhost",
        username="root",
        password="",  
    )
    if mydb.is_connected():
        create_db_query = "CREATE DATABASE movie_rec"
        with mydb.cursor() as mycursor:
            mycursor.execute(create_db_query)
except Error as e:
    print("Error while creating DB", e)

# connects to the movie_rec db created above and creates a new table
try:
    mydb = mysql.connect(
        host="localhost",
        username="root",
        password="",
        database="movie_rec"
    )
    if mydb.is_connected():
        mycursor = mydb.cursor()  
        mycursor.execute("select database();")
        record = mycursor.fetchone()
        print("You are connected to database: ", record)
        mycursor.execute('DROP TABLE IF EXISTS movies;')
        print('Creating table.....')

        mycursor.execute("CREATE TABLE movies(id INTEGER PRIMARY KEY NOT NULL,"
                         "genres TEXT,"
                         "plot TEXT,"
                         "release_date YEAR NOT NULL,"
                         "ratings FLOAT NOT NULL,"
                         "title TEXT NOT NULL)")

        print('Table is created....')

        #  loop through the data frame
        for i, row in moviedata.fillna(-1).iterrows():
            sql = "INSERT INTO movie_rec.movies VALUES (%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save the changes
            mydb.commit()

        select_movies_query = """
                        SELECT genres,plot,release_date,ratings,title
                        FROM movies
                        WHERE genres = "Action" 
                        AND release_date= 2013 
                        AND ratings > 7 AND ratings < 8
                         """

        mycursor.execute(select_movies_query)
        print('selecting.....')
        print('selection is made....')
        for movie in mycursor.fetchall():
            print(movie)
            # the connection is not auto committed by default, so we must commit to save the changes
            mydb.commit()
except Error as e:
    print("Error while connecting to MySQL", e)


# closing the database connection
# mydb.close()
