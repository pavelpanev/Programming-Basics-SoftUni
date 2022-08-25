projection_type = input()
rows = int(input())
cols = int(input())
profit = 0
all_places = rows * cols

if projection_type == "Premiere":
    profit = all_places * 12
elif projection_type == "Normal":
    profit = all_places * 7.50
elif projection_type == "Discount":
    profit = all_places * 5
print(f"{profit:.2f} leva")
