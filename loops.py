'''start = int(input("Plese enter a start value: "))
stop = int(input("Plese enter a stop value: "))
step = int(input("Plese enter a step value: "))

for i in range(start, stop, step):
    print(i)'''



'''n = int(input("please enter the number you want to print the table off: "))

for i in range( 1, 11):
    print(n, "x", i, "=", n*i)'''



'''fact = int(input("please enter the number you want a factorial off"))
f = 1
for i in range(fact, 0, -1):
    f = f*i

print("The factorial of you number is", f)'''



'''n = int(input("Please enter a number for checking if its prime or not: "))
for i in range(2, n):
    if n%i == 0:
        print(n, "is not a prime number")
        break
else:
    print(n, "is a prime number")'''


'''n = int(input("Please enter the number of terms you need in the faboinacii series: "))
f = 0
s = 1
print(f)
print(s)
for i in range(3, n+1):
    n1 = f+s
    print(n1)
    f=s
    s=n1'''

##HW
'''n = int(input("Please enter the power of the number: "))
x = int(input("Please give the number: "))
sum = 0

for i in range(1, n+1):
    sum = sum + x**i

print(sum)

n = int(input("Please enter the power of the number: "))
x = int(input("Please enter your denominator: "))
sum = 0

for i in range(1, n+1):
    sum = sum + 1/(x**i)

print(sum)'''

#Find the largest item from agiven list
'''List=[0,2,3,4,5,6,7,8,9]

largest = List[0]
smallest = List[0]

for i in List:
    if i >= largest:
        largest = i
    
    if i <= smallest:
        smallest = i

print(largest)
print(smallest)'''


#While Loop

'''x = int(input("Enter the number you want a factorial of"))
i = 1
fact = 1
while i <= x:
    fact = fact*i
    i += 1

print(fact)'''

#While loop sum of the digits in a no
'''x = input("The number = ")
sum = 0
for i in x:
    sum = sum + int(i)

print(sum)'''

#multiply digits in a no
'''x = input("The number = ")
sum = 1
for i in x:
    sum = sum * int(i)

print(sum)'''

#Nested Loops
'''for i in range(5):
    for j in range(6,11):
        print(str(i)+str(j),end = "  ")
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        print(j, end = "  ")
    print()'''

'''for i in range(1,6):
    for j in range(1,6):
        print(i, end = "  ")
    print()'''

'''for i in range(1,6):
    for j in range(1,i+1):
        print(j, end = "  ")
    print()'''

'''for i in range(1,6):
    for j in range(1, i+1):
        print(i, end = "  ")
    print()'''

'''x = 1
for i in range(1,6):
    for j in range(1,i+1):
        print(x, end = "  ")
        x += 1
    print()'''

'''for i in range(5,0,-1):
    for j in range(1, i+1):
        print(i, end = "  ")
    print()'''

'''for i in range(5,0,-1):
    for j in range(1, i+1):
        print(j, end = "  ")
    print()'''

'''x = 1
for i in range(5,0,-1):
    for j in range(1, i+1):
        print(x, end="  ")
        x += 1
    print()'''