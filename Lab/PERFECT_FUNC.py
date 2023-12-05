def perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        return True
    else:
        return False
def main():
    num=int(input("Enter the number:"))
    print("Is th number perfect:",perfect(num))
if __name__=="__main__":
    main()
