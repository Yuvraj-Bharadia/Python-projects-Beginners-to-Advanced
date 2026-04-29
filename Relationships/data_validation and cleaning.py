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
