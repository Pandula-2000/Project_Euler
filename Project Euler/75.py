# Project Euler
# Problem 75


import math

lst=[]
for n in range(1,867) :
    print(n)
    for m in range(n+1,867) :
        #print(m)
        if math.gcd(m,n)==1 and(m+n)%2 == 1 :
            a = m**2 - n**2
            b =2*m*n
            c = m**2 + n**2
            l = a+b+c
            if l > 1500000 :
                continue
            lst.append([a,b,c])
            #for L in range(l,1500000,1) :
                #if L not in lst :
                #lst.append(L)

            
lList = []
for i in lst :
    a,b,c = i[0],i[1],i[2]
    n = 1
    while (n*a+n*b+n*c) < 1500000 :
        l = (n*a+n*b+n*c)
        lList.append(l)
        n = n+1
p = []

for L in lList :
    if lList.count(p) == 1 :
        p.append(L)


    




        
