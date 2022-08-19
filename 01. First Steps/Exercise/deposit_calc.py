deposit_sum = float(input())
months = int(input())
percentage = float(input())

total_sum = deposit_sum + months * ((deposit_sum * percentage / 100) / 12)
print(total_sum)
