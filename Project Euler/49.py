# Project Euler
# Problem 49


import math
import itertools


def isPrime(x) :
    if x<2 :
        return False
    if x == 2 :
        return True
    for i in range(2,int(math.sqrt(x))+1) :
        if x%i == 0 :
            return False
    return True

comb = itertools.combinations_with_replacement([1,2,3,4,5,6,7,8,9],4)

for i in comb :
    #print(i)
    perList = []
    if sum(list(i))%3 == 0 :
        continue
    for j in itertools.permutations(list(i)) :
        per = int(''.join(map(str,(list(j)))))
        #print(per)
        if per < 9999 and isPrime(per) and per not in perList :
            perList.append(per)
    #print(perList)
    if len(perList) < 3 :
        continue
    for num in perList :
        #perlist2 = perList.copy().remove(num)
        p = perList[perList.index(num)+1:]
        if len(p) < 2 :
            continue
        for no in p[::-1] :
            if (no+num)/2 in perList :
                print(no)
                print((no+num)/2)
                print(num)
                print("      Finding other one....")
            if no == p[0] :
                continue
            
print("   *******Thats all I found*******")


                
    
        
        
        






        
        
        

