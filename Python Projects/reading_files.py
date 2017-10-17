# Michael Wu (mvw5mf)

def read_temperature_data(file_name):
    temperatures = []
    data_file = open(file_name, "r")
    burn_line = True

    for line in data_file:
        if burn_line:
            burn_line = False
            continue
        entry = line.split(",")
        temperatures.append(float(entry[1]))

    return temperatures

# input: file name of weather data to read
# output: average temp (float), high temp, low temp
def statistics(file_name):
    temperatures = read_temperature_data(file_name)

    length = len(temperatures)
    total = sum(temperatures)

    return total / length, max(temperatures), min(temperatures)



print(statistics("weather.txt"))



# absolute file path almost never used
# relative paths almost always used