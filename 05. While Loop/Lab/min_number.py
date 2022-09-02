import sys

number = input()
smallest_num = sys.maxsize

while number != "Stop":
    if int(number) < smallest_num:
        smallest_num = int(number)
    number = input()
print(smallest_num)
