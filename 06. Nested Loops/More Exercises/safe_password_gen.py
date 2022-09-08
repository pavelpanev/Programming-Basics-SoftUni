a = int(input())
b = int(input())
max_passwords = int(input())
password_counter = 0

for asci_a in range(35, 56):
    for asci_b in range(64, 97):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                print(f"{chr(asci_a)}{chr(asci_b)}{x}{y}{chr(asci_b)}{chr(asci_a)}", end="|")
                asci_a += 1
                asci_b += 1
                password_counter += 1
                if asci_a > 55:
                    asci_a = 35
                if asci_b > 96:
                    asci_b = 64
                if y >= b and x >= a:
                    exit()
                if password_counter == max_passwords:
                    exit()

