# JSON - javascript object notation
# used for storing and transfering data between client and server
# data type supported are:
# string
# number
# bool
# null
# object
# array

import json

# json methods
# dumps() => takes dictionary as input and converts it to json
# d = {
#     1: 'one',
#     2: 'two',
#     3: {
#         'three': 'tres'
#     }
# }
# toJson = json.dumps(d)

# print(d)  # {1: 'one', 2: 'two', 3: {'three': 'tres'}}

# print(type(d))  # <class 'dict'>

# print(toJson)  # {"1": "one", "2": "two", "3": {"three": "tres"}}

# print(type(toJson))  # <class 'str'>


# --------------------------------------------------------
# JSON to python obje
# method used loads()

json_data = '{"one":"1", "two":"2","three":"3"}'
json_data2 = '[{"one":"1", "two":"2","three":"3"}]'

print(json_data)  # {"one":"1", "two":"2","three":"3"}
print(json_data2)  # [{"one":"1", "two":"2","three":"3"}]

print(type(json_data))  # <class 'str'>
print(type(json_data2))  # <class 'str'>

d = json.loads(json_data)
d2 = json.loads(json_data2)

print(d)  # {'one': '1', 'two': '2', 'three': '3'}
print(d2)  # [{'one': '1', 'two': '2', 'three': '3'}]

print(type(d))  # <class 'dict'>
print(type(d2))  # <class 'list'>
