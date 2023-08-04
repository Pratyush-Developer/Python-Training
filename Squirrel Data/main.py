import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_count = len(data[data["Primary Fur Color"] == "Gray"])

red_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, red_count, black_count]
}

data_file = pandas.DataFrame(data_dict)
data_file.to_csv("squirrel_count.csv")



