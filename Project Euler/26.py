# Project Euler
# Problem 26


#kill=[]
recuryCy=[1]

for i in range(2,1000) :
    
    lst = [10]
    ans = list("0.")
    t = 2
    n = 10
    k = int(n/i)
    ans.append(str(k))
    rem = k*i
    n = (n-rem)*10
    while True :
        if n%i == 0 :
            recuryCy.append(1)
            break
        if n in lst :
            cycle = ans[lst.index(n)+2:t+1]
            recuryCy.append(len(cycle))
            break
        lst.append(n)
        k = int(n/i)
        ans.append(str(k))
        rem = k*i
        n = (n-rem)*10
        t+=1


p=max(recuryCy)

print(recuryCy)
print(p)
print(recuryCy.index(p)+1)


    
    

