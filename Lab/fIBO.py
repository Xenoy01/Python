n=int(input("Enter the value of N:"))
a=0;b=1
print(a,end=" ")
print(b,end=" ")
if n>=1:
    for i  in range (3,n+1):
        c=b
        b=a+b
        a=c
        print(b,end=" ")
