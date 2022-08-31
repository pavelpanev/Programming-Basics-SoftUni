import sys

n = int(input())
max_sum = -sys.maxsize
min_sum = sys.maxsize
temp = 0
max_diff = -sys.maxsize
for _ in range(0, n):

    num_1 = int(input())
    num_2 = int(input())
    current_sum = num_1 + num_2

    if current_sum > max_sum:
        max_sum = current_sum
    if current_sum < min_sum:
        min_sum = current_sum
    if current_sum != max_sum:
        max_diff = abs(current_sum - max_sum)
    if current_sum != min_sum:
        max_diff = abs(current_sum - min_sum)

if max_sum == min_sum:
    print(f"Yes, value={max_sum}")
    exit()
print(f"No, maxdiff={max_diff}")
