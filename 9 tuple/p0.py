# TUPLE - sequencial/ordered datatype - immutable - () - comma separated elements
# tuple must contain 1+ elements - tuple with 1 element becomes

# ind 0  1  2  3  4
t = (10, 20, 30, 40, 50)

# print(type(t))  # <class 'tuple'>
# print(t[2]) # 30

# t1 = (10)
# print(type(t1))  # <class 'int'>


# -------------------------------------------------------------
# TUPLE iteration
l = len(t)
for x in range(l):
    # print(x)
    print(t[x])

for x in t:
    print(x)


# -------------------------------------------------------------
