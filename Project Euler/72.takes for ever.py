# Project Euler
# Problem 72


import math
def isPrime(x) :
    if x<2 :
        return False
    if x==2 :
        return True
    if x%2 == 0 :
        return False
    for i in range(3,int(math.sqrt(x))+1,2) :
        if x%i == 0 :
            return False
    return True

def getPF(x) :
    lst = []
    n=2
    while x != 1 :
        while x%n == 0 :
            x=x/n
            if n not in lst :
                lst.append(n)
        n+=1
    return lst
    
#print(getPF(127430))


def phi(n) :
    ans = n
    for i in getPF(n) :
        ans = ans*(1-(1/i))
    return ans

primes=[]
for i in range(1000000) :
    if isPrime(i) :
        primes.append(i)


    





















