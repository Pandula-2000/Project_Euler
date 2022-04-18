# Project Euler
# Problem 24


def fact(n):
    
    if n==1 or n ==0 :
        return 1
    ans = n*fact(n-1)
    return ans

num = list(range(10))
no = 1000000
lex = []

for i in range(10):
    if no == 2 :
        lex.append(num[-1])
        lex.append(num[0])
    if no == 1 :
        lex.append(num[0])
        lex.append(num[-1])
    n = int(no/(fact(9-i)))
    if no%(fact(9-i)) == 0 :
        lex.append(num[n-1])
        del num[n-1]
        no = no - (fact(9-i))*n
    else :
        lex.append(num[n])
        del num[n]
        no = no - (fact(9-i))*n
    
print(lex)
