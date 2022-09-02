username = input()
password = input()

password_attempt = input()

while password_attempt != password:
    password_attempt = input()
else:
    print(f"Welcome {username}!")
