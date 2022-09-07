interval_start = input()
interval_end = input()
skip = input()
counter = 0
for combination in range(ord(interval_start), ord(interval_end) + 1):
    for combination1 in range(ord(interval_start), ord(interval_end) + 1):
        for combination2 in range(ord(interval_start), ord(interval_end) + 1):
            if chr(combination) == skip or chr(combination1) == skip or chr(combination2) == skip:
                pass
            else:
                print(f"{chr(combination)}{chr(combination1)}{chr(combination2)}", end=" ")
                counter += 1
print(counter)
