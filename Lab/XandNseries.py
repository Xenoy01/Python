n=int(input("Enter the value of N:"))
x=int(input("Enter the value of x:"))
s=1
for i in range(1,n+1):
        s=s*i
a=(x**n)/s
print("The answer is ",a)
