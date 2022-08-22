fuel = input()
fuel_quality = float(input())
card = input()
final_price = 1

if fuel == "Diesel":
    diesel = 2.33
    final_price = diesel * fuel_quality
    if card == "Yes":
        diesel -= 0.12
        final_price = diesel * fuel_quality
    if 20 <= fuel_quality <= 25:
        final_price = final_price - final_price * 0.08
    if fuel_quality > 25:
        final_price = final_price - final_price * 0.10

elif fuel == "Gasoline":
    gasoline = 2.22
    final_price = gasoline * fuel_quality
    if card == "Yes":
        gasoline -= 0.18
        final_price = gasoline * fuel_quality
    if 20 <= fuel_quality <= 25:
        final_price = final_price - final_price * 0.08
    if fuel_quality > 25:
        final_price = final_price - final_price * 0.10

elif fuel == "Gas":
    gas = 0.93
    final_price = gas * fuel_quality
    if card == "Yes":
        gas -= 0.08
        final_price = gas * fuel_quality
    if 20 <= fuel_quality <= 25:
        final_price = final_price - final_price * 0.08
    if fuel_quality > 25:
        final_price = final_price - final_price * 0.10

print(f"{final_price:.2f} lv.")
