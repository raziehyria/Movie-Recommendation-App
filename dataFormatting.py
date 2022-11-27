import pandas as pd
# import regex as re
import csv

import mysql.connector as mysql
from mysql.connector import Error


moviedata = pd.read_csv('/Users/besjana/PyCharm/dataset/dataset.csv', index_col=False, delimiter=',', quotechar='"',quoting=csv.QUOTE_ALL)
print(moviedata.head()) # displays the dataset.csv file

mydb = mysql.connect(
    host="localhost",
    username="root",
    password="",
    database="movie_rec"
)

mycursor = mydb.cursor()

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
                         "release_date DATE NOT NULL,"
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
except Error as e:
    print("Error while connecting to MySQL", e)

# mycursor.execute("CREATE DATABASE movie_rec")

# define and create the table "movies"
"""create_table = '''CREATE TABLE movies (
                id INTEGER PRIMARY KEY NOT NULL,
                genres TEXT NOT NULL,
                plot TEXT NOT NULL,
                release_date DATE NOT NULL,
                ratings FLOAT NOT NULL,
                title TEXT NOT NULL
                );'''"""

# file = open('dataset.csv')
# Read the contents of the datasetFinal.csv file into the movies table
# contents = csv.reader(file)
