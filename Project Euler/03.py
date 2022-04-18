#Project Euler
#Question 03

n = 600851475143
i = 2

while n != i :
    while n%i == 0 :
        n = n / i
    i = i +1

print(n)
print(i)

        
    
