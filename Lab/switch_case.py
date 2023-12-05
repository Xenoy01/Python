def switch(n):
    switcher={
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday"}
    return switcher.get(n,"invalid")
a=int(input("Enter the number:"))
print(switch(a))
