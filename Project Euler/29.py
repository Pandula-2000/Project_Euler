# Project Euler
# Problem 29

termList = []

for a in range(2,101) :
    for b in range(2,101) :
        x = a**b
        if x not in termList :
            termList.append(x)
            
print(len(termList))           
