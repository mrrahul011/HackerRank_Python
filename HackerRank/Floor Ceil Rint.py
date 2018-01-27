import numpy

a = input().split()
a = numpy.array(a,float)

print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))