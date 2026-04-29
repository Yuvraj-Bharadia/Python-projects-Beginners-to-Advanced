#import library
import pandas as pd
#Read csv file and store in data
data=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/netflix_titles_8085.csv')
print(data.head(5))

#print dimension of dataframe
print(data.shape)
#print all columns name
print(data.columns)

#print data type of every column
print(data.dtypes)