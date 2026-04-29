# exploratory data analysis

import pandas as pd
import numpy as np

'''df = pd.DataFrame([['Yuvraj', 14], ['Aadit', 13]], columns=['name', 'age'])

print(df)'''

'''df = pd.DataFrame({'key1':['value1','value2'],'key2':['value3','value4']})

print(df)'''

'''array = np.array([['John', 20000], ['Sam', 25000],['Yihuai', 27000], ['Annie', 18000],['Robert', 30000]])
index_values = ['1', '2', '3', '4', '5']
column_values = ['Names', 'Salary']
 
# creating the dataframe
df = pd.DataFrame(data = array, index = index_values, columns = column_values)
print(df)'''

#Read csv file
df=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/Employee_detail.csv')

#print dataframe
print(df)

#Read data with no header value
df=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/Employee_detail.csv',header=None)

#print dataframe
print(df)

#Add column name
df=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/Employee_detail.csv',names=['id','name','no_of_year','salary','no_of_leave'], index_col='id')

#print dataframe
print(df)

df=pd.read_excel('datafile_path',header=None,index_col='col_name',names=[col_1,col_2.....col_n])
print(df)

#Read csv file
df=pd.read_csv('https://confrecordings.ams3.digitaloceanspaces.com/heart_8125.csv')

#print dataframe
print(df.head(5))

#shape of dataframe
print(df.shape)

#describe the dataframe
print(df.describe())

#check null values
print(df.isnull().sum())

#calculate total_no
total_no=df['target'].nunique()

#print the total_no
print(total_no)

#calculate the count variables
count=df['target'].value_counts()

#print the count variables
print(count)

