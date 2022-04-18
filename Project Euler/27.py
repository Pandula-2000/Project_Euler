# Project Euler
# Problem 27

import math

def isPrime(x) :
    if x < 2 :
        return False
    for i in range(2,int(math.sqrt(x))+1) :
        if x%i == 0 :
            return False
    return True
listA = []
listB = []
nums = [0]
primeList = []

for i in range(0,1001) :
    if isPrime(i) == True :
        primeList.append(i)


for b in primeList :
    for a in range(-1000,1001) :
        n = 1
        k = n**2+a*n+b
        while isPrime(k) == True :
            n += 1
            k = n**2+a*n+b
        if nums[-1] < (n+1) :
            nums.append(n+1)
            listA.append(a)
            listB.append(b)
            
#print(listA)
#print(listB)
            
print(listA[-1] * listB[-1])            
        
        
                   
    
