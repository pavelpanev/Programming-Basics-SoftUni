moves_in_the_game = int(input())
points = 0
pp1 = 0
pp2 = 0
pp3 = 0
pp4 = 0
pp5 = 0
invalid_move = 0
for _ in range(0, moves_in_the_game):
    points_on_the_move = int(input())

    if 0 <= points_on_the_move <= 9:
        points += points_on_the_move * 0.2
        pp1 += 1
    elif 10 <= points_on_the_move <= 19:
        points += points_on_the_move * 0.3
        pp2 += 1
    elif 20 <= points_on_the_move <= 29:
        points += points_on_the_move * 0.4
        pp3 += 1
    elif 30 <= points_on_the_move <= 39:
        points += 50
        pp4 += 1
    elif 40 <= points_on_the_move <= 50:
        points += 100
        pp5 += 1
    else:
        points = points / 2
        invalid_move += 1

percentage_pp1 = pp1 / moves_in_the_game * 100
percentage_pp2 = pp2 / moves_in_the_game * 100
percentage_pp3 = pp3 / moves_in_the_game * 100
percentage_pp4 = pp4 / moves_in_the_game * 100
percentage_pp5 = pp5 / moves_in_the_game * 100
percentage_invalid_move = invalid_move / moves_in_the_game * 100

print(f"{points:.2f}")
print(f"From 0 to 9: {percentage_pp1:.2f}%")
print(f"From 10 to 19: {percentage_pp2:.2f}%")
print(f"From 20 to 29: {percentage_pp3:.2f}%")
print(f"From 30 to 39: {percentage_pp4:.2f}%")
print(f"From 40 to 50: {percentage_pp5:.2f}%")
print(f"Invalid numbers: {percentage_invalid_move:.2f}%")
