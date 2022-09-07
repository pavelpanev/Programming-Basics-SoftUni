number_of_days = int(input())
hours_for_day = int(input())
total = 0
for days in range(1, number_of_days + 1):
    pay_per_day = 0
    for hours in range(1, hours_for_day + 1):
        if days % 2 == 0 and hours % 2 != 0:
            pay_per_day += 2.50
        elif days % 2 != 0 and hours % 2 == 0:
            pay_per_day += 1.25
        else:
            pay_per_day += 1
    total += pay_per_day
    print(f"Day: {days} - {pay_per_day:.2f} leva")
print(f"Total: {total:.2f} leva")
