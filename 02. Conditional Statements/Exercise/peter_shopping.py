peter_budget = float(input())
video_card = int(input())
processor = int(input())
ram = int(input())

total_cost_video_cards = video_card * 250
total_cost_processor = (0.35 * total_cost_video_cards) * processor
total_cost_ram = (0.10 * total_cost_video_cards) * ram

total_cost = total_cost_ram + total_cost_video_cards + total_cost_processor

if video_card > processor:
    total_cost -= total_cost * 0.15
diff = abs(peter_budget - total_cost)
if peter_budget >= total_cost:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
