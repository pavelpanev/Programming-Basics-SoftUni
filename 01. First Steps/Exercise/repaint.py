nylon = int(input())
paint = int(input())
paint_water = int(input())
workers_hours = int(input())

nylon_sum = (nylon + 2) * 1.50
paint_sum = (paint + paint * 0.1) * 14.50
paint_water_sum = paint_water * 5

materials_sum = nylon_sum + paint_sum + paint_water_sum + 0.40
workers_per_hour = (materials_sum * 0.3) * workers_hours

total_sum = materials_sum + workers_per_hour
print(total_sum)
