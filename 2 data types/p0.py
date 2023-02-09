# ? data types in python
# numeric data 
    # integer
    # float
    # complex numbers
# sequence data
    # string
    # list
    # tuple
# dictionary
# set

# ? python divides data types in 2 categories
# mutable - states can be changed
    # list
    # dictionary
    # byte array
# immutable - states can not be changed
    # int
    # float
    # complex
    # string
    # tuple
    # set


# -------------------------------------------------------------------------
# number(immutable)
a=2
b=2.0
c=2+2j
# print(type(a))
# print(type(b))
# print(type(c))


# ------------------------------------------------------------------------
# string(immutable) => It is a collection of single or multiple characters put in a single/double/triple quote
a='this is single line string'
b="this is one more single line string"
c = '''this is
mutiline string'''
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))

# ---------------------------------------------------------------------------
# list(mutable) => order sequence of items - most used - flexible
a = [1,2,3,'yo yo',True,3.5,6+7j]
# print(a, type(a))
# a[3]='yo yo yo'
# print(a, type(a))

# --------------------------------------------------------------------------------

# tuple(immutable) => ordered sequence of items (fastly accesed than list)
a = (1,2,3,'yo yo',True,3.5,6+7j)
# print(a, type(a))


# --------------------------------------------------------------------------------
# dictionary(mutable) => unordered collection of key-value pairs
x={
    "name":'stark',
    "age":20,
    "hobbies": "killing monsters"
}
# print(x, type(x))
# x['age']=25
# print(x, type(x))


# --------------------------------------------------------------------------------
# set(immutable) => unordred collection of unique items
x= {1,2,3,4,'hello',5.5, 1+1j}
# print(x, type(x))
# x= {1,2,3,4,'hello',5.5, 1+1j, 4}
# print(x, type(x))
