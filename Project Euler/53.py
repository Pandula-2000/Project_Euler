# Project Euler
# Problem 53


def fact(x) :
    if x == 0 :
        return 1
    return x*fact(x-1)

def nCr(n,r) :
    #if n < r :
    #    return print('not Valid')
    return (fact(n))/(fact(r)*fact(n-r))

count = 0
for n in range(23,101) :
    for r in range(1,n) :
        if nCr(n,r) > 1000000 :
            count += 1
            
print(count)
