#Project Euler
#Question 01
total = 0
for i in range(1000) :
    test1 = i%3
    test2 = i%5
    if test1 == 0 or test2 == 0 :
        total = total + i
print(total)
    
    
