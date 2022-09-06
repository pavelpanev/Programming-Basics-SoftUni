jury = int(input())
all_average = 0
all_grades = 0
while True:

    presentation = input()
    current_average = 0
    if presentation == "Finish":
        break
    else:
        for _ in range(0, jury):
            all_grades += 1
            grade = float(input())
            current_average += grade
            all_average += grade

        print(f"{presentation} - {(current_average / jury):.2f}.")
print(f"Student's final assessment is {(all_average / all_grades):.2f}.")
