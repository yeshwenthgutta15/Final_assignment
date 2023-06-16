import json

file = open(r"D:\last assignment\employee.json","r")

# it read the file and converted json data into dict and returned it to us
data = json.load(file)
print(data)
print(type(data))



