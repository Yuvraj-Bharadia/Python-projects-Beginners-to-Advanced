import numpy as np
#! Range
#create nd-array number
number=np.array([0,1,2,3,4,5,6,7,8,9])
#calculate maximum value
max_value=max(number)
#calculate minimum value
min_value=min(number)
#calculate range
range=max_value - min_value
#print value of range 
print(range)

#! Percentile
#create 1d-array number
arr=[20,2,7,1,34]
#calculate first_value
first_value=np.percentile(arr,25)
#calculate second_value
second_value=np.percentile(arr,50)
#calculate third_value
third_value=np.percentile(arr,75)
#print all value 
print(first_value)
print(second_value)
print(third_value)

#! Quartiles
#create nd-array number
arr=np.array([32, 36, 46, 47, 56, 69, 75, 79, 79, 88, 89, 91, 92, 93, 96, 97, 101, 105, 112, 116])
#calculate first quartile
quartile1=np.percentile(arr, 25, interpolation = 'midpoint')
#calculate second quartile
quartile2=np.percentile(arr, 50, interpolation = 'midpoint')
#calculate third quartile
quartile3=np.percentile(arr, 75, interpolation = 'midpoint')
#print all value 
print(quartile1)
print(quartile2)
print(quartile3)

#? Second quartile and median not equal

### central 50 percent distribution
#! Interquartile Range
#calculate IQR
IQR = quartile3 - quartile1
#print value of IQR
print(IQR)

#! Variance, ##$$ Stock market volatily question
import numpy as np
#create nd-array
building_height=np.array([800, 720, 655, 655, 625, 600, 590, 529, 513, 502, 502, 502])
#calculate variance and print its value
variance=np.var(building_height)
print(variance)

#! Standard Deviation
import numpy as np
#create nd-array
weight=np.array([10, 40, 30, 50, 20])
#calculate standard deviation and print its value
std_deviation=np.std(weight)
print(std_deviation)