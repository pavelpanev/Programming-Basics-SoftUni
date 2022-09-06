prime_sum = 0
non_prime_sum = 0

while True:
    number = input()
    if number == "stop":
        break
    else:
        current_number = int(number)
        if current_number < 0:
            print("Number is negative.")
            continue
        else:
            is_prime = True
            if current_number < 2:
                is_prime = False
            else:
                for i in range(2, int(current_number / 2)):
                    if current_number % i == 0:
                        is_prime = False

    if is_prime:
        prime_sum += current_number
    else:
        non_prime_sum += current_number
print(f"Sum of all prime current_number is: {prime_sum}")
print(f"Sum of all non prime current_number is: {non_prime_sum}")
