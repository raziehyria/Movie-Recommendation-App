import pandas as pd
import re
class Node():
    #Implementation for N-Ary Tree which is a generic tree. One that can have multiple children. We will use this to create the tree such that they can be created based on year released, ratings and genre.

    def __init__(self, data):
        self.data = data
        self.child = []

#driver code to create N-Ary Tree

data = pd.read_csv('dataset.csv')
title = Node("Start") # Root Node

#First Parent Nodes
(title.child).append(Node('Genre'))
(title.child).append(Node('Ratings'))
(title.child).append(Node('Year'))

#First Child Nodes
(title.child[0].child).append(Node('Action'))
(title.child[0].child).append(Node('Romance'))
(title.child[0].child).append(Node('Drama'))
(title.child[0].child).append(Node('Horror'))
(title.child[0].child).append(Node('Sci-Fi'))
(title.child[0].child).append(Node('Comedy'))
(title.child[0].child).append(Node('Thriller'))


(title.child[1].child).append(Node('3-4 Stars'))
(title.child[1].child).append(Node('4-5 Stars'))
(title.child[1].child).append(Node('5-6 Stars'))
(title.child[1].child).append(Node('6-7 Stars'))
(title.child[1].child).append(Node('7-8 Stars'))
(title.child[1].child).append(Node('8-9 Stars'))
(title.child[1].child).append(Node('9-10 Stars'))


(title.child[2].child).append(Node('2020 and beyond'))
(title.child[2].child).append(Node('2017-2019'))
(title.child[2].child).append(Node('2015-2017'))
(title.child[2].child).append(Node('2010-2015'))
(title.child[2].child).append(Node('Before 2010'))

df = pd.DataFrame(data,columns=['title','genres','Year','ratings']) # dataframe to extract necessary information to classify into trees




for index in df.index:
    #Adds leaf nodes to tree which will allow for us to give reccomendations
    #Starting with genres
    if df['genres'][index] == 'Action':
        (title.child[0].child[0].child).append(Node(df['title'][index]))

    if df['genres'][index] == 'Romance':
        (title.child[0].child[1].child).append(Node(df['title'][index]))

    if df['genres'][index] == 'Drama':
        (title.child[0].child[2].child).append(Node(df['title'][index]))

    if df['genres'][index] == 'Horror':
        (title.child[0].child[3].child).append(Node(df['title'][index]))

    if df['genres'][index] == 'ScienceFiction':
        (title.child[0].child[4].child).append(Node(df['title'][index]))

    if df['genres'][index] == 'Comedy':
        (title.child[0].child[5].child).append(Node(df['title'][index]))

    if df['genres'][index] == 'Thriller':
        (title.child[0].child[6].child).append(Node(df['title'][index]))


#Converting the dataframe items into int we are able to easily compare the entries with the given user parameters

    if (int(df['Year'][index])<2015) and (int(df['Year'][index])>=2010):
        (title.child[2].child[3].child).append(Node(df['title'][index]))

    if (int(df['Year'][index])<2010):
        (title.child[2].child[4].child).append(Node(df['title'][index]))

    if int(df['Year'][index])>2015 and int(df['Year'][index])<2017:
        (title.child[2].child[2].child).append(Node(df['title'][index]))

    if int(df['Year'][index])<=2019 and int(df['Year'][index])>=2017:
        (title.child[2].child[1].child).append(Node(df['title'][index]))

    if int(df['Year'][index])>=2020:
        (title.child[2].child[1].child).append(Node(df['title'][index]))

#Like in the case of Release Year, we are again converting the ratings into a numerical comparable data type float in this case, and then classifying ratings

    if float(df['ratings'][index]) < 4.0:
        (title.child[1].child[0].child).append(Node(df['title'][index]))

    if float(df['ratings'][index]) >= 4.0 and float(df['ratings'][index]) < 5.0:
        (title.child[1].child[1].child).append(Node(df['title'][index]))

    if float(df['ratings'][index]) >= 5.0 and float(df['ratings'][index]) < 6.0:
        (title.child[1].child[2].child).append(Node(df['title'][index]))

    if float(df['ratings'][index]) >= 6.0 and float(df['ratings'][index]) < 7.0:
        (title.child[1].child[4].child).append(Node(df['title'][index]))

    if float(df['ratings'][index]) >= 7.0 and float(df['ratings'][index]) < 8.0:
        (title.child[1].child[5].child).append(Node(df['title'][index]))

    if float(df['ratings'][index]) >= 8.0 and float(df['ratings'][index]) < 9.0:
        (title.child[1].child[6].child).append(Node(df['title'][index]))

    if float(df['ratings'][index]) >= 9.0 and float(df['ratings'][index]) <= 10.0:
        (title.child[1].child[0].child).append(Node(df['title'][index]))










