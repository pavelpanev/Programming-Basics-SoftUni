men = int(input())
women = int(input())
tables = int(input())
free_seats = tables * 2

for man in range(1, men + 1):
    for woman in range(1, women + 1):
        print(f"({man} <-> {woman})", end=" ")
        free_seats -= 2
        if free_seats < 2:
            exit()
