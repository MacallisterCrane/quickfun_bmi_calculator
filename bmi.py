height = int(input("Enter your height in M: "))
weight = int(input("Enter your weight in Kg: "))

bmi = round(weight / height ** 2)

if bmi < 18.5:
    print("You are underweight with a BMI of", bmi)
elif bmi < 25:
    print("You are in the normal weight range with a BMI of", bmi)
elif bmi < 30:
    print("You are overweight", bmi)
elif bmi < 35:
    print("You are obese, this needs attention", bmi)
else:
    print("You are clinically obese, this is very dangerous", bmi)
