import numpy as np

a = input().strip().split()
x = int(a[0])
y = int(a[1])

b =[]
c = []

for i in range(x):
    d = input().strip().split()
    b.append(d)

for i in range(y):
    e = input().strip().split()
    c.append(e)

f = np.array(b,int)

g = np.array(c,int)

h = np.concatenate((f,g))
print(h)

#%%
#Comprehension Method

import numpy as np

a = input().strip().split()
x = int(a[0])
y = int(a[1])

b = np.array([input().strip().split() for i in range(x)],int)
c = np.array([input().strip().split() for i in range(y)],int)

h = np.concatenate((b,c))
print(h)