steps_made = 0
while True:
    steps = input()

    if steps == "Going home":
        steps_to_home = int(input())
        steps_made += steps_to_home
        if steps_made >= 10000:
            diff = steps_made - 10000
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break
        else:
            diff = 10000 - steps_made
            print(f"{diff} more steps to reach goal.")
            break
    else:
        steps_made += int(steps)
        if steps_made >= 10000:
            diff = steps_made - 10000
            print("Goal reached! Good job!")
            print(f"{diff} steps over the goal!")
            break
