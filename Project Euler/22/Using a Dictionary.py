# Project Euler
# Problem 22
# UIsing a Dictionary to store the alphabet.


f = open("p022_names.txt","r")
lst=f.read()
names =lst.split(",")
names.sort()
#print(names)


alp = {"A" : 1, "B" : 2  ,"C" :3, "D" : 4 ,"E" : 5 , "F" : 6 ,"G" : 7 , "H" : 8 ,"I" : 9 , "J" : 10 ,"K" : 11 , "L" : 12 ,"M" : 13 , "N" : 14 ,"O" : 15 , "P" : 16 , "Q" : 17 , "R" : 18 ,"S" : 19, "T" : 20 ,"U" : 21, "V" : 22 ,"W" : 23 , "X" :24 ,"Y" :25, "Z" : 26}
#print(alp)


score = 0


for i in names:
    summ = 0
    x = i[1:-1]
    for j in x:
        summ += alp[j]
    score = score + summ*(names.index(i)+1)
    
print(score)

f.close()
