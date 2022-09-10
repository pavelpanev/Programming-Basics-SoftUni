n = int(input())

for row in range(1, n + 1):
    intervals = n - row
    for inter in range(intervals, 0, -1):
        print("", end=" ")
    print("* ", end="")
    for star in range(1, row):
        print("*", end=" ")
    print()

for row1 in range(n - 1, 0, -1):
    intervals1 = n - row1
    for inter1 in range(intervals1, 0, -1):
        print("", end=" ")
    print("* ", end="")
    for star1 in range(1, row1):
        print("*", end=" ")
    print()
