# This First for loop program :

num=[2,4,6,3,23,4,6,7,8,2,3,5,7,8,7,6,4,3,2,6,8,7,5,4,3,2,1,0]
sum=0
esum=0
osum=0
for x in num:
        sum=sum+x
print("Total =",sum)

for y in num:
    if y%2==0:
        esum=esum+y
print("Even Number Sum =",esum)

for z in num:
    if z%2!=0:
        osum=osum+z
print("Odd Number Sum = ",osum)

xsum=0
ysum=0
for x in num:
    if x%2==0:
        xsum=xsum+x
    else:
        ysum=ysum+x
print("\nEven SUM =",xsum,"\nOdd SUM =",ysum)
