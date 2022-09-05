interval_beginning = int(input())
interval_ending = int(input())
magic_num = int(input())
counter = 0
for num1 in range(interval_beginning, interval_ending + 1):
    for num2 in range(interval_beginning, interval_ending + 1):
        counter += 1
        if num1 + num2 == magic_num:
            print(f"Combination N:{counter} ({num1} + {num2} = {magic_num})")
            exit()
print(f"{counter} combinations - neither equals {magic_num}")
