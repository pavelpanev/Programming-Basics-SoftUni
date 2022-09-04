needed_sum = int(input())
average_cash = 0
average_card = 0
cash_transaction_counter = 0
card_transaction_counter = 0
transaction_number = 1
current_sum = 0
while True:
    if current_sum >= needed_sum:
        print(f"Average CS: {(average_cash / cash_transaction_counter):.2f}")
        print(f"Average CC: {(average_card / cash_transaction_counter):.2f}")
        break
    item_price = input()

    if item_price == "End":
        print("Failed to collect required money for charity.")
        break
    else:
        if transaction_number % 2 == 0:
            if int(item_price) < 10:
                print("Error in transaction!")
            else:
                print("Product sold!")
                average_card += int(item_price)
                card_transaction_counter += 1
                current_sum += int(item_price)
        else:
            if int(item_price) > 100:
                print("Error in transaction!")
            else:
                print("Product sold!")
                average_cash += int(item_price)
                cash_transaction_counter += 1
                current_sum += int(item_price)
    transaction_number += 1
