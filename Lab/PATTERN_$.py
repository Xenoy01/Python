def simple_pyramid():
    for i in range(1,6):
        for j in range(0,i):
            print("*",end=' ')
        print('\n')
def R_simple_pyramid():
    for i in range(1,6):
    #white space
        for j in range(0,5-i):
            print(" ",end=' ')
        for k in range(0,i):
            print("*",end=' ')
        print("\n")
def Number_pyramid():
    for i in range(1,5):
        for j in range(0,i):
            print(i,end=' ')
        print('\n')
def continuous_pyramid():
    c=1
    for i in range(1,5):
        for j in range(0,i):
            print(c,end=' ')
            c=c+1
        print('\n')
def switch(n):
    switcher={
    1:simple_pyramid,
    2:R_simple_pyramid,
    3:Number_pyramid,
    4:continuous_pyramid
    }
    return switcher.get(n,"Invalid")()
def main():
    print("The options are:")
    print("1:Simple Pyramid");
    print("2:Rotated Simple Pyramid")
    print("3:Number Pyramid")
    print("4:Continuous Number Pyramid")
    a=int(input("Enter your choice:"))
    if a<5:
        switch(a)
    elif(a==1):
        simple_pyramid()
    elif(a==2):
        R_simple_pyramid()
    elif(a==3):
        Number_pyramid()
    elif(a==4):
        continuous_pyramid()
    else:
        print("Invalid Choice")
if __name__=="__main__":
    main()
