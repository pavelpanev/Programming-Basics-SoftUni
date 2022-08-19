all_pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())

hours_to_read = all_pages / pages_per_hour
days = hours_to_read / days_to_read
print(int(days))
