# Addition of 100 numbers
total = 0
for number in range(1, 101):
    total += number
print(total)

#Addition of Even Numbers
total_even = 0
for number in range(2, 101, 2):
    total_even += number
#printing inside the for loop will give sum of every step:
    print(total_even)

#printing outside the for loop will give the final output
print(total_even)


