# Project Euler
# Problem 60

import math
def isPrime(x) :
    if x<2 :
        return False
    if x==2 :
        return True
    for i in range(2,int(math.sqrt(x))+1) :
        if x%i == 0 :
            return False
    return True

def isPrimeCon(x,y) :
    if isPrime(int(str(x)+str(y))) :
        if isPrime(int(str(y)+str(x))) :
            return True
    return False

primes = []
for i in range(10000) :
    if isPrime(i) :
        primes.append(i)

lst = []
def f() :
    for i in primes[:7] :
        print(i) 
        for j in primes[primes.index(i)+1:] :
            if isPrimeCon(i,j) :
          
                for k in primes[primes.index(j)+1:] :
             
                    if isPrimeCon(i,k) and isPrimeCon(j,k) :
                 
                        for l in primes[primes.index(k)+1:] :
                            
                            if isPrimeCon(i,l) and isPrimeCon(j,l) and isPrimeCon(k,l) :
                            
                                for m in primes[primes.index(l)+1:] :
                               
                                    if isPrimeCon(i,m) and isPrimeCon(j,m) and isPrimeCon(k,m) and isPrimeCon(l,m) :
                                        return (i+j+k+l+m)
                                    














                
        
        
        






    
