first_num_limit = int(input())
second_num_limit = int(input())
third_num_limit = int(input())

for first in range(1, first_num_limit + 1):
    for second in range(1, second_num_limit + 1):
        for third in range(1, third_num_limit + 1):
            if third % 2 == 0 and first % 2 == 0:
                if second == 2 or second == 3 or second == 5 or second == 7:
                    print(f"{first} {second} {third}")
