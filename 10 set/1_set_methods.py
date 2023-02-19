# set
# add
# pop
# remove
# clear
# discard
# update
# ---------------------------------------

# # set()- converts list into set
# l = [1, 2, 3, 4, 5, 6, 7]
# print(l)  # [1, 2, 3, 4, 5, 6, 7]
# print(type(l))  # <class 'list'>
# s = set(l)
# print(s)  # {1, 2, 3, 4, 5, 6, 7}
# print(type(s))  # <class 'set'>

# ----------------------------------------

# add() - adds passed element into the set
s = {1, 2, 3, 4, 5, 6, 7}
s.add(10)
print(s)

# ------------------------------------------

# pop() - deletes any random element from the set & returns the deleted element
# s.pop()
# print(s)

# ------------------------------------------

# remove() - removes passed element from the set - no returns
# s.remove(10)
# print(s)

# ---------------------------------------------
# discard() - removes passed element from the set - no returns - same as remove
# s.discard(10)
# print(s)

# --------------------------------------------

# clear() - clears the set - set becomes set() - no returns
# s.clear()
# print(s)

# --------------------------------------------
# update() - takes list in the arg - adds those element in the set from the list which are not existing in the set in the first place
# {1, 2, 3, 4, 5, 6, 7, 10}
s.update([5, 12])
print(s)  # {1, 2, 3, 4, 5, 6, 7, 10, 12}
