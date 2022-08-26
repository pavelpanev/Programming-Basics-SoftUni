budget = float(input())
category = input()
all_people = int(input())

if 1 <= all_people <= 4:
    budget -= budget * 0.75
elif 5 <= all_people <= 9:
    budget -= budget * 0.6
elif 10 <= all_people <= 24:
    budget -= budget * 0.5
elif 25 <= all_people <= 49:
    budget -= budget * 0.4
elif all_people >= 50:
    budget -= budget * 0.25

if category == "VIP":
    budget = budget - all_people * 499.99
elif category == "Normal":
    budget = budget - all_people * 249.99

if budget >= 0:
    print(f"Yes! You have {budget:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(budget):.2f} leva.")
