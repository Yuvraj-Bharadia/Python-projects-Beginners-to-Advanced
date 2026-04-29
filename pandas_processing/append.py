import pandas as pd

#first dataframe
df = pd.DataFrame([[1, 2, 4], [3, 4, 6]], columns=list('ABC'), index=['x', 'y'])

#print top 5 rows
print(df.head())

#second dataframe
df2 = pd.DataFrame([[5, 6, 9], [7, 8, 10]], columns=list('ABC'), index=['f', 'g'])

#print top 5 rows
print(df2.head())

#Append second dataframe into first one
appended = df.append(df2, ignore_index = False, verify_integrity = True, sort = True)

#print top 5 row of appended
print(appended.head())

#ignore index and see top 5 rows 
ignored_index = df.append(df2, ignore_index=True)
print(ignored_index.head())
