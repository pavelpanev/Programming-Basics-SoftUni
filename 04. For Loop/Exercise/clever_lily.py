lily_age = int(input())
w_machine_price = float(input())
price_per_toy = int(input())
ten = 10
collected_money = 0

for age in range(1, lily_age + 1):
    if age % 2 == 0:
        collected_money += ten - 1
        ten += 10
    else:
        collected_money += price_per_toy

if collected_money >= w_machine_price:
    n = collected_money - w_machine_price
    print(f"Yes! {n:.2f}")
else:
    m = w_machine_price - collected_money
    print(f"No! {m:.2f}")
