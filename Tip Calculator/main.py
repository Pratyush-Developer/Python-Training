# What was the total bill?
# What percentage tip would you like to give?
# How many people to split the bill?
# Each person should pay:
print("Welcome to the Tip Calculator")
bill = input("What is the total bill?\n$")
percentage = input("What percentage tip would you like to give?\n")
people = input("How many people to slip the bill?\n")
calculate_percentage = int(percentage) / 100
percent_amount = float(bill) * (float(calculate_percentage) + 1)
split_amount = percent_amount / int(people)
final_amount = round(split_amount, 2)
final_amount = "{:.2f}".format(final_amount)
print(f"Each person should pay: ${final_amount}")

