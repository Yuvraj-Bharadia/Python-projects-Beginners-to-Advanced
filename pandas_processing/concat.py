# importing the module
import pandas as pd

# creating the DataFrames
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
'B': ['B0', 'B1', 'B2', 'B3']})
print('df1:', df1)
df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
'B': ['B4', 'B5', 'B6', 'B7']})
print('df2:', df2)

# concatenating
print('After concatenating:')
print(pd.concat([df1, df2],
keys = ['key1', 'key2']))
print(pd.concat([df1, df2],
axis = 1))