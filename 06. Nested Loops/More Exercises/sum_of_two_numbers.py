start = int(input())
end = int(input())
magic_num = int(input())
counter = 0
for num_1 in range(start, end + 1):
    for num_2 in range(start, end + 1):
        counter += 1
        if num_1 + num_2 == magic_num:
            print(f"Combination N:{counter} ({num_1} + {num_2} = {magic_num})")
            exit()
print(f"{counter} combinations - neither equals {magic_num}")
