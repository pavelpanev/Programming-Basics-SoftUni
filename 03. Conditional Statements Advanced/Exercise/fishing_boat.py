budget = int(input())
season = input()
fishermen = int(input())
boat_price = 0

if season == "Spring":
    boat_price = 3000
    if fishermen <= 6:
        boat_price -= boat_price * 0.10
    elif 7 <= fishermen <= 11:
        boat_price -= boat_price * 0.15
    elif fishermen > 12:
        boat_price -= boat_price * 0.25
    if fishermen % 2 == 0:
        boat_price -= boat_price * 0.05
elif season == "Summer":
    boat_price = 4200
    if fishermen <= 6:
        boat_price -= boat_price * 0.10
    elif 7 <= fishermen <= 11:
        boat_price -= boat_price * 0.15
    elif fishermen > 12:
        boat_price -= boat_price * 0.25
    if fishermen % 2 == 0:
        boat_price -= boat_price * 0.05
elif season == "Autumn":
    boat_price = 4200
    if fishermen <= 6:
        boat_price -= boat_price * 0.10
    elif 7 <= fishermen <= 11:
        boat_price -= boat_price * 0.15
    elif fishermen > 12:
        boat_price -= boat_price * 0.25

elif season == "Winter":
    boat_price = 2600
    if fishermen <= 6:
        boat_price -= boat_price * 0.10
    elif 7 <= fishermen <= 11:
        boat_price -= boat_price * 0.15
    elif fishermen > 12:
        boat_price -= boat_price * 0.25
    if fishermen % 2 == 0:
        boat_price -= boat_price * 0.05
diff = abs(budget - boat_price)
if budget >= boat_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
