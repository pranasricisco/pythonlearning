# divisible by 7 but are not a multiple of 5 | between 2000 and 3200 (both included).

i=2000
j=3200

for k in range(i,j):
    if k%7==0 and k%5!=0:
        print(k)

#Second Methode

num=[]

for l in range(i,j):
    if l%7==0 and l%5!=0:
        num.append(str(l))
print(num)
