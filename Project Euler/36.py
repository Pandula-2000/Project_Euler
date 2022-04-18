# Project Euler
# Problem 36


def rev(x) :
    return x[::-1]
    

#print(rev('1234'))

bList = []

for num in range(1,1000000) :
    if str(num) == rev(str(num)) :
        binary = bin(num)[2:]
        if binary[0] == '0' or binary[-1] == '0' :
            continue
        if binary == rev(binary) :
            bList.append(num)
            print(num)
            
print(len(bList))
            
print(sum(bList))        
    
