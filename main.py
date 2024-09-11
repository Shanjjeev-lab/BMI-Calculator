height = float(int("Enter your height in cm: "))
weight = float(int("Enter your weight in kg: "))

bmi = weight / (height / 100) ** 2

print("BMI", bmi)

if bmi <= 18.5:
    print("You are Underweight")

elif bmi <= 29.5:
    print("You are Healthy")

elif bmi <= 29.9:
    print("You are Overweight")

elif bmi <= 34.9:
    print("You are severly Overweight")

elif bmi <= 39.9:
    print("You are Obese")
else:
    print("You are severly Obese")