first_num = int(input())
second_num = int(input())

for number in range(first_num, second_num + 1):
    number_to_str = str(number)
    even_sum = 0
    odd_sum = 0
    for num, digit in enumerate(number_to_str):
        if num % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end=" ")
