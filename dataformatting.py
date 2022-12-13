
import pandas as pd
# import regex as re


import mysql.connector as mysql
from mysql.connector import Error

'''
tmdb_5000_movies.csv was used as a .csv file from which the information was taken to create the DB
The file had several columns with different information that was no use to us.
Code below was used to format the above mentioned file using the panda library
For example the genre column had characters like [ or } so we iterated
'''


# # temp = pd.read_csv(r'/Users/besjana/PyCharm/dataset/tmdb_5000_movies.csv')
# # datafile = pd.read_csv(r'/Users/besjana/PyCharm/dataset/tmdb_5000_movies.csv')
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


















