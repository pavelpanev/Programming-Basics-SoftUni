month = input()
days = int(input())
price_studio = 0
price_apart = 0
if month == "May" or month == "October":
    price_studio = 50 * days
    price_apart = 65 * days
    if days > 14:
        price_studio -= price_studio * 0.3
        price_apart -= price_apart * 0.1
    elif days > 7:
        price_studio -= price_studio * 0.05
elif month == "June" or month == "September":
    price_studio = 75.2 * days
    price_apart = 68.7 * days
    if days > 14:
        price_studio -= price_studio * 0.2
    if days > 14:
        price_apart -= price_apart * 0.1
elif month == "July" or month == "August":
    price_studio = 76 * days
    price_apart = 77 * days
    if days > 14:
        price_apart -= price_apart * 0.1
print(f"Apartment: {price_apart:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")
