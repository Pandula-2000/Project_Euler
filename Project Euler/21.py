# Project Euler
# Problem 21

#lets find the sum of proper divisors of a number n,
import math
def sumProperDivisors(n) :
    propDiv = [1]
    for num in range(2,round(math.sqrt(n))+1) :
        if n % num == 0 :
            test = n/num
            propDiv.append(num)
            propDiv.append(test)
    return sum(propDiv)

amicableList = []
for i in range(4,10001) : #1,2,3 are not considered because they are not amicable numbers(no proper divisors for 1)
    if i in amicableList :
        continue
    b = sumProperDivisors(i)
    if sumProperDivisors(b) == i :
        if i == b :
            continue
        else :
            amicableList.append(i)
            amicableList.append(b)
print(sum(amicableList))
print(amicableList)
#print(sumProperDivisors(284))
