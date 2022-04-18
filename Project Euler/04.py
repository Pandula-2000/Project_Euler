#Project Euler
#Question 04

theList = []

for i in range(100,1000) :
    for j in range (100, 1000) :
        num = str(i * j)
        
        if num == num[::-1] :
            theList.append(int(num))
print(max(theList))


            
        
