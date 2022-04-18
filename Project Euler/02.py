#Project Euler
#Question 02

fibSeq = [ 1 , 2 ]
Sum = 0

while fibSeq[-1] < 4000000 :
    nextTerm = int(fibSeq[-1] + fibSeq[-2])
    fibSeq.append(nextTerm)

for i in fibSeq :
    test = i%2
    if test == 0 :
        Sum = Sum + i
print(Sum)
        
