# Project Euler
# problem 45

import math

def isPent(x) :
    if (1+math.sqrt(1+(24*x)))%6 ==0 :
        return True
    return False


def isHex(x) :
    if (1+math.sqrt(1+(8*x)))%4 == 0 :
        return True
    return False

#print(isHex(46))

p = 286

while True :
    tri = (p*(p+1))/2
    if isPent(tri) and isHex(tri) :
        print(tri)
        break
        #print(p)
    p += 1
    
    
    













