first_num = int(input())
second_num = int(input())
third_num = int(input())

for first in range(1, first_num + 1):
    for second in range(1, second_num + 1):
        for third in range(1, third_num + 1):
            if first % 2 == 0 and third % 2 == 0:
                if second == 2 or second == 3 or second == 5 or second == 7:
                    print(f"{first} {second} {third}")
