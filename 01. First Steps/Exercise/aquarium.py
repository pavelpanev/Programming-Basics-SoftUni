length = int(input())
width = int(input())
height = int(input())
taken_space_percentage = float(input())

total_space = length * width * height
liters_to_fit = total_space / 1000
whole_space = liters_to_fit - liters_to_fit * taken_space_percentage / 100
print(whole_space)
