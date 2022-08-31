students = int(input())
grade_fail = 0
grade_3 = 0
grade_4 = 0
top_students = 0
average = 0
for _ in range(0, students):
    grade = float(input())
    average += grade
    if 2 <= grade <= 2.99:
        grade_fail += 1
    elif 3 <= grade <= 3.99:
        grade_3 += 1
    elif 4 <= grade <= 4.99:
        grade_4 += 1
    elif grade >= 5:
        top_students += 1

percentage_grade_fail = grade_fail / students * 100
percentage_grade_3 = grade_3 / students * 100
percentage_grade_4 = grade_4 / students * 100
percentage_top_students = top_students / students * 100
average_grade = average / students

print(f"Top students: {percentage_top_students:.2f}%")
print(f"Between 4.00 and 4.99: {percentage_grade_4:.2f}%")
print(f"Between 3.00 and 3.99: {percentage_grade_3:.2f}%")
print(f"Fail: {percentage_grade_fail:.2f}%")
print(f"Average: {average_grade:.2f}")
