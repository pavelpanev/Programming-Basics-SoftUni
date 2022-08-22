fuel = input()
liters_in_tank = int(input())

if fuel == "Diesel" or fuel == "Gasoline" or fuel == "Gas":

    if liters_in_tank >= 25:
        print(f"You have enough {fuel.lower()}.")
    else:
        print(f"Fill your tank with {fuel.lower()}!")
else:
    print("Invalid fuel!")
