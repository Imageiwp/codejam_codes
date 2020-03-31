t=int(input())
z=0
for i in range(t):
    m=[]
    n,k,p=map(int,input().split())
    for j in range(n):
        l=list(map(int,input().split()))
        m.append(l)
    s=0
    for j in range(len(m)):
        for t in range(len(m[j])):
            if(m[j][t]==max(m[j])):
                pos=t
        
      
        if((p-(pos+1))>=0):
            for k in range(len(m[j])):
                if(p>0):
                    if(k<=pos):
                        s=s+m[j][k]
                        p=p-1
            if((j+1)==len(m)):
                if(p!=0):
                    for k in range(pos+1,len(m)):
                        s=s+m[j][k]
                        
        else:
            continue
    z=z+1
    
    print("Case #"+str(z)+": "+str(s))
    
    









 
            
                           
                    
                                   
                               
                    
        
