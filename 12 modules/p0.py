# module: collection of variables or classes or functions
# 2 types - predefined modules, user defined modules
# we create in the different file then import it in other file


# importing mod0
# way-1
# import mod0

# # calling a function from mod0
# x = mod0.double(3)
# y = mod0.square(3)
# print(x)  # 6
# print(y)  # 9

# way2
# from mod0 import square, double

# x = double(3)
# y = square(3)

# print(x, y)  # 6 9

# ------------------------------------------
# using alias while imoprting
from mod0 import square as sq, double as doub

x = sq(3)
y = doub(3)

print(x, y)  # 9 6
