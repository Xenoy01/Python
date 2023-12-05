a=int(input("Enter the no between 100 to 999:"))
if 100<=a<=999:
    b=a%10
    c=(a//10)%10
    d=(a//100)
    b1=b+c+d
    print("The sum of its digits is:",b1)
else:
    print("Please enter a valid number")
