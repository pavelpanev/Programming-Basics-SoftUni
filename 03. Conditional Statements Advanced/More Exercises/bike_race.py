young_bikers = int(input())
old_bikers = int(input())
trace = input()
collected_sum = 0

if trace == "trail":
    collected_sum += young_bikers * 5.50
    collected_sum += old_bikers * 7
elif trace == "cross-country":
    collected_sum += young_bikers * 8
    collected_sum += old_bikers * 9.50
    if young_bikers + old_bikers >= 50:
        collected_sum -= collected_sum * 0.25
elif trace == "downhill":
    collected_sum += young_bikers * 12.25
    collected_sum += old_bikers * 13.75
elif trace == "road":
    collected_sum += young_bikers * 20
    collected_sum += old_bikers * 21.50
collected_sum -= collected_sum * 0.05
print(f"{collected_sum:.2f}")
