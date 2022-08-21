budget = float(input())
workers = int(input())
costume_per_worker = float(input())

expense = budget * 0.10

if workers > 150:
    costume_per_statist = costume_per_worker - costume_per_worker * 0.10
cost_for_movie = costume_per_worker * workers + expense
diff = abs(budget - cost_for_movie)
if cost_for_movie > budget:
    print("Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")
