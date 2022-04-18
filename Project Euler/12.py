# Project Euler
# Problem 12


import math
def function1(n) :
    fac=[]
    for i in range(1,round(math.sqrt(n))+1) :
        if n%i == 0 :
            fac.append(i)
            fac.append(n/i)
    return len(fac)

triList=[1,3]
numList=[1,2]

while function1(triList[-1]) <= 500 :
    numList.append(numList[-1] + 1)
    triList.append(sum(numList))
    
    
print(triList[-1])
    
    
    
    
         
    
    

        
