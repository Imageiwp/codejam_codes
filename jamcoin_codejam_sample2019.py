import math
t=int(input())
c=0
for i in range(t):
    n=int(input())
    c=c+1
    l=list(str(n))
    for k in range(len(l)):
        if(int(l[k])==4):
            l[k]='3'
    lower=''
    lower=int(lower.join(l))
    for j in range(lower,n):
        if('4' not in list(str(j))):
            a=j
            b=n-j
            if('4' not in list(str(b))):
                break
              
    print('Case #'+str(c)+":",end=" ")
    print(a,end=" ")
    print(b)
    
    
    
