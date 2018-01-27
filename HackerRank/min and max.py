import numpy

a = input().split()
b =[]

for i in range(int(a[0])):
    e=input().split()
    b.append(e)
c = numpy.array(b,int)
d=(numpy.min(c,axis=1))


print(numpy.max(d))
print(d)