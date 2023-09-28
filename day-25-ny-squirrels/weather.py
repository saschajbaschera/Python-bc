import csv
import pandas

# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     new_data = []
#     temperatures = []
#     print(data)
#     for row in data:
#         new_data.append(row)
#
#     data_without_header = new_data[1:]
#
#     for row in data_without_header:
#         temperatures.append(int(row[1]))
#
#     print(temperatures)

# data = pandas.read_csv("weather_data.csv")
# monday = data[data.day == "Monday"]
# print(monday.temp * 9/5 + 32)
# data_dict = {
#     "students": ["Amy", "James", "Angela"]
#     "scores": [76, 56, 71]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(data[data["Primary Fur Color"]] == "Gray")

grey = data[data["Primary Fur Color"] == "Gray"]
red = data[data["Primary Fur Color"] == "Cinnamon"]
black = data[data["Primary Fur Color"] == "Black"]

new_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(grey),  len(red), len(black)],
}
new_file = pandas.DataFrame(new_dict)
new_file.to_csv("squirrel_count.csv")