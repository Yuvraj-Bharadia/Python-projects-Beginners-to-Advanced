import pandas as pd

df = pd.DataFrame({'alphabets':['A','B','C','D','E'],'numbers':[1,2,3,4,5]})

#print top 5 rows
print(df.head())

#print number of rows and columns
print(df.shape)

#transpose the df dataframe
transposed = df.transpose()

"""copybool, default False

Whether to copy the data after transposing, even for DataFrames with a single dtype.

Note that a copy is always required for mixed dtype DataFrames, or for DataFrames with any extension types."""
# transposed = df.T

#print top 5 rows of transposed dataframe
print(transposed.head())

#print shape of transposed dataframe
print(transposed.shape)
