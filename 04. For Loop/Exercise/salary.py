opened_browsers = int(input())
salary = float(input())

for _ in range(0, opened_browsers):
    website_name = input()
    if website_name == "Facebook":
        salary -= 150
    elif website_name == "Instagram":
        salary -= 100
    elif website_name == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        exit()
print(int(salary))
