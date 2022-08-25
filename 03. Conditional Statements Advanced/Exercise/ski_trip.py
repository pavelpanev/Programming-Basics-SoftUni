sleeping_in = int(input())
sleeping_in -= 1
room = input()
grade = input()
price = 0
if room == "room for one person":
    price = sleeping_in * 18
    if grade == "positive":
        price += price * 0.25
    elif grade == "negative":
        price -= price * 0.10

elif room == "apartment":
    price = sleeping_in * 25
    if sleeping_in < 10:
        price -= price * 0.3
    elif sleeping_in <= 15:
        price -= price * 0.35
    else:
        price -= price * 0.50
    if grade == "positive":
        price += price * 0.25
    elif grade == "negative":
        price -= price * 0.10

elif room == "president apartment":
    price = sleeping_in * 35
    if sleeping_in < 10:
        price -= price * 0.1
    elif sleeping_in <= 15:
        price -= price * 0.15
    else:
        price -= price * 0.20
    if grade == "positive":
        price += price * 0.25
    elif grade == "negative":
        price -= price * 0.10
print(f"{price:.2f}")
