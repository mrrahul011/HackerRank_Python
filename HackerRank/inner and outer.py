import numpy

b=input().split()
c = numpy.array(b,int)

d=input().split()
g = numpy.array(d,int)

print(numpy.inner(c,g))
print(numpy.outer(c,g))

