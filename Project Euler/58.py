# Project Euler
# Problem 58


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
    
digList = [1]
sideLen = 3
num = 1
x = 5
primes = []

while True :
    n = sideLen**2
    while num < n :
        num += (sideLen - 1)
        digList.append(num)
        if isPrime(num) :
            primes.append(num)
    ratio = (len(primes)/x)*100
    #print(ratio)
    #print(digList)
    #print(primes)
    if ratio < 10 :
        print(str(ratio) + '-' + str(sideLen))
        break
    sideLen += 2
    x += 4
    print(sideLen)
    
    
















    
   
