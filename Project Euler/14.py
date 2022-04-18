# Project Euler
# Problem 14

def collatzSeq(n) :
    seq = [n]
    while seq[-1] != 1 :
        x = seq[-1]
        if x%2 == 0 :
            seq.append(x/2)
        else :
            seq.append((3*x) + 1)
    return len(seq)

    
currentLargestNum = 0
currentLargestSeqLen = 0
for i in range(2, 1000000) :  # skipping 1
    x=collatzSeq(i)
    if x > currentLargestSeqLen :
        currentLargestSeqLen = x
        currentLargestNum = i
print(currentLargestNum)

    

    
