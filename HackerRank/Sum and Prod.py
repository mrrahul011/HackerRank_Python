import numpy

a = input().split()
b =[]

for i in range(int(a[0])):
    e=input().split()
    b.append(e)
c = numpy.array(b,int)
d=(numpy.sum(c,axis=0))


print(numpy.prod(d))
print(d)