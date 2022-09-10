n = int(input())
print("+", end=" ")
for space in range(n - 2):
    print("-", end=" ")
print("+")

for i in range(n - 2):
    print("|", end=" ")
    print(f"- " * (n - 2), end="")
    print("|")

print("+", end=" ")
for space in range(n - 2):
    print("-", end=" ")
print("+")
