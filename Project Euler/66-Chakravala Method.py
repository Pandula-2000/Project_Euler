# Project Euler
# Problem 66

from math import sqrt
def isSqure(x) :
    if int(sqrt(x))**2 == x :
        return True
    return False

#def genStartingCouple(N) : # b is set to 1
   # global a
    #global k

    

def solve(N) :
    print(N)
    global a
    global b
    global k
    a1 = int(sqrt(N)) + 1
    a2 = int(sqrt(N))
    if a1**2-N < N-a2**2 :
        a = a1
    else :
        a = a2
    b = 1
    k = a**2 - N
    print(a,b,k)
    if k == 1 :
         return print(a,1)
    while k != 1 :
        for m1 in range(int(sqrt(N)),0,-1) : # m is a positive integer
            if (a+b*m1)%abs(k) == 0 :
                break
        #print(m1)
        m2 = int(sqrt(N)) + 1
        while True :
            if (a+b*m2)%abs(k) == 0 :
                break
            m2 += 1
        if abs(m1**2-N) < abs(m2**2-N) :
            m = m1
        else :
            m = m2
        print(m)
        a1=a
        a = abs(((a*m)+(N*b))/k)
        b = abs((a1+(m*b))/k)
        k = (m**2-N)/k
        print(a,b,k)
        if k == 1 :
            print(a,b,k)
            break
        if k == -1 or k == -2 or k == 2 :
            y = a
            a = abs(((a**2)+N*(b**2))/k)
            b = abs((2*y*b)/k)
            k = 1
            print(a,b,k)
            break
        if k == 4 or k == -4 :
        
            if a%2 == 0 or b%2 == 0 :
                x = a
                a = abs(((a**2)+N*(b**2))/k)
                b = abs((2*x*b)/k)
                k = 1
                print(a,b,k)
                break
                






        
solve(277)    








        
        









    
