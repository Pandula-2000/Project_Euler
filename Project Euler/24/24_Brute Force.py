# Project Euler
# Problem 24

poss=[1,1,1,1,1,1,1,1,1,1]
per = []

lst = list(range(10))

for a in lst:
    n = 0
    poss[n] = a
    lst1 = lst.copy()
    lst1.remove(a)
    
    for b in lst1 :
        n = 1
        poss[n] = b
        lst2 = lst1.copy()
        lst2.remove(b)
        for c in lst2 :
            n = 2
            poss[n] = c
            lst3 = lst2.copy()
            lst3.remove(c)
            for d in lst3 :
                n =3
                poss[n] = d
                lst4 = lst3.copy()
                lst4.remove(d)
                for e in lst4 :
                    n = 4
                    poss[n] = e
                    lst5 = lst4.copy()
                    lst5.remove(e)
                    for f in lst5 :
                        n = 5
                        poss[n] = f
                        lst6 = lst5.copy()
                        lst6.remove(f)
                        for g in lst6 :
                            n =6
                            poss[n] = g
                            lst7 = lst6.copy()
                            lst7.remove(g)
                            for h in lst7 :
                                n = 7
                                poss[n] = h
                                lst8 = lst7.copy()
                                lst8.remove(h)
                                for i in lst8 :
                                    n = 8
                                    poss[n] = i
                                    lst9 = lst8.copy()
                                    lst9.remove(i)
                                    for j in lst9 :
                                        n = 9
                                        poss[n] = j
                                        print(poss)
                                        per.append(poss)
                                        #print(len(per))
            
print(per[999999])          
            
    
    
    
        
