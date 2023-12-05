a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
dis=(b**2)-(4*a*c)
if dis>0:
    print("2 real roots")
elif dis==0:
    print("1 real roots")
else:
    print("no real roots")
