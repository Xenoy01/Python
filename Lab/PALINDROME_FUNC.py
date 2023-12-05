def palindrome(n):
    new=0
    k=n
    while(n>0):
        dig=n%10
        new=(new*10)+dig
        n=n//10
    if new==k:
        return True
    else:
        return False
def main():
    num=int(input("Enter the number:"))
    print("Is the number palindrome:",palindrome(num))
if __name__=="__main__":
    main()
