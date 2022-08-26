season = input()
km_per_month = float(input())
salary = 0
if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        salary = km_per_month * 0.75
    elif 5000 < km_per_month <= 10000:
        salary = km_per_month * 0.95
    elif 10000 < km_per_month <= 20000:
        salary = km_per_month * 1.45

if season == "Summer":
    if km_per_month <= 5000:
        salary = km_per_month * 0.9
    elif 5000 < km_per_month <= 10000:
        salary = km_per_month * 1.10
    elif 10000 < km_per_month <= 20000:
        salary = km_per_month * 1.45

if season == "Winter":
    if km_per_month <= 5000:
        salary = km_per_month * 1.05
    elif 5000 < km_per_month <= 10000:
        salary = km_per_month * 1.25
    elif 10000 < km_per_month <= 20000:
        salary = km_per_month * 1.45

salary = salary * 4
salary -= salary * 0.1
print(f"{salary:.2f}")
