import pandas as pd
data=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/netflix_titles_8085.csv')

print(data.director.value_counts())

movies_df = data[data['type'] == 'Movie']

movies_df1 = movies_df[movies_df['director'] == 'Hakan Algül']

print(movies_df1['title'])

list_of_values = ['Hakan Algül', 'Robert Vince']

movies_df2 = y = movies_df[movies_df['director'].isin(list_of_values)]

print(movies_df2)