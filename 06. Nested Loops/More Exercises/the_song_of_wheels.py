m = int(input())
password_counter = 0
password = " "
printed = False
for num1 in range(1, 10):
    for num2 in range(1, 10):
        for num3 in range(1, 10):
            for num4 in range(1, 10):
                if num1 < num2 and num3 > num4:
                    if num1 * num2 + num3 * num4 == m:
                        print(f"{num1}{num2}{num3}{num4}", end=" ")
                        print("", end="")
                        printed = True
                        password_counter += 1
                        if password_counter == 4:
                            password = f"{num1}{num2}{num3}{num4}"
if password == " " or printed == False:
    print()
    print("No!")
else:
    print()
    print(f"Password: {password}")
