import pandas as pd
data=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/netflix_titles_8085.csv')
import warnings
#warnings.filterwarnings("ignore")
tvshow_df= data[data['type'] =='TV Show']
tvshow_df['tv_duration'] = tvshow_df['duration'].map(lambda x: x.rstrip('Season')).astype(int)
movies_df= data[data['type'] =='Movie']
movies_df['movies_duration'] = movies_df['duration'].map(lambda x: x.rstrip('min')).astype(int)
import matplotlib.pyplot as plt

#count rating
count_show=movies_df['rating'].value_counts().reset_index()
#print count_show
print(count_show)

#plot bar graph
plt.plot(count_show.index ,count_show.rating)
plt.show()

