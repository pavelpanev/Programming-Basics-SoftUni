import math

current_record = float(input())
meters_to_swim = float(input())
time_to_swim_1_meter = float(input())

resistance = math.floor(meters_to_swim / 15)
resistance = resistance * 12.5
ivancho_try = (meters_to_swim * time_to_swim_1_meter) + resistance

if ivancho_try < current_record:
    print(f" Yes, he succeeded! The new world record is {ivancho_try:.2f} seconds.")
else:
    diff = abs(current_record - ivancho_try)
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
