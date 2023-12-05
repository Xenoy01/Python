def fact(n1):
    f=1
    for i in range(1,n1+1):
        f*=i
    return f
def main():
    n=int(input("Enter the value of n:"))
    if n==0:
        print("The factorial is:1")
    elif n>0:
        print("The factorial is:",fact(n))
    else:
        print("Please Enter a valid no.")
if __name__ == "__main__":
    main()
