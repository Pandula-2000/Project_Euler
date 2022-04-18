# Project Euler
#Question 06

total1 = 0
total2 = 0

for i in range(1, 101) :  # for sum of squares.
    test1 = i**2
    total1 = total1 + test1

for j in range(1,101) :
    total2= total2 + j

sumOfSqures = total1
squreOfSums = total2**2

diff = squreOfSums - sumOfSqures
print(diff)

    
