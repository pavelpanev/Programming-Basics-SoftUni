import math

n = int(input())
# exceptions
if n == 1:
    print("*")
elif n == 2:
    print("**")
else:  # FirstLine
    leftRight = math.floor((n - 1) / 2)
    for space in range(0, leftRight):
        print("-", end="")
    if n % 2 == 0:
        print("**", end="")
    else:
        print("*", end="")
    for space in range(0, leftRight):
        print("-", end="")
    # Until Middle
    leftRight -= 1
    mid = n - 2 * leftRight - 2
    while leftRight >= 0:
        print()
        for space in range(0, leftRight):
            print("-", end="")
        print("*", end="")
        for space_middle in range(0, mid):
            print("-", end="")
        print("*", end="")
        for space in range(0, leftRight):
            print("-", end="")
        leftRight -= 1
        mid = n - 2 * leftRight - 2
    # After Middle
    leftRight += 2
    mid1 = n - 2 * leftRight - 2
    while leftRight < math.floor((n - 1) / 2):
        print()
        for space in range(0, leftRight):
            print("-", end="")
        print("*", end="")
        for space_middle in range(0, mid1):
            print("-", end="")
        print("*", end="")
        for space in range(0, leftRight):
            print("-", end="")
        leftRight += 1
        mid1 = n - 2 * leftRight - 2
    print()
    for space in range(0, leftRight):
        print("-", end="")
    if n % 2 == 0:
        print("**", end="")
    else:
        print("*", end="")
    for space in range(0, leftRight):
        print("-", end="")
