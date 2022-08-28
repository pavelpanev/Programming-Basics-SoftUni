import sys

minimum = sys.maxsize
maximum = -sys.maxsize
n = int(input())

for i in range(1, n + 1):
    number = int(input())
    if number > maximum:
        maximum = number
    if number < minimum:
        minimum = number
print(f"Max number: {maximum}")
print(f"Min number: {minimum}")
