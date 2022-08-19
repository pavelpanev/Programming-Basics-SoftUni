veg_per_kg = float(input())
fruits_per_kg = float(input())
all_veg = int(input())
all_fruits = int(input())

veg_price = veg_per_kg * all_veg
fruits_price = fruits_per_kg * all_fruits
final_price = veg_price + fruits_price
euro_price = final_price / 1.94
print(f"{euro_price:.2f}")
