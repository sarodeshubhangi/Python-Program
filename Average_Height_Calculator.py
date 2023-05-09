print("This is the program to calculate average height of students using for loop")
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for height in student_heights:
  total_height += height
  # if this print will write inside for loop it will print the numbers one by one instead total
print(total_height)

number_of_students = 0
for student in student_heights:
  number_of_students += 1
print(number_of_students)

average_Height = round(total_height / number_of_students)
print(average_Height)

'''print("This is the program to calculate average height of students using sum and len function without using for loop")
student_heights_sum = sum(student_heights)
print(student_heights_sum)

number_of_students = len(student_heights)
print(number_of_students)

Average_Height = round(student_heights_sum / number_of_students)'''