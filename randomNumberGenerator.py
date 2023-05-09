import random

# Random number for integer
random_integer = random.randint(1, 10)
print(random_integer)

#Random number for float.... This will generate only upto 0.999... not upto 1
# range of random float  0.000000 - 0.9999999
random_float = random.random()
print(random_float)

#if you want to increse the number multiply it with that number
#The range will be now 4.999999.... but not 5
random_float = random.random() * 5
print(random_float)


# Program to calculate Heads or Tails 🎲

dice = random.randint(0, 1)
if dice == 1:
    print("Head")
else:
    print("Tail")