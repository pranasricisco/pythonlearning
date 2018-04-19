# Get a Factorial of a Programme

num=int(input("\nEnter any Integer number : "))
fact=1
if num>0 :
    for num in range(1,num+1):
        fact=num*fact
elif num==0 :
    print("\n Number is ZERO")
else :
    print("\n Please Enter Positive Number...")

print("Factorial of ",num,"is ",fact)

num1=int(input("\n Enter another Integer Value  :  "))

def rec_Fact(num1):
    if num1==1 or num1==0:
        return 1
    else:
        return num1*rec_Fact(num1-1)
print(rec_Fact(num1))
