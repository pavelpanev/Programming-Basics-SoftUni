x = float(input())
y = float(input())
h = float(input())

front_back_side = (x * x * 2) - (1.2 * 2)
side_sides = (x * y * 2) - (1.5 * 1.5 * 2)
green_paint = (front_back_side + side_sides) / 3.4
roof = (x * y * 2) + (0.5 * x * h * 2)
red_paint = roof / 4.3

print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")
