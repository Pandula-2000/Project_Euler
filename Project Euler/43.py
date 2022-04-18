# Project Euler
# Question 43

import itertools

x = itertools.permutations("0123456789")

wonderfulNumbers = []

for i in x :
    num = ''.join(i)
    if num[0] == '0' :
        continue
    a = int(num[1:4])%2
    b = int(num[2:5])%3
    c = int(num[3:6])%5
    d = int(num[4:7])%7
    e = int(num[5:8])%11
    f = int(num[6:9])%13
    g = int(num[7:10])%17

    if a!=0 or b !=0 or c!=0 or d!=0 or e !=0 or f!=0 or g!= 0:
        continue
    wonderfulNumbers.append(int(num))
    print(num)
print(sum(wonderfulNumbers))
        
