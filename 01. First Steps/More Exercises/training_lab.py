import math

length = float(input())
width = float(input())

width = width - 1
desks_per_columns = math.floor(width / 0.7)
all_columns = math.floor(length / 1.2)
all_space = desks_per_columns * all_columns - 3
print(all_space)
