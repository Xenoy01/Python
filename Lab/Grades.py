mark=int(input("Enter the mark of the student:"))
if mark>100 or mark<0:
    print("Please enter a valid mark")
elif mark>90:
    print("Grade O")
elif mark>80:
    print("Grade A")
elif mark>70:
    print("Grade B")
elif mark>60:
    print("Grade C")
elif mark>50:
    print("Grade D")
elif mark>40:
    print("Grade E")
else:
    print("Grade F")
