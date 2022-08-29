import sys

n = int(input())
summ = 0
max_num = -sys.maxsize

for _ in range(0, n):
    num = int(input())
    if num > max_num:
        max_num = num
    summ = summ + num

if max_num == summ - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    print("No")
    print(f"Diff = {abs((summ - max_num) - max_num)}")
