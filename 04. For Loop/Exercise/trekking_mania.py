number_of_groups = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
all_people = 0
for _ in range(0, number_of_groups):
    people_in_group = int(input())
    all_people += people_in_group

    if people_in_group <= 5:
        musala += people_in_group
    elif 6 <= people_in_group <= 12:
        monblan += people_in_group
    elif 13 <= people_in_group <= 25:
        kilimandjaro += people_in_group
    elif 26 <= people_in_group <= 40:
        k2 += people_in_group
    elif people_in_group >= 41:
        everest += people_in_group

percentage_musala = musala / all_people * 100
percentage_monblan = monblan / all_people * 100
percentage_kilimandjaro = kilimandjaro / all_people * 100
percentage_k2 = k2 / all_people * 100
percentage_everest = everest / all_people * 100

print(f"{percentage_musala:.2f}%")
print(f"{percentage_monblan:.2f}%")
print(f"{percentage_kilimandjaro:.2f}%")
print(f"{percentage_k2:.2f}%")
print(f"{percentage_everest:.2f}%")
