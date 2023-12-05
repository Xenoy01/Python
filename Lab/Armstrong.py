a=int(input("Enter the no between 100 to 999:"))
if 100<=a<=999:
    b=a%10
    c=(a//10)%10
    d=(a//100)
    b1=((b**3)+(c**3)+(d**3))
    if b1==a:
        print(a,"is an Armstrong number")
    else:
        print(a,"is not an Armstrong number")
else:
    print("Please enter a valid number")
