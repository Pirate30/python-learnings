l = [10,20,30,40,50,0,10]
print(l)

# del - tkes index number and deletes tha element from that number - no returns
# del(l[0])
# print(l)


# pop - same as del but it returns the value that it deleted
# print(l.pop(1))
# print(l)

# remove - removes passed element from the list - no returns
# l.remove(0)
# print(l)

# clear - clears the whole list - no returns
# l.clear()
# print(l)


# insert - takes index number and value - inserts element and shifts preceeding elements one index next
# l.insert(0,'new elem')
# l.insert(5,'new elem')
# l.insert(7,'new elem')
# l.insert(len(l), 'new el em')
# print(l)


# append - adds element on the end of the list
# l.append(-10)
# appends sub array as it is
# l.append([80,90]) #[10, 20, 30, 40, 50, 0, -10, [80, 90]]
# print(l)

# extend - takes list and appends it by destructing it
# l.extend([90,100]) # [10, 20, 30, 40, 50, 0, 90, 100]
# print(l)


# count - counts occurence of passed element
# print(l.count(10))


# max - returns max value from the list
# print(max(l))


# min - returns min value
# print(min(l))


# sort - sorts - no returns
# l.sort()
# print(l)


# reverse - reverses - no returns
# l.reverse()
# print(l)

# index - takes element and retuns index of that elem | the first occurence
print(l.index(10))
print(l.index(50))