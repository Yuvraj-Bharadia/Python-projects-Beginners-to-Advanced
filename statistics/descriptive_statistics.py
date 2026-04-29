#import numpy module
import numpy as np
#create mytuple
mytuple=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#create nd-array
arr=np.array(mytuple)
#print nd-array
print(arr)
#print type of arr
print(type(arr))

# Mean
#Create nd-array marks
marks=np.array([10,12,17,17,20,17,29,12,98,100])
#Calculate mean_value
mean_value=np.mean(marks)
#print value of mean_value
print(mean_value)

# Median
marks=np.array([10,12,17,17,20,17,29,12,98,100])
#Calculate median value
median_value=np.median(marks)
#Print median value
print(median_value)

#import library
from scipy import stats
import numpy as np
marks=np.array([10,12,17,17,20,17,29,12,98,100])
#calculate mode value
mode_value=stats.mode(marks)
#print mode value
print(mode_value)

# Skewness is teh affect of mean and median
# Import in thE gdp per capita example so if more people are rich or poor
# Skewness calculation = ____
#                        Mean   -  Mode /
#                       Standard Deviation



'''In the applications of skewness, there is a confusion in positively skewed and negatively skewed'''


