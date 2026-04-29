# Complete case analysis
#import libraries and read the data

#? Missing at Random
import pandas as pd
df=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/Life_Expectancy_Data.csv')

#inspect data
print(df.isnull().sum())
print(df.isnull())
print(df.shape)
cca = df.dropna(axis = 0)
print(cca.shape)
print(cca.isnull().sum())

#Arbitrary value imputation
#? Missing not at random

# Check unique values in column
print(df.Status.unique())

#replaces the NULL values with a specified value
df['Status'] = df['Status'].fillna('Missing')

#Numerical
# ! Arbitrary value imputation try'''
df['GDP'] = df['GDP'].fillna(999999)

#check again unique values in column
print(df.Status.unique())
print(df.GDP.unique())
print(df.isnull().sum())


# Frequency category imputation
import pandas as pd

df=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/Life_Expectancy_Data.csv')

print(df.isnull().sum())
print(df.Status.value_counts())
df['Status'] = df['Status'].fillna('Developing')

print(df.Status.value_counts())
print(df.isnull().sum())

# Clearance: Missing not at random is when people refuse to give data