def range1(a1,b1,n1):
    if a1<=n1<=b1:
        return True
    else:
        return False
def main():
    a=int(input("Enter the lower limit:"))
    b=int(input("Enter the upper limit:"))
    n=int(input("Enter th number:"))
    print("Is the no. in the range:",range1(a,b,n))
if __name__=="__main__":
    main()
