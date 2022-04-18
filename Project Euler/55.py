# Project Euler
# Problem 55


def rev(x) :
    # x will be given in integer
    return int(str(x)[::-1])
    
def isLychrel(x,n) :
    if n > 0 :
        if x == rev(x) :
            return False
    if n == 50 :
        return True
    n += 1
    return isLychrel((x+rev(x)),n)

#print(isLychrel(4994,0))

lyNumbers = []
for num in range(1,10001) :
    if isLychrel(num,0) :
        lyNumbers.append(num)

print(lyNumbers)
print(len(lyNumbers))
    
