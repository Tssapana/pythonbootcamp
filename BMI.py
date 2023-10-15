Height= float(input(("Enter height in m:")))

Weight= float(input(("Enter weight in Kg:")))

Height_new= (Height)*(Height) 

BMI = (Weight)/(Height_new)

print("BMI:", int(BMI))

if BMI < 18.5:
    print( " you are underweight")
elif BMI < 25:
    print (" you are normal weight")
elif BMI < 30:
  print(" you are overweight")
else:
    print(" you are obese")

# print(f"Your BMI is {BMI}, you are {category}.")


