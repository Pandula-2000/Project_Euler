# Project Euler
# Problem 20


n=100
ans=1

for i in range(1,n+1) :
    ans=ans*i
print( '100! is ' +str(ans))
print(sum([int(j) for j in str(ans)]))
