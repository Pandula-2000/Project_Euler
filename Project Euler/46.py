# Project Euler
# problem 46



import math
def isPrime(x) :
    if x < 2 :
        return False
    if x == 2 :
        return True
    for i in range(2,int(math.sqrt(x)) + 1) :
        if x%i == 0 :
            return False
    return True
    

def isSqure(x) :
    root = x**(0.5)
    if root == (x/round(root)) :
        return True
    return False

primes = [1,2,3,5]


def primeRange(n) :
    global primes
    k = primes[-1]
    while k < n :
        k += 1
        if k >= n :
                break
        if isPrime(k) :
            primes.append(k)


def doesAgree(n) :
    for p in primes[::-1] :
        if p == 1 :
            return False
        squ = (n-p)/2
        if isSqure(squ) :
            return True
        
n = 9
                             
while True :
    if isPrime(n) :
        n += 2
        continue
    primeRange(n)
    if doesAgree(n) == False :
        print(n)
        break
    n += 2
        
        
        
    



