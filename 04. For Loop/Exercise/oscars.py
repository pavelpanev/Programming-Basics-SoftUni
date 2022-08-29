actor_name = input()
points_from_academy = float(input())
judges_number = int(input())

for _ in range(0, judges_number):
    judge_name = input()
    points_from_judge = float(input())
    points_from_academy += len(judge_name) * points_from_judge / 2
    if points_from_academy > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points_from_academy:.1f}!")
        exit()
needed_points = 1250.5 - points_from_academy
print(f"Sorry, {actor_name} you need {needed_points:.1f} more!")
