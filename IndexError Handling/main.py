# Issue: We've got some buggy code, try running the code. The code will crash and give you an IndexError.
# This is because we're looking through the list of fruits for an index that is out of range.

fruits = ["Apple", "Pear", "orange"]


# TODO: Catch the exception and make sure the code runs.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError as error_message:
        print(f"Fruit pie --> cause: {error_message}")
    else:
        print(fruit + "pie")


make_pie(3)
