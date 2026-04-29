# To derive information from exisiting columns  

import pandas as pd
data=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/netflix_titles_8085.csv')

#check type
print(data['duration'].dtypes)

#Print the top 10 values of 'duration' column
print(data['duration'].head(10))

#Print the two columns 'type' , 'duration' values.
print(data[['type','duration']])


import warnings
warnings.filterwarnings("ignore")

#create new dataframe for type 'movies'
movies_df = data[data["type"] == 'Movie']

#print all column name of new dataframe
print(movies_df.columns)

#Eliminate "min" from type column of movies_df
movies_df["movies_duration"] = movies_df['duration'].map(lambda x: x.rstrip('min')).astype(int)

#print the top 5 values of movie_duration column
print(movies_df['movie_duration'].head())

#create new dataframe for type 'TV Show'
tvshow_df= data[data["type"] =='TV Show']

#print all column name of new dataframe
print(tvshow_df.columns)

#Eliminate Season from type column of tvshow_df
tvshow_df["tv_duration"] = tvshow_df['duration'].map(lambda x: x.rstrip('Season')).astype(int)

#print the top 5 values of tvshow_df column
print(tvshow_df['tv_duration'].head())



#! Cast Members apply()

import pandas as pd

data=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/netflix_titles_8085.csv')

#check null value
print(data.isnull().sum())

#replace with nan
movies_df.cast.fillna("nan", inplace=True)

movies_df['count_mov']=movies_df['cast'].str.split(',').apply(len)

#display two columns cast and count_mov
print(movies_df[["cast","count_mov"]].head()) 