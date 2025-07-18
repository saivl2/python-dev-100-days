import random
print("Welcome to the PyPassword Generator!")
num_letters = int(input("How many letters would you like in your password?\n "))
num_symbols = int(input("How many symbols would you like?\n "))
num_numbers = int(input("How many numbers would you like?\n "))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = [
    '.', ',', '!', '?', ';', ':', '-', "'", '"', '(', ')', '[', ']', '{', '}', '/', '\\', '|',
    '@', '#', '$', '%', '^', '&', '*', '+', '=', '<', '>', '~', '`', '_',
    '≤', '≥', '≠', '±', '÷', '×'
]

numbers = [0,1,2,3,4,5,6,7,8,9]
chosen_chars = []
# Choose letters
for _ in range(num_letters):
    chosen_chars.append(random.choice(letters))

# Choose Symbols
for _ in range(num_symbols):
    chosen_chars.append(random.choice(symbols))

# Choose Numbers
for _ in range(num_numbers):
    chosen_chars.append(random.choice(numbers))

# SHuffle the list
random.shuffle(chosen_chars)

password = ''
for item in chosen_chars:
    password += str(item)

print(f"Your password is: {password}")




