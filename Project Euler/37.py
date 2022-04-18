# Project Euler
# Problem 37

import math
def isPrime(x) :
    if x<2 :
        return False
    if x == 2 :
        return True
    for i in range(2,int(math.sqrt(x))+1) :
        if x%i == 0 :
            return False
    return True




n = 0
a = 10
lst = []
while n<11 :
    a += 1
    x = str(a)
    y = str(a)[::-1]
    k = 1
    for i in range(0,len(x)) :
        if isPrime(int(x[i:])) == False :
            k = 0
            break
        if isPrime(int(y[i::][::-1])) == False :
            k = 0
            break
    if k == 1 :
        lst.append(a)
        print(a)
        n += 1
        
    
    
    
    
