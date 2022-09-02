payment = input()
summ = 0

while payment != "NoMoreMoney":
    if float(payment) <= 0:
        print("Invalid operation!")
        break
    else:
        summ += float(payment)
        print(f"Increase: {float(payment):.2f}")
        payment = input()
print(f"Total: {summ:.2f}")
