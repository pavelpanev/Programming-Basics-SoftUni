n = int(input())

for i in range(0, n + 1):
    for inter in range(0, n - i):
        print("", end=" ")
    for stars in range(0, i):
        print("*", end="")
    print(" | ", end="")
    for stars1 in range(0, i):
        print("*", end="")
    print()
