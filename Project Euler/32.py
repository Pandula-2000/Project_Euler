# Project Euler
# Problem 32


sumList = []
tester = []
lst = []
for num in range(2,4990) :
    k=0
    for i in str(num) :
        if i == '0' :
            k=1
            break
        if str(num).count(i)>1 :
            k=1
            break
    if k ==0:
        
        lst.append(num)

for j in lst :
    for n in lst :
        m = j*n
        three = str(j)+str(n)+str(m)
        q = 0
        if len(three) != 9 :
            continue
        for p in three :
            if p == '0' :
                q=1
                break
            if three.count(p) > 1 :
                q = 1
                break
        if q == 0 :
            sumList.append(m)

lst1=[]
for a in sumList:
    if a not in lst1:
        lst1.append(a)

print(sum(lst1))        
        
           
        
        




















    
