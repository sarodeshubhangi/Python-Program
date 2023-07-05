student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# Creating an empty string
student_grades ={}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
       student_grades[student] = "Outstnading"
    elif score > 80:
       student_grades[student] = "Exceeds expectations"
    elif score > 70:
       student_grades[student] = "Acceptable"
    else:
       student_grades[student] = "Fail"

print(student_grades)
