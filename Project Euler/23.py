# Project Euler
# Problem 23


import math
n = 28123
abundantNum = []
lst =list(range(n+1))
for num in range(12,n+1) :
    properDivi = [1]
    for i in range(2,round(math.sqrt(num))+1) :
        if i not in properDivi :  
            if num%i == 0 :
                properDivi.append(i)
                if math.sqrt(num) == i :
                    continue
                properDivi.append(int(num/i))
    if sum(properDivi) > num :
        abundantNum.append(num)
        
print(abundantNum)

#for no in range(1,n+1) :
#    k = 1
#    for j in abundantNum :
#        if (no-j) in abundantNum :
#            k = 0
#            break
#    if k == 1 :
#        lst.append(no)
#        print(no)

for n1 in abundantNum :
    print(n1)
    
    x=0
    for n2 in abundantNum[x:] :
        no = n1 + n2
        if no  in lst :
            lst.remove(no)
    x=x+1
    
print(sum(lst))

        
    










    
    
            
    
