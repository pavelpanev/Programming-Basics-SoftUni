stadium_capacity = int(input())
fans = int(input())
sector_A = 0
sector_B = 0
sector_V = 0
sector_G = 0
for _ in range(0, fans):

    sector = input()
    if sector == "A":
        sector_A += 1
    elif sector == "B":
        sector_B += 1
    elif sector == "V":
        sector_V += 1
    elif sector == "G":
        sector_G += 1
percentage_sector_A = sector_A / fans * 100
percentage_sector_B = sector_B / fans * 100
percentage_sector_V = sector_V / fans * 100
percentage_sector_G = sector_G / fans * 100
percentage_fans = fans / stadium_capacity * 100

print(f"{percentage_sector_A:.2f}%")
print(f"{percentage_sector_B:.2f}%")
print(f"{percentage_sector_V:.2f}%")
print(f"{percentage_sector_G:.2f}%")
print(f"{percentage_fans:.2f}%")
