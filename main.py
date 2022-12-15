# import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)

# # printing a coloumn
# temp = data.temp
# print(temp)

# # printing a row
# row = data[data.day == "Monday"]
# print(row)


import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

grey_Squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_Squirrel_count)

Cinnamon_Squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(Cinnamon_Squirrel_count)

Black_Squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(Black_Squirrel_count)


# Now Constructing a data frame using the easiest way i.e. Dictionary
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_Squirrel_count, Cinnamon_Squirrel_count, Black_Squirrel_count]
}
# printing the above dictionary
print(data_dict)
# Converting the above dictionary into a data frame
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
