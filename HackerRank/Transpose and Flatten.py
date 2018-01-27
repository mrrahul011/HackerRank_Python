import numpy as np

b = input().strip().split()
x = int(b[0])
y = int(b[1])
c=[]

for i in range(int(x)):
    d = (input().split())
    c.append(d)
    
b = np.array(c,int)    
print(b)
print(np.transpose(b))
print(b.flatten())   

