import pandas as pd
data=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/netflix_titles_8085.csv')

import warnings
warnings.filterwarnings("ignore")

y=lambda x: x+"hrs"

print(y("4"))

## changing a string
#    movies_df["movies_duration"] = movies_df['duration'].map(lambda x: x.rstrip("min") + "hrs")
