# Project Euler
# Problem 35


import math

def isPrime(x) :
    if x < 2 :
        return False
    elif x == 2 :
        return True
    else:
        for i in range(2,int(math.sqrt(x))+1) :
            if x%i == 0 :
                return False
        return True

def isCircular(x,n) :
    if n == 0 :
        return True
    if isPrime(int(x)) == False :
        return False
    s=str(x)[1:] + str(x)[0]
    #print(s)
    return isCircular(s,n-1)  # This is Recursive!!!
    
#print(isCircular(101,3))
cirList = []
    
for num in range(1,1000000) :
    if isCircular(str(num),len(str(num))) :
        cirList.append(num)
        #print(num)
        
print(len(cirList))

















    
