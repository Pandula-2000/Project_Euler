# Project Euler
# Problem 61

import itertools

tri = []
for i in range(1,1000) :
    T = (i*(i+1))/2
    if T >= 10000 :
        break
    if T > 1000 :
        if str(T)[2:] != '00' and str(T)[2] != '0' :
            tri.append(int(T))

squ = []
for j in range(1,1000) :
    S = (j*j)
    if S >= 10000 :
        break
    if S > 1000 :
        if str(S)[2:] != '00' and str(S)[2] != '0' :
            squ.append(int(S))

pen = []
for k in range(1,1000) :
    P = (k*(3*k-1))/2
    if P >= 10000 :
        break
    if P > 1000 :
        if str(P)[2:] != '00' and str(P)[2] != '0' :
            pen.append(int(P))

hexa = []
for l in range(1,1000) :
    H = (l*(2*l-1))
    if H >= 10000 :
        break
    if H > 1000 :
        if str(H)[2:] != '00' and str(H)[2] != '0' :
            hexa.append(int(H))

hep = []
for m in range(1,1000) :
    HT = (m*(5*m-3))/2
    if HT >= 10000 :
        break
    if HT > 1000 :
        if str(HT)[2:] != '00' and str(HT)[2] != '0' :
            hep.append(int(HT))

octa = []
for n in range(1,1000) :
    O = (n*(3*n-2))
    if O >= 10000 :
        break
    if O > 1000 :
        if str(O)[2:] != '00' and str(O)[2] != '0' :
            octa.append(int(O))

def frontBack(x,y) :
    if  str(y)[:2] == str(x)[2:] :
        return True
    return False

def magic(x) :
    for a in x[0] :
        for b in x[1] :
            if frontBack(a,b) :
                for c in x[2] :
                    if frontBack(b,c) :
                        for d in x[3] :
                            if frontBack(c,d) :
                                for e in x[4] :
                                    if frontBack(d,e) :
                                        for f in x[5] :
                                            if frontBack(e,f) :
                                                if frontBack(f,a) :
                                                    print(a)
                                                    print(b)
                                                    print(c)
                                                    print(d)
                                                    print(e)
                                                    print(f)
                                                    print(a+b+c+d+e+f)
                                                    return True
                                                

for per in itertools.permutations([tri,squ,pen,hexa,hep,octa],6) :
    #print(list(per))
    x = magic(list(per))
    print(x)
    if x == True :
        break
                                                
                                                
                                                
                                       


















    
