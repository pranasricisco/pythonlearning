# Dictionay {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36.........., n: n*n}
num=int(input("Enter a Number  :  "))
i=0
for i in range(0,num):
    print(i,i*i)
    i=i+1

d=dict()

#Second Method

for j in range(0,num+1):
    d[j]=j*j

print(d)
