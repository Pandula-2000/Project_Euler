# Project Euler
# Problem 38

conList = []
for num in range(1,10000) :
    c = 'run'
    n = 1
    con = []
    while len(con) < 9 :
        pro = str(num * n)
        for i in pro :
            if con.count(i) != 0 or i == '0' :
                c = 'kill'
                break   
            con.append(i)
        if c == 'kill' :
            break
        n += 1
    if  len(con) == 9 :
        k = ''.join(con)
        conList.append(int(k))
        print(k)
            
print(max(conList))           
                
        
        
