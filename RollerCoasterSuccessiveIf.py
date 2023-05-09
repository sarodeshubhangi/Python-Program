print("***Successive if statement using Roller coster Tickets Example*** ")

height = int(input("What is your Height in cm? : "))

if height >= 120:
  print("You can ride the roller coster")
  age = int(input("What is your age : "))
  if age < 12:
    bill = 5
    print("Please pay 5 euros")
  elif age <= 18:
    bill = 7
    print("Please pay 7 euros")
  elif age <= 25:
    bill = 12
    print("Please pay 12 euros")
  else:
    bill = 15
    print("You have to pay 15 euros")

  want_photos = input("Do you want a photo taken? Y or N :")
  if want_photos == "Y":
    bill += 3

  print(f"Your final bill is {bill}")
else:
  print("Sorry! You have to grow taller before ride")