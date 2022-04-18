# Project Euler
# Problem 48


tot = 0
for i in range(1,1001) :
    tot = tot + i**i

print(str(tot)[-10:])
