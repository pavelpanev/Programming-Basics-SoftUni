flower_type = input()
flowers = int(input())
budget = int(input())
price = 0

if flower_type == "Roses":
    price = flowers * 5
    if flowers > 80:
        price -= price * 0.10
elif flower_type == "Dahlias":
    price = flowers * 3.8
    if flowers > 90:
        price -= price * 0.15
elif flower_type == "Tulips":
    price = flowers * 2.8
    if flowers > 80:
        price -= price * 0.15
elif flower_type == "Narcissus":
    price = flowers * 3
    if flowers < 120:
        price += price * 0.15
elif flower_type == "Gladiolus":
    price = flowers * 2.5
    if flowers < 80:
        price += price * 0.20
diff = abs(budget - price)
if price <= budget:
    print(f"Hey, you have a great garden with {flowers} {flower_type} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
