# Project Euler
# Problem 64

import math
def contFrac(x,y,z) :
    global lst
    if z == 2 :
        if str(x)[:4] == str(y)[:4] :
            return lst
    lst.append(int(x))
    m = (1/(x-int(x)))
    #print(m)
    return contFrac(m,y,2)

def isSqure(x) :
    if int(math.sqrt(x))**2 == x :
        return True
    return False
    

count = 0
for i in range(2,10001) :
    lst = []
    if isSqure(i) :
        continue
    print(i)
    n = (1/(math.sqrt(i)-int(math.sqrt(i))))
    #print(n)
    a = contFrac(n,n,1)
    print(a)
    if len(a)%2 == 1 :
        count += 1
        
    
print(count)

    
