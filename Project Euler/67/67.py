# Project Euler
# Problem 67

f = open('p067_triangle.txt','r')
k = f.readlines()

triList = []
for i in k :
    line = i[:-1].split(' ')
    triList.append(list(map(int,line)))
    
#print(triList[:5])

for line in triList[-2::-1] :
    n = 0
    #print(line)
    for num in line :
        #print(num)
        line[n] = num + max(triList[-1][n],triList[-1][n+1])
        n += 1
    del(triList[-1])

print(triList)
                                          
    
