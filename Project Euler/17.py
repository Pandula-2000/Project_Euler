# Project Euler
# Problem 17

a='one'
b='two'
c='three'
d='four'
e='five'
f='six'
g='seven'
h='eight'
i='nine'
j='ten'
list1=[a,b,c,d,e,f,g,h,i,j]

aa='eleven'
bb='twelve'
cc='thirteen'
dd='fourteen'
ee='fifteen'
ff='sixteen'
gg='seventeen'
hh='eighteen'
ii='nineteen'
list2=[aa,bb,cc,dd,ee,ff,gg,hh,ii]

aaa='twenty'
bbb='thirty'
ccc='forty'
ddd='fifty'
eee='sixty'
fff='seventy'
ggg='eighty'
hhh='ninety'
list3=[aaa,bbb,ccc,ddd,eee,fff,ggg,hhh]

count = 0

for j in list1 :
    print(j)
    count = count + len(j)
        
for k in list2:
    print(k)
    count = count + len(k)


for num1 in list3 :
    print(num1)
    count = count + len(num1)
    for num2 in list1[:9] :
        print(num1 + num2)
        count = count + len(num1+num2)
            
for l in list1[:9] :
    print(l + 'hundred')
    count = count +len(l + 'hundred')
    for num3 in list1 :
        print(l + 'hundredand' + num3)
        count = count + len(l + 'hundredand' + num3)
    for num4 in list2 :
        print(l + 'hundredand' + num4)
        count = count + len(l + 'hundredand' + num4)

    for num5 in list3 :
        print(l + 'hundredand' + num5)
        count = count + len(l + 'hundredand' + num5)
        for num6 in list1[:9] :
            print(l + 'hundredand' + num5 + num6)
            count = count + len(l + 'hundredand' + num5 + num6)
print('onethousand')
count = count + len('onethousand')
print(count)      
   
    
  
    






    
