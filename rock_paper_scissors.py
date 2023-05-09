import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors = [rock, paper, scissors]

user_Choice = int(input("What you want to choose? type 0 for rock, 1 for paper and 2 for scissors : \n"))
# we write if statement here to solve bug, ow it will give o/p you win
if user_Choice >=3 or user_Choice < 0:
  print("You typed an invalid number, you lose")
else:
  print(rock_paper_scissors[user_Choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(rock_paper_scissors[computer_choice])

if user_Choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_Choice == 2:
  print("You lose")
elif user_Choice > computer_choice:
  print("You win!")
elif computer_choice > user_Choice:
  print("You lose")
elif computer_choice == user_Choice:
  print("It's a draw")
