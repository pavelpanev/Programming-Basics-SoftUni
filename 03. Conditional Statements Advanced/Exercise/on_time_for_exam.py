exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_hour = exam_hour * 60
arrival_hour = arrival_hour * 60
exam = exam_hour + exam_minute
arrival = arrival_hour + arrival_minute

if exam == arrival:
    print("On time")
elif exam > arrival:
    diff = exam - arrival
    if diff < 31:
        print("On time")
        print(f"{diff} minutes before the start")
    elif diff <= 59:
        print("Early")
        print(f"{diff} minutes before the start")
    else:
        minutes = diff % 60
        print("Early")
        if minutes < 10:
            print(f"{diff // 60}:0{minutes} hours before the start")
        else:
            print(f"{diff // 60}:{minutes} hours before the start")

elif exam < arrival:
    diff = arrival - exam
    minutes_late = diff % 60
    if diff <= 59:
        print("Late")
        print(f"{minutes_late} minutes after the start")
    else:
        if minutes_late < 10:
            print("Late")
            print(f"{diff // 60}:0{minutes_late} hours after the start")
        else:
            print("Late")
            print(f"{diff // 60}:{minutes_late} hours after the start")
