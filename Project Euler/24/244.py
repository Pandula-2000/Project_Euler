p = [1,1,1]

lst=list(range(3))

for a in lst:
    n=0
    p[n]=a
    
    lst1=lst.copy()
    lst1.remove(a)
    
    for b in lst1:
        n=1
        p[n]=b
        
        
        lst2=lst1.copy()
        lst2.remove(b)
        
        for c in lst2:
            n=2
            p[n] = c
            print(p)



