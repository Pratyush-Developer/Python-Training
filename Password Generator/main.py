import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would yu like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
total_letters = ""
total_symbols = ""
total_numbers = ""
for l in range(0, nr_letters):
    count_letters = len(letters)
    random_letters = random.randint(0, count_letters - 1)
    total_letters += letters[random_letters] + " "
for s in range(0, nr_symbols):
    count_symbols = len(symbols)
    random_symbols = random.randint(0, count_symbols - 1)
    total_symbols += symbols[random_symbols] + " "
for n in range(0, nr_numbers):
    count_numbers = len(numbers)
    random_numbers = random.randint(0, count_numbers - 1)
    total_numbers += numbers[random_numbers] + " "
total_password = (total_letters + total_numbers + total_symbols).split(" ")
random.shuffle(total_password)
count_password = len(total_password)
final_password = ""
for p in total_password:
    final_password += p

print(f"Your password is: {final_password}")




