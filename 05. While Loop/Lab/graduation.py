student_name = input()
grade = 1
counter = 0
average_grade = 0
while grade <= 12:
    yearly_grade = float(input())
    if yearly_grade < 4.00:
        counter += 1
        if counter > 1:
            print(f"{student_name} has been excluded at {grade} grade")
            exit()
        continue
    average_grade += yearly_grade
    grade += 1
print(f"{student_name} graduated. Average grade: {(average_grade / 12):.2f}")
