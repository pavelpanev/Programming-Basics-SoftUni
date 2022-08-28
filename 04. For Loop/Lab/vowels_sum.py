sum_vowels = 0
a_str = input()
for letter in a_str:
    if letter == "a":
        sum_vowels += 1
    elif letter == "e":
        sum_vowels += 2
    elif letter == "i":
        sum_vowels += 3
    elif letter == "o":
        sum_vowels += 4
    elif letter == "u":
        sum_vowels += 5
print(sum_vowels)
