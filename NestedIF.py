#This is nested IF Program

#num=eval(input("\nEnter any Number   :  "))

Number=[22,42.7,335,98.0,0,-23,-45.3,-2,-89.0]
for num in Number:
    if num==0:
        print("\nThis is ZERO Number...")
    elif num>0 and type(num)==int:
        print("\n This is Positive Integer Number...")
    elif num>0 and type(num)==float:
        print("\n This is Positive Float...")
    elif num<0 and type(num)==int:
        print("\n This is Negative Integer...")
    elif num<0 and type(num)==float:
        print("\n This is Negative Float...")
    else:
        print("This is String...")
