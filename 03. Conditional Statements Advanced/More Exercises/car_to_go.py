budget = float(input())
season = input()
klasse = ""
car = ""
price = 0
if budget <= 100:
    klasse = "Economy class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.35
    elif season == "Winter":
        car = "Jeep"
        price = budget * 0.65
elif 100 < budget <= 500:
    klasse = "Compact class"
    if season == "Summer":
        car = "Cabrio"
        price = budget * 0.45
    elif season == "Winter":
        car = "Jeep"
        price = budget * 0.80
elif budget > 500:
    klasse = "Luxury class"
    car = "Jeep"
    price = budget * 0.9

print(f"{klasse}")
print(f"{car} - {price:.2f}")
