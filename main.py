# import sqlite3
# 
import pandas as pd
# import regex as re
import csv

import mysql.connector as mysql
from mysql.connector import Error

'''
tmdb_5000_movies.csv was used as a .csv file from which the information was taken to create the DB
The file had several columns with different information that was no use to us.
Code below was used to format the above mentioned file using the panda library
For example the genre column had characters like [ or } so we iterated
'''


# # temp = pd.read_csv(r'/Users/besjana/Desktop /archive/tmdb_5000_movies.csv')
# # datafile = pd.read_csv(r'/Users/besjana/Desktop /archive/tmdb_5000_movies.csv')
# # 
# # 
# # temp.head()
# # temp.info() # shows the information about the columns and then how many rows 
# # temp.describe()
# # 
# # # cleaning genres
# # dlist = []
# # for i in temp['genres']:
# #     check=i.replace('[','')
# #     check=check.replace('{','')
# #     check=check.replace(']','')
# #     check=check.replace('}','')
# #     check =re.sub('"id":','', check)
# #     check=check.replace('"','')
# #     check=check.replace(' ','')
# #     check =re.sub('name:','', check)
# #     check =re.sub("\d+,",'', check)
# #     dlist.append(check)
# # 
# # temp['genres']=dlist
# # temp['genres']
# # 
# # temp['genres'] = temp['genres'].astype(str).str.split(",")
# # temp = temp.explode("genres", ignore_index=True)
# # print(temp)
# # 
# # temp=temp.drop(['homepage'],axis=1)
# # temp=temp.drop(['tagline'],axis=1)
# # # temp=temp.drop(['overview'],axis=1)
# # temp = temp.drop(['keywords'],axis=1)
# # temp = temp.drop(['original_language'],axis=1)
# # temp = temp.drop(['production_companies'],axis=1)
# # temp = temp.drop(['production_countries'],axis=1)
# # temp = temp.drop(['revenue'],axis=1)
# # temp = temp.drop(['spoken_languages'],axis=1)
# # temp = temp.drop(['popularity'],axis=1)
# # temp = temp.drop(['budget'],axis=1)
# # temp = temp.drop(['original_title'],axis=1)
# # temp = temp.drop(['runtime'],axis=1)
# # temp = temp.drop(['vote_count'],axis=1)
# # temp = temp.drop(['status'],axis=1)
# # 
# # 
# # temp = temp.drop_duplicates(['title'])
# # 
# # print('\nThis is the new database \n\n',temp)
# 
# 
# # # newfile = pd.write_csv(r'/Users/besjana/Desktop /archive/tmdb_5000_movies_new.csv')
# # temp.to_csv('dataset.csv')
# 
# data = pd.read_csv(r'/Users/besjana/PyCharm/dataset/dataset.csv')
# df = pd.DataFrame(data)
# 
# # connecting to a database
# connection = sqlite3.connect('movieRec')
# 
# # create a cursor object to execute SQL queries on a database table
# cursor = connection.cursor()
# 
# # # define the table
# # create_table = '''CREATE TABLE movies (
# #                 id INTEGER PRIMARY KEY NOT NULL,
# #                 genres TEXT NOT NULL,
# #                 plot TEXT NOT NULL,
# #                 release_date DATE NOT NULL,
# #                 ratings FLOAT NOT NULL,
# #                 title TEXT NOT NULL
# #                 );'''
# # 
# # # Create the table into the database
# # cursor.execute(create_table)
# 
# # Open the datasetFinal.csv file
# file = open('dataset.csv')
# # Read the contents of the datasetFinal.csv file into the movies table
# contents = csv.reader(file)
# 
# # SQL query to insert data into the movies tables
# insert_records = "INSERT INTO movies (id, genres, plot, release_date, ratings, title) VALUES (?, ?, ?, ?, ?, ?)"
# 
# # Import the contents of the file into the movies table
# cursor.executemany(insert_records, contents)
# 
# '''
# SQL query that retrieves all data from the movies table
# Verifies that the data was successfully inserted into the table
# '''

# Open the datasetFinal.csv file
moviedata = pd.read_csv('/Users/besjana/PyCharm/dataset/dataset.csv', index_col=False, delimiter=',')
print(moviedata.head()) # displays the dataset.csv file

mydb = mysql.connect(
    host="localhost",
    username = "root",
    password = "",
    database = "movie_rec"
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
                         "genres TEXT NOT NULL,"
                         "plot TEXT NOT NULL,"
                         "release_date DATE NOT NULL,"
                         "ratings FLOAT NOT NULL,"
                         "title TEXT NOT NULL)")
        
        print('Table is created....')
        
        #  loop through the data frame
        for i,row in moviedata.fillna(-1).iterrows():
            sql = "INSERT INTO movie_rec.movies VALUES (%s,%s,%s,%s,%s,%s)"
            mycursor.execute(sql, tuple(row))
            print("Record inserted")
            # the connection is not auto committed by default, so we must commit to save the changes
            mydb.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
            







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

# SQL query to insert data into the movies tables
# insert_records = "INSERT INTO movies (id, genres, plot, release_date, ratings, title) VALUES (?, ?, ?, ?, ?, ?)"

# Import the contents of the file into the movies table
# mycursor.executemany(insert_records, contents)

# Committing the changes
# mydb.commit()

'''
SQL query that retrieves all data from the movies table
Verifies that the data was successfully inserted into the table
'''
# select_all = "SELECT * FROM movies"
# rows = mycursor.execute(select_all).fetchall()
# 
# 
# # Output to the console screen
# for r in rows:
#     print(r)
# 
# Committing the changes
# connection.commit()
# 
# # closing the database connection
# connection.close()










