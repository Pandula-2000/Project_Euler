# Project Euler
# Problem 34


def fact(x) :
    if x == 0 :
        return 1
    return x*fact(x-1)

def factSum(y) :
    sum = 0
    for i in str(y) :
        sum += fact(int(i))
    return sum

sumList = []

for num in range(10,2540160) :
    if factSum(num) == num :
        sumList.append(num)
        print(num)
print(sum(sumList))

        
        
    
    
    
