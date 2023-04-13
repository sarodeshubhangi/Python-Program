print("***This is the Program for BMI Converter***")

Height = input("Enter the Height : ")
Weight = input("Enter the Weight : ")

BMI = int(Weight)/float(Height)**2

BMI_as_int = int(BMI)

print(BMI_as_int)