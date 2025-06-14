
weight = float(input("What is your weight? \n"))

height = float(input("What is your height? \n"))

if height > 5:
    height = height / 100
else:
    height = height


bmi = weight / height**2

if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif 18 <= bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 <= bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 <= bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
  print(f"Your BMI is {bmi}, you are clinically obese.")