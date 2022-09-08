last_sector = input()
sector_A_rows = int(input())
odd_row_seats = int(input())
counter = 0
for sector in range(ord("A"), ord(last_sector) + 1):
    sector_A_rows += 1
    for row in range(1, sector_A_rows):
        if row % 2 == 0:
            seats = odd_row_seats + 2
        else:
            seats = odd_row_seats
        for seat in range(ord("a"), ord("z")):
            if seats <= 0:
                break
            else:
                print(f"{chr(sector)}{row}{chr(seat)}")
                counter += 1
            seats -= 1
print(counter)
