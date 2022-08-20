import math

figure = input()

if figure == "square":
    side = float(input())
    square_area = side * side
    print(f"{square_area:.3f}")

elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    rectangle_area = side_b * side_a
    print(f"{rectangle_area:.3f}")

elif figure == "circle":
    r = float(input())
    circle_area = math.pi * r * r
    print(f"{circle_area:.3f}")

elif figure == "triangle":
    side_1 = float(input())
    side_h = float(input())
    triangle_area = side_1 * side_h / 2
    print(f"{triangle_area:.3f}")
