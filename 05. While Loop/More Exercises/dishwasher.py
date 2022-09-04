bottles_washer = int(input())
washings = 1
washer = 750 * bottles_washer
clean_dishes = 0
clean_pots = 0
while True:
    dishes = input()
    if dishes == "End":
        break
    else:
        if washings % 3 == 0:
            washer -= 15 * int(dishes)
            clean_pots += int(dishes)
        else:
            washer -= 5 * int(dishes)
            clean_dishes += int(dishes)
    if washer < 0:
        print(f"Not enough detergent, {abs(washer)} ml. more necessary!")
        exit()

    washings += 1

print("Detergent was enough!")
print(f"{clean_dishes} dishes and {clean_pots} pots were washed.")
print(f"Leftover detergent {washer} ml.")
