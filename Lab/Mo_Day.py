d=int(input("Enter the day value:"))
m=int(input("Enter the monyth value:"))
if(m>=3 and m<=6):
    if(m==3):
        print(d>=20 and d<=31)
    elif(m==6):
        print(d<=20 and d>=1)
    else:
        print(d>0 and d<=31)
        
