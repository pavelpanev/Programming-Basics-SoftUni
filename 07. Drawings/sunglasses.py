n = int(input())
# row1
for stars in range(0, 2 * n):
    print("*", end="")
for space in range(0, n):
    print(" ", end="")
for stars1 in range(0, 2 * n):
    print("*", end="")
# middle
for middle in range(0, n - 2):
    print()
    print("*", end="")
    for slash in range(0, 2 * n - 2):
        print("/", end="")
    print("*", end="")
    # odd
    if n % 2 != 0:
        if middle == (n - 1) / 2 - 1:
            for slash2 in range(0, n):
                print("|", end="")
        else:
            for inter in range(0, n):
                print(" ", end="")
    # even
    else:
        if middle == (n - 2) / 2 - 1:
            for slash3 in range(0, n):
                print("|", end="")
        else:
            for inter in range(0, n):
                print(" ", end="")
    print("*", end="")
    for slash1 in range(0, 2 * n - 2):
        print("/", end="")
    print("*", end="")
# last row
print()
for stars in range(0, 2 * n):
    print("*", end="")
for space in range(0, n):
    print(" ", end="")
for stars1 in range(0, 2 * n):
    print("*", end="")
