number_of_cargos = int(input())
all_tons = 0
microbus = 0
truck = 0
train = 0
for _ in range(0, number_of_cargos):
    weight_of_cargo_in_tons = int(input())
    all_tons += weight_of_cargo_in_tons

    if weight_of_cargo_in_tons <= 3:
        microbus += weight_of_cargo_in_tons
    elif 4 <= weight_of_cargo_in_tons <= 11:
        truck += weight_of_cargo_in_tons
    elif weight_of_cargo_in_tons >= 12:
        train += weight_of_cargo_in_tons

average_per_tone = ((microbus * 200) + (truck * 175) + (train * 120)) / all_tons
percentage_microbus = microbus / all_tons * 100
percentage_truck = truck / all_tons * 100
percentage_train = train / all_tons * 100
print(f"{average_per_tone:.2f}")
print(f"{percentage_microbus:.2f}%")
print(f"{percentage_truck:.2f}%")
print(f"{percentage_train:.2f}%")
