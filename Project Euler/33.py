# Project Euler
# Problem 33



import math

def isPrime(x) :   # This will decide if a number is prime or not
    if x < 2 :
        return False
    if x == 2 :
        return True
    for i in range(2,int(math.sqrt(x))+1) :
        if x%i == 0:
            return False
    return True

def prime(x) :     # This will find the x th prime num.
    n = 0
    t = 1
    while n < x :
        if isPrime(t) == True :
            n += 1
        t += 1
    return (t-1)

def fact(x) :   # This one will give out all prime factors
    fact = []   # of a number(x)
    n = 1
    while (isPrime(x)) == False and x != 1 :
        while x%prime(n) == 0 and x != 1:
            x = x/prime(n)
            fact.append(prime(n))
        n += 1
    if isPrime(x) :
        fact.append(x)
        return fact

# ***************Here Starts our Code************************            

lst = []

for i in range(10,100) :
    for j in range(i+1,100) :
        n = i/j
        for num in str(i) :
            if num in str(j) and num != '0' :
                ii = int(str(i)[1-str(i).index(num)])
                jj = int(str(j)[1-str(j).index(num)])
                if jj != 0 :
                    m = ii/jj
                    if m == n :
                        lst.append([i,j])
                
                
print(lst)
#*********************End of it****************************

# You can do the rest by hand. but i was too lazy
# So here we go,,,,
# Using the Def s we did at the very beginning,

deno = 1
nume = 1

for f in lst :
    deno = deno*f[1]
    nume = nume*f[0]

lst1 = fact(nume)
lst2 = fact(deno)   # Get numerator and denominator

for factor in lst1 :
    if factor in lst2 :
        lst2.remove(factor) # Removing same factors from denominator
        
product = 1
for fac in lst2 :
    product = product*fac  # Multipy the elements in denominator list and,,,
    
print(product)#<<<<<<FInally!
    


















  
        

















        
        



















            
        
        
        
    























        
