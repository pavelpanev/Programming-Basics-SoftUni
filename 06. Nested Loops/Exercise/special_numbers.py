n = int(input())
number = 1111
while number <= 9999:
    counter = 0
    for index, digit in enumerate(str(number)):
        if int(digit) == 0:
            break
        if n % int(digit) == 0:
            counter += 1
    if counter == 4:
        print(f"{number}", end=" ")
    number += 1
