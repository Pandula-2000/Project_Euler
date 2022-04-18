# Project Euler
# Problem 47


import math

def isPrime(x) :
    if x < 2 :
        return False
    if x == 2 :
         return True
    for i in range(2,int(math.sqrt(x))+1) :
        if x%i == 0 :
            return False
    return True

def getFacts(x) :
    facts = []
    for i in range(2,int(math.sqrt(x))+1) :
        if x%i == 0 :
            n = x/i
            if isPrime(n) == True and n not in facts :
                facts.append(int(n))
            if isPrime(i) and i not in facts :
                facts.append(int(i))
    return facts

v=getFacts(10)
#print(v)
#print(len(v))

n = 10          
while True :
    a = getFacts(n)
    b = getFacts(n+1)
    c = getFacts(n+2)
    d = getFacts(n+3)
    if len(a)==len(b)==len(c)==len(d) == 4 :
        print(n)
        break

    n += 1
        
        
        
        
















    
    
    
