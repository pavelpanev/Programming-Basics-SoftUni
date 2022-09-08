one_lev = int(input())
two_leva = int(input())
five_leva = int(input())
summ = int(input())

for one in range(0, one_lev + 1):
    for two in range(0, two_leva + 1):
        for five in range(0, five_leva + 1):
            if one + two * 2 + five * 5 == summ:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {summ} lv.")
