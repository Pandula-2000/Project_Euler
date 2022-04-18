# Project Euler
# Problem 52


import itertools

start = 100001
end = 166667
n = 1
while True :
    n = n*10
    for num in range(start,end) :
        #print(num)
        if num == 150000 :
            print('oh no!')
            break
        number = list(map(int,list(str(num))))
        perTups = [int(''.join(list(map(str,i)))) for i in list(itertools.permutations(number))]
        if num*2 in perTups :
            if num*3 in perTups :
                if num*4 in perTups :
                    if num*5 in perTups :
                        if num*6 in perTups :
                            print(num)
                            input()
                            break
                
            
            
   
         
            
    
    
    



















    
