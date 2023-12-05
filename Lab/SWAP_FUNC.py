def swap(a,b):
    return b,a
def main():
    a=int(input("Enter the value of a:"))
    b=int(input("Enter the value of b:"))
    a,b=swap(a,b)
    print("Value of a is:",a,"and b is:",b)
if __name__=="__main__":
    main()
