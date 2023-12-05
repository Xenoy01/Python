n=input("Enter the value of N:")
"""lst=[x for x in n]
lst.reverse()
print(int(lst))"""
a=len(n)
n=int(n)
new=0
for i in range(a-1,-1,-1):
    rem=n%10
    n=n//10
    new=new+(rem*(10**i))
print(new)
