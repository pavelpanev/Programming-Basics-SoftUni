first_pair_start = int(input())
second_pair_start = int(input())
first_pair_diff = int(input())
second_pair_diff = int(input())

for num1 in range(first_pair_start, first_pair_start + first_pair_diff + 1):
    for num2 in range(second_pair_start, second_pair_start + second_pair_diff + 1):
        if num2 == 11 or num2 == 13 or num2 == 17 or num2 == 19 or num2 == 23 or num2 == 29 or num2 == 31 or num2 == 37 or num2 == 41 or num2 == 43 or num2 == 47 or num2 == 53 or num2 == 59 or num2 == 61 or num2 == 67 or num2 == 71 or num2 == 73 or num2 == 79 or num2 == 83 or num2 == 89 or num2 == 97:
            if num1 == 11 or num1 == 13 or num1 == 17 or num1 == 19 or num1 == 23 or num1 == 29 or num1 == 31 or num1 == 37 or num1 == 41 or num1 == 43 or num1 == 47 or num1 == 53 or num1 == 59 or num1 == 61 or num1 == 67 or num1 == 71 or num1 == 73 or num1 == 79 or num1 == 83 or num1 == 89 or num1 == 97:
                print(f"{num1}{num2}")
