fee_yearly = int(input())
sneakers = 0.6 * fee_yearly
suit = sneakers - sneakers * 0.2
ball = suit / 4
accessories = ball / 5

total_sum = fee_yearly + sneakers + suit + ball + accessories
print(total_sum)
