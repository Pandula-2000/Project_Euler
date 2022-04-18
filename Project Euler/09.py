# Project Euler
# Question 09


for a in range(1, 1001) :
    for b in range(1, 1001) :     #first we choosea abd b to test
        c = 1000 - a - b          #finding c 
        if a**2 + b**2 != c**2 :  #test fails so skip that b, test the next b
            continue              
        elif a**2 + b**2 == c**2 :#if we found a match,break from for loop for c
            break
    if a**2 + b**2 == c**2 :      #break out of main loop if we get a match
        break

print('a will be ' + str(a))
print('b will be ' + str(b))
print('c will be ' + str(c))
