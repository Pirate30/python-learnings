import json

file = open('./12 modules/json.json', 'r')
# r - mode - read
data = file.read()  # this data will be in string format
final = json.loads(data)  # loads will convert that into python object
print(final)
print(type(data))  # <class 'str'>
print(type(final))  # <class 'list'>
