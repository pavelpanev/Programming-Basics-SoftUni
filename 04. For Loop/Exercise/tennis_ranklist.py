import math

tournaments = int(input())
starting_points = int(input())
added_points = 0
win_counter = 0
for _ in range(0, tournaments):
    reached = input()
    if reached == "W":
        added_points += 2000
        win_counter += 1
    elif reached == "F":
        added_points += 1200
    elif reached == "SF":
        added_points += 720

average_points_won = added_points / tournaments
won_tournaments = win_counter / tournaments * 100

print(f"Final points: {starting_points + added_points}")
print(f"Average points: {math.floor(average_points_won)}")
print(f"{won_tournaments:.2f}%")
