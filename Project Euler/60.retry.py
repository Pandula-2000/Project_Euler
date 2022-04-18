# Project Euler
# Problem 60


from math import sqrt
def isPrime(x) :
    if x < 2 :
        return False
    if x == 2 :
        return True
    for i in range(2,int(sqrt(x))+1) :
        if x%i == 0 :
            return False
    return True

def isConPrime(x,y) :
    if isPrime(int(str(x)+str(y))) :
        if isPrime(int(str(y)+str(x))) :
            return True
        return False
    return False
        
        

primes = []
for i in range(3,10000) :
    if isPrime(i) :
        primes.append(i)
    
import sys        
for a in primes :
    primes1 = primes[primes.index(a)+1:]
    for b in primes1 :
        if isConPrime(a,b) :
            primes2 = primes[primes.index(b)+1:]
            for c in primes2 :
                if isConPrime(a,c) and isConPrime(b,c) :
                    primes3 = primes[primes.index(c)+1:]
                    for d in primes3 :
                        if isConPrime(a,d) and isConPrime(b,d) and isConPrime(c,d) :
                            primes4 = primes[primes.index(d)+1:]
                            for e in primes4 :
                                if isConPrime(a,e) and isConPrime(b,e) and isConPrime(c,e) and isConPrime(d,e) :
                                    print(a,b,c,d,e)
                                    print(a+b+c+d+e)
                                    input('press enter to EXIT')
                                    sys.exit()
                                          
                                    
                        











        
