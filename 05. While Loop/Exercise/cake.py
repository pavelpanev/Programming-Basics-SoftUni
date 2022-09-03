width = int(input())
length = int(input())

cake_pieces = width * length
pieces_taken = 0

while cake_pieces > 0:
    currently_taken_pieces = input()
    if currently_taken_pieces == "STOP":
        print(f"{cake_pieces - pieces_taken} pieces are left.")
        break
    else:
        pieces_taken += int(currently_taken_pieces)
        if pieces_taken > cake_pieces:
            diff = pieces_taken - cake_pieces
            print(f"No more cake left! You need {diff} pieces more.")
            break
