# Project Euler
# Problem 42


wordsFile = open("p042_words.txt","r").read()
wordsFile = wordsFile[1:]
wordsFile = wordsFile[0:-1]



words = wordsFile.split('","')
#print(words)
 # Just to find the word with maximmum letters
x = 0           
for i in words:
    if len(i) > x :
        x = len(i)
#print(x)
# This gives out x = 14. so the biggest possible number
# we can made is (14*26) = 364. This means that the biggest
# number we have to check is 364.
# SO WE GET A LIST OF TRI NUM: UNDER 364.

triList = [1]
n = 2

while triList[-1] < 364 :
    triList.append(int((n*(n+1))/2))
    n += 1
    
#print(triList)

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
triWords = []

for word in words :
    total = 0
    for letter in word :
        total += alpha.index(letter) + 1
    if total in triList :
        triWords.append(word)
print(triWords)
print(len(triWords))
        
open("p042_words.txt","r").close()    
    

















    
    


