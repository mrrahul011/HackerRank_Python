
#%%

import numpy

a = input().strip().split()
x = int(a[0])
y = int(a[1])
A = []
B = []

for i in range(x):
    a = input().strip().split()
    A.append(a)
A = numpy.array(A,int)

for i in range(x):
    b = input().strip().split()
    B.append(b)
B = numpy.array(B,int)
print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(numpy.floor_divide(A,B))
print(numpy.mod(A,B))
print(numpy.power(A,B))

#%%

#Comprehension method

import numpy

a = input().strip().split()
x = int(a[0])
A = numpy.array([input().strip().split() for i in range(x)],int)
B = numpy.array([input().strip().split() for i in range(y)],int)
print(numpy.add(A,B))
print(numpy.subtract(A,B))
print(numpy.multiply(A,B))
print(numpy.floor_divide(A,B))
print(numpy.mod(A,B))
print(numpy.power(A,B))
