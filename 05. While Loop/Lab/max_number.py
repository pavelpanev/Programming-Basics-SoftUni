import sys

number = input()
biggest_num = - sys.maxsize

while number != "Stop":
    if int(number) > biggest_num:
        biggest_num = int(number)
    number = input()
print(biggest_num)
