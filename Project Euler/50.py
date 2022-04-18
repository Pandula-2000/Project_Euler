# Project Euler
# Problem 50


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

def primeRange(x) :
    for i in range(1,x+1) :
        if isPrime(i) :
            yield (i)
primes = list(primeRange(20000))

# Because under 10000 we get 65 primes and
# 65*20000 =1300000 which is > 1000000
# so the list cannot come up to 20000
# so that it is enough to check untill 20000
# matbe perhaps thats too much too. But we do that anyway...



n = 2
while True :
    #print(n)
    x = 0
    for i in range(n) :
        lst = primes[i:len(primes)-n+2+i]
        if sum(lst) < 1000000 and isPrime(sum(lst))  :
            #print("No. of consecative Primes :")
            #print(len(lst))
            #print("Starter :")
            #print(lst[0])
            #print("That prime is :")
            print(sum(lst))
            x = 1
            break
    if x == 1 :
        break
    n += 1

        
    



























        
