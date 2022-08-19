mackerel_price = float(input())
sprat_price = float(input())
bonito_per_kg = float(input())
scad_per_kg = float(input())
clam_per_kg = int(input())

bonito_price = mackerel_price + mackerel_price * 0.6
scad_price = sprat_price + sprat_price * 0.8
clam_price = 7.50

total_price = bonito_per_kg * bonito_price + scad_per_kg * scad_price + clam_per_kg * clam_price
print(f"{total_price:.2f}")
