# Project Euler
# Problem 30

numList = []

for num in range(2,354295) : 
    k = 0
    for i in str(num) :
        k += int(i)**5
    if k == num :
        print(num)
        numList.append(num)
print(sum(numList))


# The largest number that can be written as fifth powers of
# its digits if 354295(six times of 9**5).no number greater than this
# can be written as fifth powers of its digits
