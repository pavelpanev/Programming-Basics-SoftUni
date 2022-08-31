import sys

n = int(input())
sum_even = 0
sum_odd = 0
biggest_odd = - sys.maxsize
biggest_even = - sys.maxsize
lowest_odd = sys.maxsize
lowest_even = sys.maxsize
for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 0:
        sum_even += num
        if num > biggest_even:
            biggest_even = num
        if num < lowest_even:
            lowest_even = num
    else:
        sum_odd += num
        if num > biggest_odd:
            biggest_odd = num
        if num < lowest_odd:
            lowest_odd = num

print(f"OddSum={sum_odd:.2f},")
if lowest_odd == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={lowest_odd:.2f},")
if biggest_odd == - sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={biggest_odd:.2f},")
print(f"EvenSum={sum_even:.2f},")
if lowest_even == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={lowest_even:.2f},")
if biggest_even == - sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={biggest_even:.2f}")
