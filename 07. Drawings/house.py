import math

n = int(input())
current_stars = 0
# roof
rooftop = math.floor((n + 1) / 2)
for roof in range(0, rooftop):
    if roof == 0:
        if n % 2 == 0:
            for interval in range(0, math.floor(n / 2 - 1)):
                print("-", end="")
            print("**", end="")
            for interval in range(0, math.floor(n / 2 - 1)):
                print("-", end="")
            current_stars = 2
        else:
            for interval1 in range(0, math.floor(n / 2)):
                print("-", end="")
            print("*", end="")
            for interval1 in range(0, math.floor(n / 2)):
                print("-", end="")
            current_stars = 1
    else:  # under roof
        print()
        stars_to_be_printed = current_stars + 2
        if stars_to_be_printed == n:
            for stars in range(0, n):
                print("*", end="")
        else:
            spaces = math.floor((n - stars_to_be_printed) / 2)
            for space in range(0, spaces):
                print("-", end="")
            for stars in range(0, stars_to_be_printed):
                print("*", end="")
            for space in range(0, spaces):
                print("-", end="")
            current_stars += 2
# body
print()
if n % 2 == 0:
    left_rows = int(n / 2)
else:
    left_rows = int(n - math.ceil(n / 2))
for body in range(0, left_rows):
    print("|", end="")
    for star1 in range(0, n - 2):
        print("*", end="")
    print("|")
