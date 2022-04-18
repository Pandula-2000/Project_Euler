# Project Euler
# Problem 41


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
    
lastList = [1,3,7]
numList = list(range(1,8))
possList =[]


for a in lastList :
    poss1 = (str(a))
    lst1 = numList.copy()
    lst1.remove(a)
    for b in lst1 :
        poss2 = (str(b) + poss1)
        lst2 = lst1.copy()
        lst2.remove(b)
        for c in lst2 :
            poss3 = (str(c) + poss2)
            lst3 = lst2.copy()
            lst3.remove(c)
            for d in lst3 :
                poss4 = (str(d) + poss3)
                lst4 = lst3.copy()
                lst4.remove(d)
                for e in lst4 :
                    poss5 = (str(e) + poss4)
                    lst5 = lst4.copy()
                    lst5.remove(e)
                    for f in lst5 :
                        poss6 = (str(f) + poss5)
                        lst6 = lst5.copy()
                        lst6.remove(f)
                        for g in lst6 :
                            poss7 = (str(g) + poss6)
                            if isPrime(int(poss7)) == True :
                                possList.append(int(poss7))
                                
                            

#print(len(possList))
print(possList)
print(max(possList))


                    


