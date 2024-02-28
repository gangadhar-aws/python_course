height = input("Enter your Height in Meters : ")
weight = input("Enter Weight in kgs :")

bmi = round(int(weight)/float(height)**2, 2)

if bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi > 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 25 and bmi <30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you are normal weight.")
else:
    print(f"Your BMI is {bmi}, you are underweight")