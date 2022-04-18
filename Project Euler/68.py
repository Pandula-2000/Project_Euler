# Project Euler
# Problem 68


from itertools import permutations,combinations

solList = []
nums = [1,2,3,4,5,6,7,8,9,10]

for i in combinations(nums,3) :
    for j in permutations(list(i),3) :
        abc = list(j)
        a,b,c = abc[0],abc[1],abc[2]
        lstD = nums.copy()
        lstD.remove(a)
        lstD.remove(b)
        lstD.remove(c)
        for d in lstD :
            lstF = lstD.copy()
            lstF.remove(d)
            e = (a+b)-d
            if (e not in lstF) :
                continue
            lstF.remove(e)
            for f in lstF :
                lstH = lstF.copy()
                lstH.remove(f)
                g = (c+d)-f
                if (g not in lstH) :
                    continue
                lstH.remove(g)
                for h in lstH :
                    lst =lstH.copy()
                    lst.remove(h)
                    i = (e+f)-h
                    if (i not in lst) :
                        continue
                    lst.remove(i)
                    j = (a+c)-i
                    if (j not in lst) :
                        continue
                    solA =str(a)+str(b)+str(c)+str(d)+str(c)+str(e)+str(f)+str(e)+str(g)+str(h)+str(g)+str(i)+str(j)+str(i)+str(b)
                    if len(solA) != 16 :
                        continue
                    sol = [[a,b,c],[d,c,e],[f,e,g],[h,g,i],[j,i,b]]
                    minTri = [10]
                    for tri in sol :
                        if tri[0] < minTri[0] :
                            minTri = tri
                    solution = sol[sol.index(minTri):] + sol[:sol.index(minTri)]
                    #print(solA)
                    #print(minTri)
                    #print(solution)
                    strSol = ''
                    for triple in solution :
                        strTriple = list(map(str,triple))
                        strSol += ''.join(strTriple)
                    #print(strSol)
                    solList.append(int(strSol))
                    
print(max(solList))                        
                 
                    
                        
                     









                
                
                

            

        
