n = int(input())
current_num = 1
is_bigger = False

for row in range(1, n + 1):
    for col in range(1, row + 1):

        if current_num <= n:
            print(f"{current_num}", end=" ")
        else:
            is_bigger = True
            break
        current_num += 1
    if is_bigger:
        break
    print()
