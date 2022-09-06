total_tickets = 0
student_tickets = 0
standart_tickets = 0
kid_tickets = 0
while True:
    movie = input()
    if movie == "Finish":
        break
    else:
        free_spaces = int(input())
        taken_spaces = 0
        while taken_spaces < free_spaces:
            ticket_type = input()
            if ticket_type == "End":
                break
            if ticket_type == "student":
                student_tickets += 1
            elif ticket_type == "standard":
                standart_tickets += 1
            elif ticket_type == "kid":
                kid_tickets += 1
            taken_spaces += 1
            total_tickets += 1

        percentage_full = taken_spaces / free_spaces * 100
        print(f"{movie} - {percentage_full:.2f}% full.")

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets * 100):.2f}% student tickets.")
print(f"{(standart_tickets / total_tickets * 100):.2f}% standard tickets.")
print(f"{(kid_tickets / total_tickets * 100):.2f}% kids tickets.")
