n = int(input())
counter = 1
summ = 0
while counter <= n:
    number = int(input())
    summ += number
    counter += 1
print(f"{(summ / (counter - 1)) :.2f}")
