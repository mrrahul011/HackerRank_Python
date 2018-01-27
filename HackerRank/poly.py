import numpy as np

c = input().split()
c=np.array(c,float)
d = input().split()
b=int(d[0])
print(np.polyval(c,b))