n=int(input("Enter the value of N:"))
a=1;b=2;c=3
print(a,end=" ")
print(b,end=" ")
print(c,end=" ")
if n>=1:
    for i  in range (4,n+1):
        d=a+b+c
        a,b,c=b,c,d
        print(d,end=" ")
