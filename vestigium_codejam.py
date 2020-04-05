import numpy as np
t=int(input())
z=0
for i in range(t):
    n=int(input())
    s=0
    r=0
    c=0
    m=[]
    for j in range(n):
        l=list(map(int,input().split()))
        m.append(l)
        s= s + l[j]
        if(len(set(l)) != len(l) ):
            r=r+1
    p=np.array(m).transpose().tolist()
    for j in range(n):
        if(len(set(p[j])) != len(p[j]) ):
            c=c+1
    z=z+1
    print('Case #' + str(z) + ': ' + str(s) + ' ' + str(r) + ' ' + str(c)) 
            
