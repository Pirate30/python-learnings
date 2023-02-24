# PICKLE - provides powerful algorithm for serialize and de-serialize python data object.
# storing datatypesL
    # bools
    # ints
    # floats
    # complex nums
    # strings
    # tuples
    # lists
    # sets
    # dictionaries

import pickle

# Methods:
# dump - to serialize object hierarchy
# load - to de-serialize object hierarchy

# dump() - takes object and file in args
demo = {
    1:'one', 
    2:'two', 
    3:'three', 
}

pickle_wrt = open("text0.txt", "wb")
# ! wb - it is a mode - write binary
pickle.dump(demo, pickle_wrt)
pickle_wrt.close()

# load

file=open("text0.txt", 'rb')
# ! rb - it is a mode - read binary
res=pickle.load(file)
print(res) # {1: 'one', 2: 'two', 3: 'three'}