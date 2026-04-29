#! Will learn qdratic and exponetial

import warnings
warnings.filterwarnings("ignore")
import pandas as pd

#Load data
df=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/netflix_titles_8085.csv')

#Check null values
print(df.isnull().sum())

#Check the datatype
print(df.dtypes)

#Create a new dataframe called movies_df
movies_df= df[df['type'] =='Movie']

#Eliminating the 'min' from 'duration' in movies_df
movies_df['movies_duration'] = movies_df['duration'].map(lambda x: x.rstrip('min')).astype(int)

#Check the first 5 rows of movies_df
print(movies_df.head())


#import library
import matplotlib.pyplot as plt

#plot the scatter graph
plt.scatter(x=movies_df['release_year'],y=movies_df['movies_duration'])
plt.xlabel('release year')
plt.ylabel('movies duration')
plt.show()

#! Try with pandas df.plot.scatter()





#? Correlation discussion

#import library
import seaborn as sns

#Find correlation matrix and print it.
corr_data=movies_df.corr()
print(corr_data)

# Formula for calculation correlation coefficient

#Plot the correlation matrix
sns.heatmap(corr_data, annot=True)
plt.show()

