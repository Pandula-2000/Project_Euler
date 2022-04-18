# Project Euler
# Problem 40


num = 1
deci = ''

while len(deci) < 9999999 :
    deci = deci + str(num)
    num += 1
 
    
 print(deci[9]*deci[99]*deci[999]*deci[9999]*deci[99999]*deci[999999])
 
    
    
    
