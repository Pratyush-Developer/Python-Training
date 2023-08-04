# Exercise 1: You are going to write a List Comprehension to create a new list called squared_numbers.
# This new list should contain every number in the list numbers but each number should be squared.
# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a loop.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(squared_numbers)

# Exercise 2: You are going to write a List Comprehension to create a new list called result. This new list should only
# contain the even number from the list numbers.
# DO NOT modify the List numbers directly. Try to use List Comprehension instead of a loop.

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [n for n in numbers if n % 2 == 0]
print(result)