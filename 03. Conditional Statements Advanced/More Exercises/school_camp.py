season = input()
gender = input()
students = int(input())
nights = int(input())
price = 0
sport = ""
if season == "Winter":
    if gender == "boys" or gender == "girls":
        price = students * 9.60 * nights
    elif gender == "mixed":
        price = students * 10 * nights
    if 10 <= students < 20:
        price -= price * 0.05
    elif 20 <= students < 50:
        price -= price * 0.15
    elif 50 <= students:
        price -= price * 0.5
    if gender == "boys":
        sport = "Judo"
    elif gender == "girls":
        sport = "Gymnastics"
    elif gender == "mixed":
        sport = "Ski"

elif season == "Spring":
    if gender == "boys" or gender == "girls":
        price = students * 7.20 * nights
    elif gender == "mixed":
        price = students * 9.50 * nights
    if 10 <= students < 20:
        price -= price * 0.05
    elif 20 <= students < 50:
        price -= price * 0.15
    elif 50 <= students:
        price -= price * 0.5
    if gender == "boys":
        sport = "Tennis"
    elif gender == "girls":
        sport = "Athletics"
    elif gender == "mixed":
        sport = "Cycling"

elif season == "Summer":
    if gender == "boys" or gender == "girls":
        price = students * 15 * nights
    elif gender == "mixed":
        price = students * 20 * nights
    if 10 <= students < 20:
        price -= price * 0.05
    elif 20 <= students < 50:
        price -= price * 0.15
    elif 50 <= students:
        price -= price * 0.5
    if gender == "boys":
        sport = "Football"
    elif gender == "girls":
        sport = "Volleyball"
    elif gender == "mixed":
        sport = "Swimming"
print(f"{sport} {price:.2f} lv.")
