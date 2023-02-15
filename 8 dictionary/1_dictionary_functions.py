d={
    1:'one',
    2:'two',
    3:'three',
    4:'four',
}
print(d)
# get - takes key and returns the value of that key from the list - returns none is key doesn't exist
# v=d.get(4)
# print(v)


# keys - returns list of keys
# print(d.keys())


# values - returns list of values
# print(d.values())


# items - returns array of (key,value) pairs
# print(d.items()) # dict_items([(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')])


# del - takes input as list[key] & deletes item
# del d[4]
# print(d)


# pop - deletes the item and returns deleted value of the passed key
# x= d.pop(4)
# print(x)
# print(d)


# dict - creates the dictionary
# d1= dict(key='value', key1='value1', key3="value3")
# print(d1)


# update - updates
# d.update({1:'onee'})
# print(d)

# clear - clears the whole dictionary
# d.clear()
# print(d)



# ---------------------------------------------------------
# inserting new value in the dictionary
d[5]='five'
print(d)

# updating without using the update method
d[5]="six"
print(d)