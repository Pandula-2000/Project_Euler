# Project Euler
# Problem 07

import math
primeList = [2,3]
num = 4

while len(primeList) <= 10000 :
    test = 0
    for i in range(2, int(math.sqrt(num))+) :
        if num % i == 0 :
            test = 1
            break

    if test == 0 :
         primeList.append(num)
         #print(len(primeList))
         print(num)

    num = num + 1
   
print(primeList[-1])
    


