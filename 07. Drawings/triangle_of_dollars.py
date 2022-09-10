n = int(input())
for row in range(n):
    for col in range(-1, row):
        print("$", end=" ")
    print()
