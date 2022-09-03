favourite_book = input()
counter = 0
while True:
    current_book = input()
    counter += 1
    if current_book == favourite_book:
        print(f"You checked {counter - 1} books and found it.")
        break
    elif current_book == "No More Books":
        print("The book you search is not here!")
        print(f"You checked {counter - 1} books.")
        break
