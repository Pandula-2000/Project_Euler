# Project Euler
# Problem 54


def isSameSuit(x) :
    if x[0][-1]==x[1][-1]==x[2][-1]==x[3][-1]==x[4][-1] :
        return True
    return False

def isCon(x) :
    if int(x[0][:-1])+4== int(x[1][:-1])+3==int(x[2][:-1])+2==int(x[3][:-1])+1==int(x[4][:-1]) :
        return True
    return False
    
def isSameValue(x,y) : # x-list,y-no. of same values
    lst = []
    for i in x :
        lst.append(i[:-1])
    for j in lst :
        if lst.count(j) == y :
            return True
    return False

def maxCard(x) :
    lst = []
    for i in x:
        lst.append(int(i[:-1]))
    return max(lst)

def repeatedMax(x,y) :
    lst = []
    for i in x :
        lst.append(i[:-1])
    for j in lst :
        if lst.count(j) == y :
            return int(j)
    
def maxRest(x,y):
    lst = []
    for i in x :
        lst.append(int(i[:-1]))
    n = lst.copy()
    for j in lst :
        if n.count(j) == y :
            lst.remove(j)
    return max(lst)
            
def isDoubleDuo(x) :
    duo = []
    for i in x :
        duo.append(i[:-1])
    for j in duo :
        if duo.count(j) == 2 :
            duo.remove(j)
            duo.remove(j)
            break
    for k in duo :
        if duo.count(k) == 2 :
            return True
    return False

def maxDuo(x):
    maxx = []
    duo = []
    for i in x :
        duo.append(int(i[:-1]))
    for j in duo :
        if duo.count(j) == 2 :
            maxx.append(j)
            duo.remove(j)
            duo.remove(j)
            break
    for k in duo :
        if duo.count(k) == 2 :
            maxx.append(k)
            duo.remove(k)
            duo.remove(k)
    maxx.sort()
    yield maxx[-1]
    yield maxx[0]
    yield duo[0]
    

def marks(x) :
    markList = []
    if isCon(x) :
        conRank =int(x[-1][:-1])
        if isSameSuit(x) :
            markList.append(1)
            markList.append(conRank) # Royal Flush and Straight Flush done.
        else : # Straight here.
            markList.append(5)
            markList.append(conRank)
    elif isSameSuit(x) : # Flush done.
        markList.append(4)
        markList.append(maxCard(x))
    elif isSameValue(x,4) : # Four of a kind done.
        markList.append(2)
        markList.append(repeatedMax(x,4))
        markList.append(maxRest(x,4))
    elif isSameValue(x,2) and isSameValue(x,3) :
        markList.append(3)
        markList.append(repeatedMax(x,3))
        markList.append(repeatedMax(x,2)) # Full House done.
    elif isSameValue(x,3) :
        markList.append(6)
        markList.append(repeatedMax(x,3))
        markList.append(maxRest(x,3)) # 3 of a kind done.
    elif isSameValue(x,2) :
        if isDoubleDuo(x) :
            markList.append(7)
            for i in maxDuo(x) :
                markList.append(i) # Two pairs done.
        else :
            markList.append(8)
            markList.append(repeatedMax(x,2))
            markList.append(maxRest(x,2)) # One pair done
    else :
        markList.append(9)
        markList.append(maxRest(x,5)) # High card done finally.
    return markList
            
f = open('p054_poker.txt','r')
k = f.read()
a = k.replace('A','14')
f = open('p054_poker.txt','w')
f.write(a)

f = open('p054_poker.txt','r')
k = f.read()
a = k.replace('K','13')
f = open('p054_poker.txt','w')
f.write(a)

f = open('p054_poker.txt','r')
k = f.read()
a = k.replace('Q','12')
f = open('p054_poker.txt','w')
f.write(a)

f = open('p054_poker.txt','r')
k = f.read()
a = k.replace('J','11')
f = open('p054_poker.txt','w')
f.write(a)

f = open('p054_poker.txt','r')
k = f.read()
a = k.replace('T','10')
f = open('p054_poker.txt','w')
f.write(a)


f = open('p054_poker.txt','r')

k = f.readlines()

sum1 = 0
sum2 = 0

for i in k[0:]:
    #print(i)
    allCards = i[:-1].split(' ')
    x = allCards[0:5]
    y = allCards[5:]
    x.sort()
    y.sort()
    for j in x :
        if len(j) == 2 :
            n = x.index(j)
            #print(n)
            break
    player1 = x[n:]+x[0:n]
    for k in y :
        if len(k) == 2 :
            m = y.index(k)
            break
    player2 = y[m:]+y[0:m]
    print(player1)
    print(marks(player1))
    print(player2)
    print(marks(player2))
    ms1 = marks(player1)
    ms2 = marks(player2)
    if ms1[0] < ms2[0] :
        sum1 += 1
    elif ms1[0] == ms2[0] :
        if ms1[1] > ms2[1] :
            sum1 += 1
        elif ms1[1] == ms2[1] :
            if ms1[2] > ms2[2] :
                sum1 += 1
            elif ms1[2] == ms2[2] :
                if ms1[3] > ms2[3] :
                    sum1 += 1
            
        
    
print(sum1)  

#print(marks(['5H','5c','5s','14s','14D']))
    
f.close()
###### This code actually works!!! 

