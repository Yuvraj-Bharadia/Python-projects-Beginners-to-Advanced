# Python program to convert
# dictionary to numpy array

# Import required package
#! discuss
import numpy as np

# Creating a Dictionary
# with Integer Keys
dict = {1: 'All',
2: 'For',
3: 'Apples'}

print(dict)

# to return a group of the key-value
# pairs in the dictionary
result = dict.items()

print(result)

# Convert object to a list
data = list(result)

print(data)

# Convert list to an array
numpyArray = np.array(data)

# print the numpy array
print(numpyArray)
print(numpyArray.ndim)
print(numpyArray.shape)

'''discussion'''