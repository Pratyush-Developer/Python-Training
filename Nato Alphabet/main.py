import pandas

# TODO 1. Create a CSV file in dictionary format.

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_frame = pandas.DataFrame(data)
nato_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that user inputs.
def user_input():
    user_name = input("Enter a name: ").upper()
    try:
        user_list = [nato_dict[word] for word in user_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        user_input()
    else:
        print(user_list)


user_input()

