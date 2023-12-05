def prime(n):
    k=int(n**0.5)
    if n%2==0 or n%3==0:
        return n==2 or n==3
    for i in range(5,k+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    else:
        return True
def main():
    num=int(input("Enter the number:"))
    print("Is the entered no. prime:",prime(num))
if __name__=="__main__":
    main()
