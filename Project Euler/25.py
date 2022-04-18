# Project Euler
# Problem 25

febSeq = [1,1]

while len(str(febSeq[-1])) < 1000 :
    febSeq.append(febSeq[-1]+febSeq[-2])

print(febSeq.index(febSeq[-1]))
   

