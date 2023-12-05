def HCF(x,y):
    if x>y:
        small=x
    else:
        small=y
    for i in range (1,small+1):
        if((x%i==0) and (y%i==0)):
            hcf=i
    if hcf==1:
        return 1
    else:
        return 0
a=int(input("Enter the first no."))
b=int(input("Enter the second no."))
if HCF(a,b):
    print("is co-prime")
else:
    print("not co prime")
