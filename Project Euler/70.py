# Project Euler
# Problem 70


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

def isPer(x,y) :
    lx = list(int(i) for i in str(x))
    lx.sort()
    ly = list(int(j) for j in str(y))
    ly.sort()
    if lx == ly :
        return True
    return False

lst = []
for num in range(4000,2000,-1) :
    if isPrime(num) :
        lst.append(num)

lst1 = lst.copy()

ans = 0
ratio = 100


for i in lst :
    #print(i)
    lst1.remove(i)
    for j in lst1 :
        #print(j)
        n = i*j
        if n > 10000000 :
            continue
        phiF = int((i-1)*(j-1))
        if isPer(n,phiF) :
            if (n/phiF) < ratio :
                ratio = n/phiF
                ans = n

print(ans)
            
            
    

    
        
