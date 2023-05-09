print("***Python Program to Calculate BMI***")

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight/height**2)
print(BMI)

if BMI < 18.5:
    print(f"your BMI is {BMI},you are underweight.")
elif BMI < 25:
    print(f"your BMI is {BMI}, you are normal weight.")
elif BMI < 30:
    print(f"your BMI is {BMI}, you are overweight.")
elif BMI <35:
    print(f"your BMI is {BMI}, you are obese.")
else:
    print(f"your BMI is {BMI}, you are clinically obese.")