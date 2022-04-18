# Priject Euler
# Problem 97


#n = ((2**7830457)*28433) + 1
x = 2
for i in range(7830456) :
    x = (x*2)%10000000000
x = (x*28433)
x += 1
x = x%10000000000
print(x)
