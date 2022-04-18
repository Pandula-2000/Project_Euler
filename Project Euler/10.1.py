# Project Euler
# Problem 10


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

sum = 0
for i in range(2,2000000) :
    if isPrime(i) == True :
        #print(i)
        sum += i

print(sum)
