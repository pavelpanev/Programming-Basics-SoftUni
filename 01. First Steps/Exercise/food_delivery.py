chicken_menus = int(input())
fish_menus = int(input())
vegan_menus = int(input())

chicken_sum = chicken_menus * 10.35
fish_sum = fish_menus * 12.40
vegan_sum = vegan_menus * 8.15
desert = (chicken_sum + fish_sum + vegan_sum) * 0.2
total_sum = chicken_sum + fish_sum + vegan_sum + desert + 2.50
print(total_sum)
