# Exercise 1: You are going to use Dictionary Comprehension to create a dictionary called result that takes each
# word in the given sentence and calculates the number of letters in each word.

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_list = list(sentence.split())

word_dict = {word: len(word) for word in word_list}
print(word_dict)

# Exercise 2: You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each
# temperature in degrees Celcius and converts it into degrees Farenheight.

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(temp_c * 9/5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)

