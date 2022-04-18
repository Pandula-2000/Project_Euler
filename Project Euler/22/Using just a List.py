# Project Euler
# Problem 22
# Using a List

f = open("p022_names.txt","r")
lst = f.read()
names = lst.split(",")
names.sort()
#print(names)

alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


score = 0
for name in names :
    x = name[1:-1]
    summ = 0
    for letter in x :
        summ += alp.index(letter)+1
    score += summ*(names.index(name)+1)



print(score)
f.close()
        
# This way is Easy!

