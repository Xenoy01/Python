n=int(input("Enter the value of N:"))
s=1
if n>=1:
    for i in range(1,n+1):
        s=s*i
    print("The factorial is",s)
else:
    print("Please put a valid no.")
