# project Euler
# Problem 57


def dev(x,y) :
    yield (x+y)
    yield (y)
lst = []
a = 3
b = 2
for i in range(1000) :
    n = 1
    for i in dev(a,b) :
        if n == 1 :
            c = i
        if n == 2 :
            d = i
        n += 1
    m = 1
    for j in dev(d,c) :
        if m == 1 :
            a = j
        if m == 2 :
            b = j
        m += 1
    if len(str(a)) > len(str(b)) :
        lst.append(a)
        
print(len(lst))    
         
    
