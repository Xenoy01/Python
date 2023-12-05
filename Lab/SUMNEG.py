n=int(input("Enter the value of N:"))
s=0;a=1
if n>=1:
    for i in range(1,n+1,2):
        s=s+(a*i)
        a=-a
    print("The sum is",s)
else:
    print("Please put a valid no.")
