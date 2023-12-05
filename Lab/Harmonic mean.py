N=int(input("Enter the value of n:"))
Sum=0
for i in range(1,N+1):
    Sum=Sum+(1/i)
H=N/(Sum)
print("The Harmonic mean is ",H)
