months = int(input())
water = 20
internet = 15
other = 0
average = 0
el = 0
for _ in range(0, months):
    electricity_bill = float(input())
    el += electricity_bill
    current_other = (electricity_bill + water + internet) + (electricity_bill + water + internet) * 0.2
    other += current_other
    current_average = water + internet + current_other + electricity_bill
    average += current_average

print(f"Electricity: {el:.2f} lv")
print(f"Water: {(water * months):.2f} lv")
print(f"Internet: {(internet * months):.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {(average / months):.2f} lv")
