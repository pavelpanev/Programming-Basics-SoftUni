chrysanthemum = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()
price = 0

if season == "Spring" or season == "Summer":
    if holiday == "Y":
        price += chrysanthemum * (2 + 2 * 0.15)
        price += roses * (4.10 + 4.10 * 0.15)
        price += tulips * (2.50 + 2.50 * 0.15)

    elif holiday == "N":
        price += chrysanthemum * 2
        price += roses * 4.10
        price += tulips * 2.50

    if season == "Spring" and tulips > 7:
        price -= price * 0.05

    if chrysanthemum + roses + tulips > 20:
        price -= price * 0.2

elif season == "Autumn" or season == "Winter":
    if holiday == "Y":
        price += chrysanthemum * (3.75 + 3.75 * 0.15)
        price += roses * (4.50 + 4.50 * 0.15)
        price += tulips * (4.15 + 4.15 * 0.15)

    elif holiday == "N":
        price += chrysanthemum * 3.75
        price += roses * 4.50
        price += tulips * 4.15

    if season == "Winter" and roses >= 10:
        price -= price * 0.1

    if chrysanthemum + roses + tulips > 20:
        price -= price * 0.2
price = price + 2
print(f"{price:.2f}")
