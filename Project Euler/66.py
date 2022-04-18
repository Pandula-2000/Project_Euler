# Project Euler
# Problem 66

import math
def isSqure(x) :
    if x == int(math.sqrt(x))**2 :
        return True
    return False
#print(isSqure(4))

DList = []
for D in range(61,62) :
    #print(D)
    if isSqure(D) :
        continue
    k = 0
    X = int(math.sqrt(D)) + 1
    Y = 1
    while True :
        #print('D is' + str(D))
        
        while X**2 > (D*(Y**2)) :
            #print(str(X)+'  ' + str(Y))
            #print(Y)
            if (X**2) - (D*(Y**2)) == 1 :
                DList.append(X)
                print(X)
                k = 1
                Y = 1
                break
            Y += 1
        if k == 1 :
            break
        X += 1
        Y = 1
        
        
        
        
    
