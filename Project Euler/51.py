# Project Euler
# Problem 51

import sys
import math
import itertools

def insert(x,n) : # Will insert '*' to a given position
    return x[:n-1] + '*' + x[n-1:]


def isPrime(x) :
    if x < 2 :
        return False
    if x == 2 :
        return True
    for i in range(2,int(math.sqrt(x))+1) :
        if x%i == 0 :
            return False
    return True


def rep(x):
    w = []
    for j in range(10):
        n = x.replace('*',str(j))
        if isPrime(int(n)) :
            w.append(n)
    return len(w)


lst = []
n = 1
while n < 6 :
    for rep in itertools.combinations([1,2,3,4,5,6],n) :
        #input(':::')
        for k in itertools.combinations_with_replacement([0,1,2,3,4,5,6,7,8,9],6-n) :
            #print(k)
            for per in itertools.permutations(list(k)) :
                strPer = ''.join(map(str,per))
                for i in list(rep) :
                    strPer = insert(strPer,i)
                if strPer[0] == '0' or strPer[-1] == '0' or strPer[-1] == '2' or strPer[-1] == '4' or strPer[-1] == '5' or strPer[-1] == '6' or strPer[-1] == '8' :
                    continue
                lstt = []
                for j in range(10):
                    m = strPer.replace('*',str(j))
                    if isPrime(int(m)) and m[0] != '0':
                        lstt.append(m)
                if len(lstt) == 8 :
                    print(strPer)
                    input()
                    sys.exit()
                
    n += 1
       
                    
                
                
                
        
        
        
        
        
        
