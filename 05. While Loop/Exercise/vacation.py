needed_money = float(input())
available_money = float(input())
spend_counter = 0
days = 0
while True:
    action = input()
    amount_for_action = float(input())
    days += 1

    if action == "save":
        spend_counter = 0
        available_money += amount_for_action
        if available_money >= needed_money:
            print(f"You saved the money for {days} days.")
            break

    elif action == "spend":
        spend_counter += 1
        if amount_for_action >= available_money:
            available_money = 0
        else:
            available_money -= amount_for_action
        if spend_counter == 5:
            print(f"You can't save the money.")
            print(f"{days}")
            break
