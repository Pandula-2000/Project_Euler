# Project Euler
# Problem 28


import math
n=1
diagonalList = []
k=0


while n<=(1001*1001) : 
    diagonalList.append(n)
    if math.sqrt(n)%2 == 1 : 
        #print(n)
        k+=2
    n+=k
    
print(sum(diagonalList))




#A side lenth of a small spiral always gives an odd number. So its easy to code... 
