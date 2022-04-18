# Project Euler
# Problem 10

prime = [2,3] #starting with 2 and 3
import math

for i in range(4,2000001) :
    k = 0
    for j in range(2,int(math.sqrt(i))+1) :
        if i%j == 0 :
            k = 1
            break
    if k == 0 :
        prime.append(i)
        #print(i)
        
print(sum(prime))
