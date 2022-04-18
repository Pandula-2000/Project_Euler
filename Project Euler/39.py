# Project Euler
# Problem 39


from statistics import mode

pyList = []
for c in range(1,1000) :
    for a in range(1,c-1) :
        k = 0
        for b in range(a+1,c) :
            if a + b + c > 1000 :
                k = 1
                break
            if (a**2 + b**2) == c**2 :
                pyList.append(a+b+c)
                print(c)
                #print(str(a)+' '+str(b)+'>>>'+str(c))
        if k == 1 :
            break
print(mode(pyList))            
    
            
            
        
        
    
        
    
