wg=float(input("Enter the weight of the person in pound:"))
hg=float(input("Enter the height of the person in inch:"))
pound=wg*0.45359237
mtr=hg*0.0254
BMI=pound/(mtr**2)
print("Your BMI is:",BMI)
