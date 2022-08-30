heritage = float(input())
year_to_live = int(input())
ivancho_years = 18
spending = 0

for year in range(1800, year_to_live + 1):
    if year % 2 == 0:
        spending -= 12000
    else:
        spending -= 12000 + 50 * ivancho_years

    ivancho_years += 1

if heritage >= abs(spending):
    n = heritage + spending
    print(f"Yes! He will live a carefree life and will have {n:.2f} dollars left.")
else:
    m = abs(heritage + spending)
    print(f"He will need {m:.2f} dollars to survive.")
