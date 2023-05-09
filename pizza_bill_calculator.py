
print("***This is the program to calculate the bill for pizza***")

size = input("What size of pizza do you want? S , M , L: ")
add_pepperoni = input("Do you want Pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size == "S":
    bill += 20
elif size == "M":
    bill += 30
else:
    size == "L"
    bill += 40

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 5

if extra_cheese == "Y":
    bill += 3

print(f"Your bill is : € {bill}")