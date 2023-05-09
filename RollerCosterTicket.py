print("***Program to calculate the Rollercoaster Tickets*** ")

height = int(input("What is your Height in cm? : "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age : "))
    if age < 12:
      print("Please pay 5 euros")
    elif age <= 18:
      print("Please pay 7 euros")
    elif age <=25:
      print("Please pay 12 euros")
    else:
      print("You have to pay 15 euros")
else:
    print("Sorry! You have to grow taller before ride")