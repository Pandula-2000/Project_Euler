# Project Euler
# Problem 63


def pow(x,y) :   # x<10
    if len(str(x**y)) == y :
        return True
    return False

n = 1
lst = []
while True :
    m = 0
    for i in range(1,10) :
        if pow(i,n) :
            m += 1
    #print(m)
    lst.append(m)
    if m == 0 :
        #print(n)
        break
    n += 1
        
    
print(sum(lst))
