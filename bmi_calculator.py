weight = float(input("enter your weight: "))
height = float(input("enter your height: "))
BMI = weight / (height ** 2)
if BMI<18.5:
    print("you are underweight")
elif BMI<24.9:
    print("you are normal")
elif BMI<30:
    print("you are overweight")
else:
    print("you are obese")
