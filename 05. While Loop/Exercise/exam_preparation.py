bad_grades_number = int(input())
bad_grades_counter = 0
task_name = ""
average_score = 0
number_of_problems = 0
last_problem = ""

while True:

    task_name = input()
    if task_name == "Enough":
        break

    task_grade = int(input())
    number_of_problems += 1
    if task_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == bad_grades_number:
            print(f"You need a break, {bad_grades_counter} poor grades.")
            exit()

    average_score += task_grade
    last_problem = task_name

print(f"Average score: {(average_score / number_of_problems):.2f}")
print(f"Number of problems: {number_of_problems}")
print(f"Last problem: {last_problem}")
