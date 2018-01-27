import numpy

a=input().split()
b=[]
for i in range(int(a[0])):
    c=input().split()
    b.append(c)
    
b=numpy.array(b,float)

print(numpy.linalg.det(b))
    