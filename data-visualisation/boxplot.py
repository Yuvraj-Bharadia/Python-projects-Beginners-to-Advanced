import pandas as pd
data=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/netflix_titles_8085.csv')
import warnings
warnings.filterwarnings("ignore")
tvshow_df= data[data['type'] =='TV Show']
tvshow_df['tv_duration'] = tvshow_df['duration'].map(lambda x: x.rstrip('Season')).astype(int)
movies_df= data[data['type'] =='Movie']
movies_df['movies_duration'] = movies_df['duration'].map(lambda x: x.rstrip('min')).astype(int)
import matplotlib.pyplot as plt

#plot boxplot for movies_df
x=movies_df['movies_duration']
x.plot(kind='box')
plt.xlabel('movies_duration')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.boxplot([tvshow_df['tv_duration'],movies_df['movies_duration']])
plt.show()
