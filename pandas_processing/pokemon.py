import pandas as pd

# pokemon assignment
df = pd.read_csv("https://confrecordings.ams3.digitaloceanspaces.com/Pokemon.csv")

print(df.head(10))
print(df.tail(10))
print(df.shape)
print(df.columns)
print(df.describe())
print(df.dtypes)
print(df.isnull().sum())
df.drop(df['#'], axis=1, inplace=True)
print(df.shape)
df.set_index("Name", inplace = True)
print(df["Type 1"].unique())
print(df["Type 1"].value_counts())
print(df["Type 2"].unique())
print(df["Legendary"].nunique())

df['Type 2'].fillna("None",inplace=True)
print(df['Type 2'])
print(df.isnull().sum())

# print(df['Name']=='Bulbasaur')

print(df.head())
df.drop('Bulbasaur', inplace = True, axis = 0)
print(df.head())