trip_cost = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())
total_profit = puzzles * 2.60 + dolls * 3 + bears * 4.10 + minions * 8.20 + trucks * 2
total_toys = puzzles + dolls + bears + minions + trucks
if total_toys >= 50:
    total_profit -= total_profit * 0.25
rent = total_profit * 0.10
total_profit -= rent
diff = abs(total_profit - trip_cost)
if total_profit >= trip_cost:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")

