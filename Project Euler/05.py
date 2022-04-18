# Project Euler
# Question 05

def smallestDivisible1to20(number) :
    for i in range(11,21) :
        if number % i != 0 :
            return False
    return True

number = 1
while True:
    if smallestDivisible1to20(number) == True :
        break
    number = number + 1
    print(number)
    
    
print(number)
