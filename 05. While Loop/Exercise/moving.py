free_space_width = int(input())
free_space_length = int(input())
free_space_height = int(input())
space_taken = 0
cubic_meter_free_space = free_space_width * free_space_length * free_space_height

while True:
    number_of_boxes = input()
    if number_of_boxes == "Done":
        diff = cubic_meter_free_space - space_taken
        print(f"{diff} Cubic meters left.")
        break
    else:
        space_taken += int(number_of_boxes)
        if space_taken > cubic_meter_free_space:
            diff = abs(space_taken - cubic_meter_free_space)
            print(f"No more free space! You need {diff} Cubic meters more.")
            break
